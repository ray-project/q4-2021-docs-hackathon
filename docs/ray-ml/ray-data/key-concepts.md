# Key Concepts

## Deployments

Deployments are the central concept in Ray Serve. They allow you to
define and update your business logic or models that will handle
incoming requests as well as how this is exposed over HTTP or in Python.

A deployment is defined using
`@serve.deployment <ray.serve.api.deployment>` on a Python class (or
function for simple use cases). You can specify arguments to be passed
to the constructor when you call `Deployment.deploy()`, shown below[^1].


``` python title="deployments.py"
{! ray_data.py [ln:1-17] !}
```

1.  :man_raising_hand: Your first deployment!


Deployments can be exposed in two ways: over HTTP or in Python via the
`servehandle-api`. By default, HTTP requests will be forwarded to the
`__call__` method of the class (or the function) and a
`Starlette Request` object will be the sole argument. You can also
define a deployment that wraps a FastAPI app for more flexible handling
of HTTP requests. See `serve-fastapi-http` for details.


## Replicas

A deployment consists of a number of *replicas*, which are individual
copies of the function or class that are started in separate Ray Actors
(processes).

[^1]: This example has been tested independently and was added to this document from a separate Python file.
