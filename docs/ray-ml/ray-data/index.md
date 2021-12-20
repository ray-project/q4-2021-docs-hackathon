# Data: Scalable and Programmable Serving

## Getting Started

Ray Serve is an easy-to-use scalable model serving library built on Ray.
Ray Serve is:


-   **Framework-agnostic**: Use a single toolkit to serve everything
    from deep learning models built with frameworks like
    PyTorch, Tensorflow, and Keras, to Scikit-learn models, to arbitrary Python
    business logic.
-   **Python-first**: Configure your model serving declaratively in pure
    Python, without needing YAML or JSON configs.


Since Ray Serve is built on Ray, it allows you to easily scale to many
machines, both in your datacenter and in the cloud.

Ray Serve can be used in two primary ways to deploy your models at
scale:

1.  Have Python functions and classes automatically placed behind HTTP
    endpoints.
2.  Alternatively, call them from
    `within your existing Python web server <serve-web-server-integration-tutorial>`
    using the Python-native `servehandle-api`.


## Installation

Ray Serve supports Python versions 3.6 through 3.8, with experimental support for Python 3.9. To install Ray
Serve, run the following command:

``` bash
pip install "ray[serve]"
```

## Why Ray Serve?

There are generally two ways of serving machine learning applications,
both with serious limitations: you can use a **traditional web
server**---your own Flask app---or you can use a cloud-hosted solution.

The first approach is easy to get started with, but it's hard to scale
each component. The second approach requires vendor lock-in (SageMaker),
framework-specific tooling (TFServing), and a general lack of
flexibility.

Ray Serve solves these problems by giving you a simple web server (and
the ability to `use your own <serve-web-server-integration-tutorial>`)
while still handling the complex routing, scaling, and testing logic
necessary for production deployments.

Beyond scaling up your deployments with multiple replicas, Ray Serve
also enables:

-   `serve-model-composition`---ability to flexibly compose multiple
    models and independently scale and update each.
-   `serve-batching`---built in request batching to help you meet your
    performance objectives.
-   `serve-cpus-gpus`---specify fractional resource requirements to
    fully saturate each of your GPUs with several models.

For more on the motivation behind Ray Serve, check out these [meetup
slides][] and this [blog post][].

## When should I use Ray Serve?

Ray Serve is a flexible tool that's easy to use for deploying,
operating, and monitoring Python-based machine learning applications.
Ray Serve excels when you want to mix business logic with ML models and
scaling out in production is a necessity. This might be because of
large-scale batch processing requirements or because you want to scale
up a model pipeline consisting of many individual models with different
performance properties.

**If you plan on running on multiple machines, Ray Serve will serve you well!**
