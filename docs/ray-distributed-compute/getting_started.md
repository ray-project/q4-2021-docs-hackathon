## Getting started with a Ray core walk through


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

```
import ray

# Start Ray. If you're connecting to an existing cluster, you would use
# ray.init(address=<cluster-address>) instead.

ray.init()
```

## Remote functions (Tasks)

Ray enables arbitrary functions to be executed asynchronously. These asynchronous Ray functions are called “remote functions”. They
return immediately with a future reference, which can be fetched. Here is simple example.

```
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
## Fetching returned values 

From the above `my_function`, the result can be retrieved with ``ray.get``, which is a blocking call.
```
assert ray.get(obj_ref) == 1
```

You can also fetch list of objects returned, as we did above. 
```
assert ray.get(obj_refs) == [1, 1, 1, 1]
```
This will return a list of [1, 1, 1, 1]

## Passing object refs to remote functions
**Object refs** can also be passed into remote functions. When the function actually gets executed, on
a remote host, the argument will be a retrieved in-line from an object store as a **regular object**.
For example, take this function:

```
@ray.remote
def function_with_an_argument(value):
    # argument in-line fetched or resolved as a value
    # no need to explicit ray.get(). Ray will handle resolving
    return value + 1

obj_ref1 = my_function.remote()
assert ray.get(obj_ref1) == 1

# You can pass an object ref as an argument to another Ray remote function.
obj_ref2 = function_with_an_argument.remote(obj_ref1)
assert ray.get(obj_ref2) == 2
```

A couple of salient Ray behavior to note here:

1. The second task will not be executed until the first task has finished executing because the second task depends on the output of the first task.

2. If the two tasks are scheduled on different machines, the output of the first task (the value corresponding to **obj_ref1/objRef1**) will be sent over the network to the machine where the second task is scheduled.

## Returning multiple values from Ray tasks

Being true to Pythonic, Ray can return multiple object refs, by specifying in the remote decorator. The 
returned object_refs can be retrieved individually via `ray.get(obj_ref)`.

```
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

```
@ray.remote
def blocking_operation():
    time.sleep(10e6)

obj_ref = blocking_operation.remote()
# Use the obj_ref to terminate the remote task
ray.cancel(obj_ref)
```

Fetching an obj_ref of a cancelled task raises and exception. 
```
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

```
ray.init(num_cpus=8, num_gpus=4)

```
For a specific Ray task, you can specify individual resources as well.
```
# Specify required resources.
@ray.remote(num_cpus=4, num_gpus=2)
def my_function():
    return 1
```
Of the eight CPUs and four GPUs requested, four CPUs and two GPUs will be allocated when
this above task is scheduled for execution.