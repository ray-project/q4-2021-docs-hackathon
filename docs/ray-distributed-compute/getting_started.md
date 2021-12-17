## Getting started

This short tutorial will quickly get you started with Ray core. It will give you the feel for its simplicity and
velocity with which you can quickly write a distributed application using its distributed primitives. After this short
tutorial or a walk through, we suggest you read the [key concepts](key_concepts.md).

## Installation
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

# The result can be retrieved with ``ray.get``, which is a blocking call.
assert ray.get(obj_ref) == 1

@ray.remote
def slow_function():
    time.sleep(10)
    return 1

# Invocations of Ray remote functions happen in parallel.
# All computation is performed in the background, driven by Ray's internal event loop.
for _ in range(4):
    # This doesn't block.
    slow_function.remote()
```

