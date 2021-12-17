# Key Concepts

## Deployments

Deployments are the central concept in Ray Serve. They allow you to
define and update your business logic or models that will handle
incoming requests as well as how this is exposed over HTTP or in Python.

A deployment is defined using
`@serve.deployment <ray.serve.api.deployment>` on a Python class (or
function for simple use cases). You can specify arguments to be passed
to the constructor when you call `Deployment.deploy()`, shown below.

``` python
@serve.deployment
class MyFirstDeployment:
  # Take the message to return as an argument to the constructor.
  def __init__(self, msg):
      self.msg = msg

  def __call__(self, request):
      return self.msg

  def other_method(self, arg):
      return self.msg

MyFirstDeployment.deploy("Hello world!")
```

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

