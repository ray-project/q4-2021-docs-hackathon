# Model Composition

Ray Serve supports composing individually scalable models into a single model
out of the box. For instance, you can combine multiple models to perform
stacking or ensembles.

To define a higher-level composed model you need to do three things:

1. Define your underlying models (the ones that you will compose together) as
   Ray Serve deployments.
2. Define your composed model, using the handles of the underlying models
   (see the example below).
3. Define a deployment representing this composed model and query it!

In order to avoid synchronous execution in the composed model (e.g., it's very
slow to make calls to the composed model), you'll need to make the function
asynchronous by using an ``async def``. You'll see this in the example below.

That's it. Let's take a look at an example:

```python
from random import random
import requests
import ray
from ray import serve

ray.init(num_cpus=8)
serve.start()

# Our pipeline will be structured as follows:
# - Input comes in, the composed model sends it to model_one
# - model_one outputs a random number between 0 and 1, if the value is
#   greater than 0.5, then the data is sent to model_two
# - otherwise, the data is returned to the user.

# Let's define two models that just print out the data they received.


@serve.deployment
def model_one(data):
    print("Model 1 called with data ", data)
    return random()


model_one.deploy()


@serve.deployment
def model_two(data):
    print("Model 2 called with data ", data)
    return data


model_two.deploy()


# max_concurrent_queries is optional. By default, if you pass in an async
# function, Ray Serve sets the limit to a high number.
@serve.deployment(max_concurrent_queries=10, route_prefix="/composed")
class ComposedModel:
    def __init__(self):
        self.model_one = model_one.get_handle()
        self.model_two = model_two.get_handle()

    # This method can be called concurrently!
    async def __call__(self, starlette_request):
        data = await starlette_request.body()

        score = await self.model_one.remote(data=data)
        if score > 0.5:
            result = await self.model_two.remote(data=data)
            result = {"model_used": 2, "score": score}
        else:
            result = {"model_used": 1, "score": score}

        return result


ComposedModel.deploy()

for _ in range(5):
    resp = requests.get("http://127.0.0.1:8000/composed", data="hey!")
    print(resp.json())
# Output
# {'model_used': 2, 'score': 0.6250189863595503}
# {'model_used': 1, 'score': 0.03146855349621436}
# {'model_used': 2, 'score': 0.6916977560006987}
# {'model_used': 2, 'score': 0.8169693450866928}
# {'model_used': 2, 'score': 0.9540681979573862}
```
