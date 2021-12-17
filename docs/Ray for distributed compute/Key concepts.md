# Key concepts

## Ray basics

**Ray Application** <br>
A program including a Ray script that calls ray.init() and uses Ray tasks or actors.

**Tasks (Remote functions)** <br>
Tasks (Remote functions) are asynchronous Ray functions. Ray enables arbitrary functions to be executed asynchronously.

**Actors (Remote Classes)** <br>
An actor is essentially a stateful worker (or a service). When a new actor is instantiated, a new worker is created, and methods of the actor are scheduled on that specific worker and can access and mutate the state of that worker.

**Dependencies, or Environment** <br>
Anything outside of the Ray script that your application needs to run, including files, packages, and environment variables.

**Files**  <br>
Code files, data files or other files that your Ray application needs to run.

**Packages** <br>
External libraries or executables required by your Ray application, often installed via pip or conda.

**Runtime Environments** <br>
A runtime environment describes the dependencies your Ray application needs to run, including files, packages, environment variables, and more. It is installed dynamically on the cluster at runtime.

**Remote objects** <br>
In Ray, we can create and compute on objects. We refer to these objects as remote objects,

**Object refs** <br>
We use object refs to refer to remote objects.

**Object stores** <br>
Remote objects are stored in shared-memory object stores, and there is one object store per node in the cluster. In the cluster setting, we may not actually know which machine each object lives on.


## Running Ray
**Ray runtime** <br>
Ray programs are able to parallelize and distribute by leveraging an underlying Ray runtime. The Ray runtime consists of multiple services/processes started in the background for communication, data transfer, scheduling, and more. The Ray runtime can be started on a laptop, a single server, or multiple servers.

**Cluster** <br>
A Ray cluster consists of a head node and a set of worker nodes.

**Head node** <br>
Te head node is started first in the cluster.

**Worker node** <br>
...

**Ray client** <br>
The Ray Client is an API that connects a Python script to a remote Ray cluster. Effectively, it allows you to leverage a remote Ray cluster just like you would with Ray running on your local machine.

**Local machine and Cluster** <br>
The recommended way to connect to a remote Ray cluster is to use Ray Client, and we will call the machine running Ray Client your local machine.

**Driver** <br>
An entry point of Ray applications that calls ray.init(address=’auto’) or ray.init() 

**Job** <br>
A period of execution between connecting to a cluster with ray.init() and disconnecting by calling ray.shutdown() or exiting the Ray script.

**Namespace** <br>
A namespace is a logical grouping of jobs and named actors. When an actor is named, its name must be unique within the namespace.

### Placement groups
**Bundle** <br>
A bundle is a collection of “resources”, i.e. {“GPU”: 4}. A bundle must be able to fit on a single node on the Ray cluster. Bundles are then placed according to the “placement group strategy” across nodes on the cluster.

**Placement group** <br>
A placement group is a collection of bundles.

**Placement group strategy** <br>
A placement group strategy is an algorithm for selecting nodes for bundle placement. Read more about placement strategies.


## Advanced concepts:

**Serialization and Deserialization** <br>
serialization or serialisation is the process of translating a data structure or object state into a format that can be stored or transmitted and reconstructed later. The opposite operation, extracting a data structure from a series of bytes, is deserialization.

### Memory
#### Ray system memory: memory used internally by Ray

**Redis** <br>
memory used for storing the list of nodes and actors present in the cluster. The amount of memory used for these purposes is typically quite small.

**Raylet** <br>
memory used by the C++ raylet process running on each node. This cannot be controlled, but is typically quite small.

#### Application memory: memory used by your application

**Worker heap** <br>
memory used by your application (e.g., in Python code or TensorFlow), best measured as the resident set size (RSS) of your application minus its shared memory usage (SHR) in commands such as top. The reason you need to subtract SHR is that object store shared memory is reported by the OS as shared with each worker. Not subtracting SHR will result in double counting memory usage.

**Object store memory** <br>
memory used when your application creates objects in the object store via ray.put and when returning values from remote functions. Objects are reference counted and evicted when they fall out of scope. There is an object store server running on each node. In Ray 1.3+, objects will be spilled to disk if the object store fills up.

**Object store shared memory** <br>
memory used when your application reads objects via ray.get. Note that if an object is already present on the node, this does not cause additional allocations. This allows large objects to be efficiently shared among many actors and tasks.


















