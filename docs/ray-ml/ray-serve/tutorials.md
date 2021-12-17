# Tutorials

## Quickstart


By the end of this tutorial, you will have learned the basics of Ray
Serve and will be ready to pick and choose from the advanced topics in
the sidebar.

First, install Ray Serve and all of its dependencies by running the
following command in your terminal:

``` bash
pip install "ray[serve]"
```

Now we will write a Python script to serve a simple "Counter" class over
HTTP. You may open an interactive Python terminal and copy in the lines
below as we go.

First, import Ray and Ray Serve:

``` python
import ray
from ray import serve
```

Ray Serve runs on top of a Ray cluster, so the next step is to start a
local Ray cluster:

``` python
ray.init()
```

Next, start the Ray Serve runtime:

``` python
serve.start()
```



Now we will define a simple Counter class. The goal is to serve this
class behind an HTTP endpoint using Ray Serve.

By default, Ray Serve offers a simple HTTP proxy that will send requests
to the class' `__call__` method. The argument to this method will be a
Starlette `Request` object.

``` python
@serve.deployment
class Counter:
  def __init__(self):
      self.count = 0
  def __call__(self, request):
      self.count += 1
      return {"count": self.count}
```


Notice that we made this class into a `Deployment` with the
`@serve.deployment <ray.serve.api.deployment>` decorator. This decorator
is where we could set various configuration options such as the number
of replicas, unique name of the deployment (it defaults to the class
name), or the HTTP route prefix to expose the deployment at. See the
Deployment API reference for more
details. In order to deploy this, we simply need to call
`Counter.deploy()`.

``` python
Counter.deploy()
```


Now that our deployment is up and running, let's test it out by making a
query over HTTP. In your browser, simply visit
`http://127.0.0.1:8000/Counter`, and you should see the output
`{"count": 1"}`. If you keep refreshing the page, the count should
increase, as expected.

Now let's say we want to update this deployment to add another method to
decrement the counter. Here, because we want more flexible HTTP
configuration we'll use Serve's FastAPI integration. For more
information on this, please see `serve-fastapi-http`.

``` python
from fastapi import FastAPI
app = FastAPI()
@serve.deployment
@serve.ingress(app)
class Counter:
  def __init__(self):
      self.count = 0
  @app.get("/")
  def get(self):
      return {"count": self.count}
  @app.get("/incr")
  def incr(self):
      self.count += 1
      return {"count": self.count}
  @app.get("/decr")
  def decr(self):
      self.count -= 1
      return {"count": self.count}
```

We've now redefined the `Counter` class to wrap a `FastAPI` application.
This class is exposing three HTTP routes: `/Counter` will get the
current count, `/Counter/incr` will increment the count, and
`/Counter/decr` will decrement the count.

To redeploy this updated version of the `Counter`, all we need to do is
run `Counter.deploy()` again. Serve will perform a rolling update here
to replace the existing replicas with the new version we defined.

``` python
Counter.deploy()
```

If we test out the HTTP endpoint again, we can see this in action. Note
that the count has been reset to zero because the new version of
`Counter` was deployed.

``` bash
> curl -X GET localhost:8000/Counter/
{"count": 0}
> curl -X GET localhost:8000/Counter/incr
{"count": 1}
> curl -X GET localhost:8000/Counter/decr
{"count": 0}
```

Congratulations, you just built and ran your first Ray Serve
application! 