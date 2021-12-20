## Getting started with a 10-minute Ray core walk through


This short walk through will quickly get you started with Ray core APIs. It will give you the feel for its simplicity and
velocity with which you can quickly write a distributed application using its distributed primitives. 
More importantly this walk through will provide a preliminary introduction to basics concepts of Ray:

 1. Installing Ray
 2. Starting Ray
 3. Using remote functions (tasks)t
 4. Fetching values from object refs
 5. Specifying resources for tasks
 6. Objects in Ray (object refs)
 7. Using remote classes (actors)

## Installing Ray
To run this walkthrough, install Ray with `pip install -U ray`. 
For the latest wheels (for a snapshot of master), you can use these instructions at [Daily Releases (Nightlies](https://docs.ray.io/en/latest/installation.html#install-nightlies).

## Starting Ray 

You can start Ray cluster with a single node or your laptop and utilize all its multiple cores.

=== "Python"

    ```py
    import ray

    # Start Ray. If you're connecting to an existing cluster, you would use
    # ray.init(address=<cluster-address>) instead.
    
    ray.init()
    ```

=== "C++"

    ```c++
    // Run `ray cpp --show-library-path` to find headers and libraries.
    #include <ray/api.h>
    
    int main(int argc, char **argv) {
      // Start Ray runtime. If you're connecting to an existing cluster, you can set
      // the `RAY_ADDRESS` env var.
      ray::Init();
      ...
    }
    ```

=== "Java"

    ```java
    import io.ray.api.Ray;

    public class MyRayApp {
    
      public static void main(String[] args) {
        // Start Ray runtime. If you're connecting to an existing cluster, you can set
        // the `-Dray.address=<cluster-address>` java system property.
        Ray.init();
        ...
      }
    }
    ```
    

## Remote functions as Tasks

Ray enables arbitrary functions to be executed asynchronously. These asynchronous Ray functions are called “remote functions”. They
return immediately with a future reference, which can be fetched. Here is simple example.

=== "Python"
    
    ```py
    # A regular Python function.
    def my_function():
        return 1
    
    # By adding the `@ray.remote` decorator, a regular Python function
    # becomes a Ray remote function.
    @ray.remote
    def my_function():
        return 1
    
    # To invoke this remote function, use the `remote` method.
    # This will immediately return an object ref (a future) and then create
    # a task that will be executed on a worker process.
    obj_ref = my_function.remote()
    
    @ray.remote
    def slow_function():
        time.sleep(10)
        return 1
    
    # Invocations of Ray remote functions happen in parallel.
    # All computation is performed in the background, driven by Ray's internal event loop.
    obj_refs=[]
    for _ in range(4):
        # This doesn't block.
       obj_ref = slow_function.remote()
       obj_refs.append(obj_ref)
    ```

=== "C++"

    ```c++
    // A regular C++ function.
    int MyFunction() {
      return 1;
    }
    // Register as a remote function by `RAY_REMOTE`.
    RAY_REMOTE(MyFunction);
    
    // Invoke the above method as a Ray remote function.
    // This will immediately return an object ref (a future) and then create
    // a task that will be executed on a worker process.
    auto res = ray::Task(MyFunction).Remote();
    
    // The result can be retrieved with ``ray::ObjectRef::Get``.
    assert(*res.Get() == 1);
    
    int SlowFunction() {
      std::this_thread::sleep_for(std::chrono::seconds(10));
      return 1;
    }
    RAY_REMOTE(SlowFunction);
    
    // Invocations of Ray remote functions happen in parallel.
    // All computation is performed in the background, driven by Ray's internal event loop.
    for(int i = 0; i < 4; i++) {
      // This doesn't block.
      ray::Task(SlowFunction).Remote();
    }
    ```

=== "Java"

    ```java
    public class MyRayApp {
      // A regular Java static method.
      public static int myFunction() {
        return 1;
      }
    }
    
    // Invoke the above method as a Ray remote function.
    // This will immediately return an object ref (a future) and then create
    // a task that will be executed on a worker process.
    ObjectRef<Integer> res = Ray.task(MyRayApp::myFunction).remote();
    
    // The result can be retrieved with ``ObjectRef::get``.
    Assert.assertTrue(res.get() == 1);
    
    public class MyRayApp {
      public static int slowFunction() throws InterruptedException {
        TimeUnit.SECONDS.sleep(10);
        return 1;
      }
    }
    
    // Invocations of Ray remote functions happen in parallel.
    // All computation is performed in the background, driven by Ray's internal event loop.
    for(int i = 0; i < 4; i++) {
      // This doesn't block.
      Ray.task(MyRayApp::slowFunction).remote();
    }
    ```
    
## Fetching returned values 

From the above `my_function`, the result can be retrieved with ``ray.get``, which is a blocking call.

=== "Python"

    ```py
    assert ray.get(obj_ref) == 1
    ```

=== "C++"

    ```c++
    assert(*obj_ref.Get() == 1);
    ```

=== "Java"

    ```Java
    Assert.assertTrue(objRef.get() == 1);
    ```
    
You can also fetch list of objects returned, as we did above. 

=== "Python"
    ```py
    assert ray.get(obj_refs) == [1, 1, 1, 1]
    ```

=== "C++"

    ```c++
    auto results = ray::Get(obj_refs);
    assert(results.size() == 3);
    assert(*results[0] == 1);
    assert(*results[1] == 1);
    assert(*results[2] == 1);
    ```

=== "Java"

    ```java
    List<Integer> results = Ray.get(objectRefs);
    Assert.assertEquals(results, ImmutableList.of(1, 1, 1));
    ```

This will return a list of [1, 1, 1, 1]

## Passing object refs to remote functions
**Object refs** can also be passed into remote functions. When the function actually gets executed, on
a remote host, the argument will be a retrieved in-line from an object store as a **regular object**.
For example, take this function:

=== "Python"

    ```py
    @ray.remote
    def function_with_an_argument(value):
        # argument in-line fetched or resolved as a value
        # no need to explicit ray.get(). Ray will handle resolving
        return value + 1
    
    obj_ref1 = my_function.remote(0)
    assert ray.get(obj_ref1) == 1
    
    # You can pass an object ref as an argument to another Ray remote function.
    obj_ref2 = function_with_an_argument.remote(obj_ref1)
    assert ray.get(obj_ref2) == 2
    ```

=== "C++"

    ```c++
    static int FunctionWithAnArgument(int value) {
      return value + 1;
    }
    RAY_REMOTE(FunctionWithAnArgument);
    
    auto obj_ref1 = ray::Task(MyFunction).Remote(0);
    assert(*obj_ref1.Get() == 1);
    
    // You can pass an object ref as an argument to another Ray remote function.
    auto obj_ref2 = ray::Task(FunctionWithAnArgument).Remote(obj_ref1);
    assert(*obj_ref2.Get() == 2);
    ```

=== "Java"

    ```java
    
    public class MyRayApp {
        public static int functionWithAnArgument(int value) {
            return value + 1;
      }
    }
    
    ObjectRef<Integer> objRef1 = Ray.task(MyRayApp::myFunction).remote(0);
    Assert.assertTrue(objRef1.get() == 1);
    
    // You can pass an object ref as an argument to another Ray remote function.
    ObjectRef<Integer> objRef2 = Ray.task(MyRayApp::functionWithAnArgument, objRef1).remote();
    Assert.assertTrue(objRef2.get() == 2);
    ```

A couple of salient Ray behavior to note here:

1. The second task will not be executed until the first task has finished executing because the second task depends on the output of the first task.

2. If the two tasks are scheduled on different machines, the output of the first task (the value corresponding to **obj_ref1/objRef1**) will be sent over the network to the machine where the second task is scheduled.

## Returning multiple values from Ray tasks

Being true to Pythonic, Ray can return multiple object refs, by specifying in the remote decorator. The 
returned object_refs can be retrieved individually via `ray.get(obj_ref)`.

=== "Python"
    
    ```py
    @ray.remote(num_returns=3)
    def return_multiple():
        return 1, 2, 3
    
    a, b, c = return_multiple.remote()
    assert ray.get(a) == 1
    assert ray.get(b) == 2
    assert ray.get(c) == 3
    ```

## Cancelling Ray tasks
Often you may want to cancel a long-running task on a remote host. You don't know where the task is
scheduled, but using returned obj_ref, you instruct Ray to locate the task and terminate it.

=== "Python"

    ```py
    @ray.remote
    def blocking_operation():
        time.sleep(10e6)
    
    obj_ref = blocking_operation.remote()
    # Use the obj_ref to terminate the remote task
    ray.cancel(obj_ref)
    ```

Fetching an obj_ref of a cancelled task raises and exception. 

=== "Python"

    ```py
    from ray.exceptions import TaskCancelledError
    
    # In case you want to be cautious.
    try:
        ray.get(obj_ref)
    except TaskCancelledError:
        print("Object reference was cancelled.")
    ```

## Specifying resources for a Ray task
For compute intensive Ray application, you may want to assign resources, such as number of CPUs or GPUs.
Ray can then schedule the task on the node on the cluster with the required compute resources.
Ray will automatically detect the available GPUs and CPUs on the machine. However, you can 
override this default behavior by passing in specific resources.

=== "Python"

    ```py
    ray.init(num_cpus=8, num_gpus=4)

    ```

=== "C++"

    ```c++
    RayConfig config;
    config.num_cpus = 8;
    config.num_gpus = 4;
    ray::Init(config);
    ```

=== "Java"

    ```java
    Set Java system property: -Dray.resources=CPU:8,GPU:4
    ```
The resource requirements of a task have implications for the Ray’s scheduling concurrency. In particular, the sum of the 
resource requirements of all concurrently executing tasks on a given node cannot exceed the node’s total resources.

For a specific Ray task, you can specify individual resources as well.

=== "Python"
    
    ```py
    # Specify required resources.
    @ray.remote(num_cpus=4, num_gpus=2)
    def my_function():
        return 1
    ```

=== "C++"

    ```c++
    // Specify required resources.
    ray::Task(MyFunction).SetResource("CPU", 1.0).SetResource("GPU", 4.0).Remote();
    ```

=== "Java"

    ```java
    // Specify required resources.
    Ray.task(MyRayApp::myFunction).setResource("CPU", 1.0).setResource("GPU", 4.0).remote();
    ```

Of the eight CPUs and four GPUs requested, four CPUs and two GPUs will be allocated when
this above task is scheduled for execution.

**Note**:

1. If you do not specify any resources, the default is 1 CPU resource and no other resources. 
2. If specifying CPUs, Ray does not enforce isolation (i.e., your task is expected to honor its request).
3. If specifying GPUs, Ray does provide isolation in forms of visible devices (setting the environment variable **CUDA_VISIBLE_DEVICES**), but it is the task’s responsibility to actually use the GPUs (e.g., through a deep learning framework like TensorFlow or PyTorch).

### Objects in Ray

In Ray, we can create and compute on objects. We refer to these objects as remote objects, and we use object refs to refer to them. 
Remote objects are stored in **shared-memory object stores**, and there is one object store per node in the cluster. In the cluster setting, 
we may not actually know which machine each object lives on.

An *object ref* is essentially a unique ID that can be used to refer to a remote object. If you’re familiar with **futures**, 
our object refs are conceptually similar.

Object refs can be created in multiple ways:

 1. They are returned by remote function calls. 
 2. They are returned by `ray.put`.

For example:

=== "Python"

    ```py
    y = 1
    object_ref = ray.put(y)
    ```

=== "C++"

    ```c++
    // Put an object in Ray's object store.
    int y = 1;
    ray::ObjectRef<int> object_ref = ray::Put(y);
    ```

=== "Java"

    ```java
    // Put an object in Ray's object store.
    int y = 1;
    ObjectRef<Integer> objectRef = Ray.put(y);
    ```
### Fetching Objects in Ray
Ray provides primitives `ray.get(object_ref) to retrieve object refs values from the object store. 
As a developer, you need not worry where or on what node's object store the object ref is stored.
Ray keeps all the bookkeeping and meta-data associated with it and know precisely how to fetch its
associated value.

If the current node’s object store, where `ray.get(object_ref)` is being executed, does not contain the object, the object is downloaded
from where it's stored in the cluster. 

Also, if the object is a **numpy array** or a collection of numpy arrays, the get call is zero-copy and returns arrays backed by shared 
object store memory. Otherwise, we deserialize the object data into a Python object.

=== "Python"
    
    ```py
    # Get the value of one object ref.
    obj_ref = ray.put(1)
    assert ray.get(obj_ref) == 1
    
    # Get the values of multiple object refs in parallel.
    assert ray.get([ray.put(i) for i in range(3)]) == [0, 1, 2]
    
    # You can also set a timeout to return early from a ``get`` that's blocking for too long.
    from ray.exceptions import GetTimeoutError
    
    @ray.remote
    def long_running_function():
        time.sleep(8)
    
    obj_ref = long_running_function.remote()
    try:
        ray.get(obj_ref, timeout=4)
    except GetTimeoutError:
        print("`get` timed out.")
    ```

=== "C++"

    ```c++
    // Get the value of one object ref.
    ray::ObjectRef<int> obj_ref = ray::Put(1);
    assert(*obj_ref.Get() == 1);
    
    // Get the values of multiple object refs in parallel.
    std::vector<ray::ObjectRef<int>> obj_refs;
    for (int i = 0; i < 3; i++) {
      obj_refs.emplace_back(ray::Put(i));
    }
    auto results = ray::Get(obj_refs);
    assert(results.size() == 3);
    assert(*results[0] == 0);
    assert(*results[1] == 1);
    assert(*results[2] == 2);
    ```

=== "Java"

    ```java
    // Get the value of one object ref.
    ObjectRef<Integer> objRef = Ray.put(1);
    Assert.assertTrue(objRef.get() == 1);
    
    // Get the values of multiple object refs in parallel.
    List<ObjectRef<Integer>> objectRefs = new ArrayList<>();
    for (int i = 0; i < 3; i++) {
      objectRefs.add(Ray.put(i));
    }
    List<Integer> results = Ray.get(objectRefs);
    Assert.assertEquals(results, ImmutableList.of(0, 1, 2));
    ```

After launching a number of tasks, you may want to know which ones have finished executing. This can be done 
with `ray.wait`. One way is to fetch only the finished tasks returned. You can programmatically do as follows.

=== "Python"
    
    ```py
    @ray.remote
    def f():
        time.sleep(1)
        return "done"
    
    # Execute `f()` in a comprehension, returning a list of object refs   
    obj_refs =  [f.remote() for i in range(5)])]
    # Iterate over the unfinished tasks
    while len(obj_refs) > 0:
       return_n = 2 if len(obj_refs) > 1 else 1
       # only return no more than two finished tasks. This may block of no tasks are finished yet
       ready_refs, remaining_refs = ray.wait(obj_refs, num_returns=return_n, timeout=10.0)
       # print the finished tasks. This get won't block
       if len(ready_refs) > 0:
          print(ray.get(ready_refs))
       # Update the remaining ones
       obj_refs = remaining_refs
    
    [done, done]
    [done, done]
    [done]
    ```

## Remote Classes as Ray Actors
Actors extend the Ray API from a function as remote-stateless task to class as remote-stateful service. An actor is essentially a 
stateful worker; its class methods can be executed as remote-stateful tasks. Let's see an easy example.

=== "Python"

    ```py
    @ray.remote
    class Counter:
        def __init__(self):
            self.value = 0
        def increment(self, val=1):
            self.value += val
            return self.value
            
    # Create an actor from this class.
    counter = Counter.remote()
    ```

=== "C++"

    ```c++
    // A regular C++ class.
    class Counter {
    
    private:
        int value = 0;
    
    public:
      int Increment() {
        value += 1;
        return value;
      }
    };
    
    // Factory function of Counter class.
    static Counter *CreateCounter() {
        return new Counter();
    };
    
    RAY_REMOTE(&Counter::Increment, CreateCounter);
    
    // Create an actor from this class.
    // `ray::Actor` takes a factory method that can produce
    // a `Counter` object. Here, we pass `Counter`'s factory function
    // as the argument.
    auto counter = ray::Actor(CreateCounter).Remote();
    ```

=== "Java"

    ```java
    // A regular Java class.
    public class Counter {
    
      private int value = 0;
    
      public int increment() {
        this.value += 1;
        return this.value;
      }
    }
    
    // Create an actor from this class.
    // `Ray.actor` takes a factory method that can produce
    // a `Counter` object. Here, we pass `Counter`'s constructor
    // as the argument.
    ActorHandle<Counter> counter = Ray.actor(Counter::new).remote();
    ```
## Specifying required resources
As with Ray tasks, you can allocate compute resources to a Ray actor

=== "Python"

    ```py
    @ray.remote
    class Actor(num_cpus=2, num_gpus=0.5)
        pass
    ```

=== "C++"
    ```c++
    // Specify required resources for an actor.
    ray::Actor(CreateCounter).SetResource("CPU", 2.0).SetResource("GPU", 0.5).Remote();
    ```

=== "Java"

    ```java
    // Specify required resources for an actor.
    Ray.actor(Counter::new).setResource("CPU", 2.0).setResource("GPU", 0.5).remote();
    ```

**Note**: Yes, you can allocate a fraction of a compute resource

## Calling the actor methods
We can interact with the actor by calling its methods with the `remote` operator. We can then call get on the object ref to retrieve 
the actual value.

=== "Python"

    ```py
    assert ray.get(counter.remote()) == 1
    # Send the value 2 as an argument to its method via the `remote` method
    assert ray.get(counter.remote(2) == 3
    ```

=== "C++"
    
    ```c++
    / Call the actor.
    auto object_ref = counter.Task(&Counter::increment).Remote();
    assert(*object_ref.Get() == 1);

    auto object_ref = counter.Task(&Counter::increment).Remote(2);
     assert(*object_ref.Get() == 3);
    ```

=== "Java"

    ```java
    / Call the actor.
    ObjectRef<Integer> objectRef = counter.task(&Counter::increment).remote();
    Assert.assertTrue(objectRef.get() == 1);

    / Call the actor with another value
    ObjectRef<Integer> objectRef = counter.task(&Counter::increment).remote(2);
    Assert.assertTrue(objectRef.get() == 3);
    ```
Observe the state, the current value of the instance variable, is maintained by the remote actor. 

Methods called on different actors can execute in parallel, and methods called on the same actor are executed serially in the order that they are called. Methods on the same actor will share state 
with one another, as shown below.

=== "Python"

    ```py
    # Create ten instances of actors wit Counter
    counters = [Count.remote() for _ in range(10)]
    # Increment each Counter once and get the results. These tasks all happen in parallel
    results = ray.get([c.increment.remote() for c in counters])
    print(results)  # prints [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    # Increment the first Counter five times. These tasks are executed serially
    # and share state.
    results = ray.get([counters[0].increment.remote() for _ in range(5)])
    print(results)  # prints [2, 3, 4 , 5, 6]
    ```

Now that you have take a 10-minute walk through Ray core APIs and how they work, this is a good time
to comprehend some Ray concepts that were used here as well as Ray architecture. 



