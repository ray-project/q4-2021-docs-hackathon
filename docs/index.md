# Test CI
![Ray logo](images/ray_header_logo.png)

# If you are building distributed applications
**[Ray Core](ray-distributed-compute/getting-started.md) provides a simple, universal API for building distributed applications.**

Ray accomplishes this mission by:

1. Providing simple primitives for building and running distributed applications.
2. Enabling end users to parallelize single machine code, with little to zero code changes.
3. Including a large ecosystem of applications, libraries, and tools on top of the core Ray to enable complex applications.

<!-- **Ray Core** provides the simple primitives for application building. -->

# If you are building machine learning solutions
On top of Ray Core are several libraries for solving problems in machine learning:

- [Ray Data (beta)](ray-ml/ray-data/getting-started.md): distributed data loading and compute
- [Ray Train](ray-ml/ray-train/getting-started.md): distributed deep learning
- [Ray Tune](ray-ml/ray-tune/getting-started.md): scalable hyperparameter tuning
- [Ray RLlib](ray-ml/ray-rllib/getting-started.md): industry-grade reinforcement learning

As well as libraries for taking ML and distributed apps to production:

- [Ray Serve](ray-ml/ray-serve/getting-started.md): scalable and programmable serving
- [Ray Workflows (alpha)](ray-ml/ray-workflows/getting-started.md): fast, durable application flows

There are also many [community integrations](ecosystem/integrations/integrations.md) with Ray, including [Dask](https://docs.ray.io/en/latest/data/dask-on-ray.html), [MARS](https://docs.ray.io/en/latest/data/mars-on-ray.html), [Modin](https://github.com/modin-project/modin), [Horovod](https://horovod.readthedocs.io/en/stable/ray_include.html), [Hugging Face](https://huggingface.co/transformers/main_classes/trainer.html#transformers.Trainer.hyperparameter_search), [Scikit-learn](ecosystem/integrations/joblib.md), and others. Check out the [full list of Ray distributed libraries here](ecosystem/integrations/integrations.md).


# If you are deploying Ray on your infrastructure
TODO

# Getting Involved

Ray is more than a framework for distributed applications but also an active community of developers,
researchers, and folks that love machine learning. Here's a list of tips for getting involved with the Ray community:

- Join our [community Slack](https://forms.gle/9TSdDYUgxYs8SA9e8) to discuss Ray!
- Star and follow us on [GitHub](https://github.com/ray-project/ray).
- To post questions or feature requests, check out the [Discussion Board](https://discuss.ray.io/).
- Follow us and spread the word on [Twitter](https://twitter.com/raydistributed).
- Join our [Meetup Group](https://www.meetup.com/Bay-Area-Ray-Meetup/) to connect with others in the community.
- Use the `[ray]` tag on [StackOverflow](https://stackoverflow.com/questions/tagged/ray) to ask and answer questions about Ray usage.

If you're interested in contributing to Ray, visit our page on [Getting Involved](contributor-guide/getting-involved.md) to read about the contribution process and see what you can work on!

<!-- 
# More Information

Here are some talks, papers, and press coverage involving Ray and its libraries. Please raise an issue if any of the below links are broken, or if you'd like to add your own talk! -->

<!-- 
Blog and Press
--------------

  - `Modern Parallel and Distributed Python: A Quick Tutorial on Ray <https://towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8>`_
  - `Why Every Python Developer Will Love Ray <https://www.datanami.com/2019/11/05/why-every-python-developer-will-love-ray/>`_
  - `Ray: A Distributed System for AI (BAIR) <http://bair.berkeley.edu/blog/2018/01/09/ray/>`_
  - `10x Faster Parallel Python Without Python Multiprocessing <https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1>`_
  - `Implementing A Parameter Server in 15 Lines of Python with Ray <https://ray-project.github.io/2018/07/15/parameter-server-in-fifteen-lines.html>`_
  - `Ray Distributed AI Framework Curriculum <https://rise.cs.berkeley.edu/blog/ray-intel-curriculum/>`_
  - `RayOnSpark: Running Emerging AI Applications on Big Data Clusters with Ray and Analytics Zoo <https://medium.com/riselab/rayonspark-running-emerging-ai-applications-on-big-data-clusters-with-ray-and-analytics-zoo-923e0136ed6a>`_
  - `First user tips for Ray <https://rise.cs.berkeley.edu/blog/ray-tips-for-first-time-users/>`_
  - [Tune] `Tune: a Python library for fast hyperparameter tuning at any scale <https://towardsdatascience.com/fast-hyperparameter-tuning-at-scale-d428223b081c>`_
  - [Tune] `Cutting edge hyperparameter tuning with Ray Tune <https://medium.com/riselab/cutting-edge-hyperparameter-tuning-with-ray-tune-be6c0447afdf>`_
  - [RLlib] `New Library Targets High Speed Reinforcement Learning <https://www.datanami.com/2018/02/01/rays-new-library-targets-high-speed-reinforcement-learning/>`_
  - [RLlib] `Scaling Multi Agent Reinforcement Learning <http://bair.berkeley.edu/blog/2018/12/12/rllib/>`_
  - [RLlib] `Functional RL with Keras and Tensorflow Eager <https://bair.berkeley.edu/blog/2019/10/14/functional-rl/>`_
  - [Modin] `How to Speed up Pandas by 4x with one line of code <https://www.kdnuggets.com/2019/11/speed-up-pandas-4x.html>`_
  - [Modin] `Quick Tip – Speed up Pandas using Modin <https://pythondata.com/quick-tip-speed-up-pandas-using-modin/>`_
  - `Ray Blog`_

.. _`Ray Blog`: https://ray-project.github.io/

Talks (Videos)
--------------

 - `Unifying Large Scale Data Preprocessing and Machine Learning Pipelines with Ray Datasets | PyData 2021 <https://zoom.us/rec/share/0cjbk_YdCTbiTm7gNhzSeNxxTCCEy1pCDUkkjfBjtvOsKGA8XmDOx82jflHdQCUP.fsjQkj5PWSYplOTz?startTime=1635456658000>`_ `(slides) <https://docs.google.com/presentation/d/19F_wxkpo1JAROPxULmJHYZd3sKryapkbMd0ib3ndMiU/edit?usp=sharing>`_
 - `Programming at any Scale with Ray | SF Python Meetup Sept 2019 <https://www.youtube.com/watch?v=LfpHyIXBhlE>`_
 - `Ray for Reinforcement Learning | Data Council 2019 <https://www.youtube.com/watch?v=Ayc0ca150HI>`_
 - `Scaling Interactive Pandas Workflows with Modin <https://www.youtube.com/watch?v=-HjLd_3ahCw>`_
 - `Ray: A Distributed Execution Framework for AI | SciPy 2018 <https://www.youtube.com/watch?v=D_oz7E4v-U0>`_
 - `Ray: A Cluster Computing Engine for Reinforcement Learning Applications | Spark Summit <https://www.youtube.com/watch?v=xadZRRB_TeI>`_
 - `RLlib: Ray Reinforcement Learning Library | RISECamp 2018 <https://www.youtube.com/watch?v=eeRGORQthaQ>`_
 - `Enabling Composition in Distributed Reinforcement Learning | Spark Summit 2018 <https://www.youtube.com/watch?v=jAEPqjkjth4>`_
 - `Tune: Distributed Hyperparameter Search | RISECamp 2018 <https://www.youtube.com/watch?v=38Yd_dXW51Q>`_

Slides
------

- `Talk given at UC Berkeley DS100 <https://docs.google.com/presentation/d/1sF5T_ePR9R6fAi2R6uxehHzXuieme63O2n_5i9m7mVE/edit?usp=sharing>`_
- `Talk given in October 2019 <https://docs.google.com/presentation/d/13K0JsogYQX3gUCGhmQ1PQ8HILwEDFysnq0cI2b88XbU/edit?usp=sharing>`_
- [Tune] `Talk given at RISECamp 2019 <https://docs.google.com/presentation/d/1v3IldXWrFNMK-vuONlSdEuM82fuGTrNUDuwtfx4axsQ/edit?usp=sharing>`_

Papers
------

- `Ray 1.0 Architecture whitepaper`_ **(new)**
- `Ray Design Patterns`_ **(new)**
- `RLlib paper`_
- `RLlib flow paper`_
- `Tune paper`_

*Older papers:*

- `Ray paper`_
- `Ray HotOS paper`_

.. _`Ray 1.0 Architecture whitepaper`: https://docs.google.com/document/d/1lAy0Owi-vPz2jEqBSaHNQcy2IBSDEHyXNOQZlGuj93c/preview
.. _`Ray Design Patterns`: https://docs.google.com/document/d/167rnnDFIVRhHhK4mznEIemOtj63IOhtIPvSYaPgI4Fg/edit
.. _`Ray paper`: https://arxiv.org/abs/1712.05889
.. _`Ray HotOS paper`: https://arxiv.org/abs/1703.03924
.. _`RLlib paper`: https://arxiv.org/abs/1712.09381
.. _`RLlib flow paper`: https://arxiv.org/abs/2011.12719
.. _`Tune paper`: https://arxiv.org/abs/1807.05118

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Overview of Ray

   ray-overview/index.rst
   ray-libraries.rst
   installation.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Ray Core

   walkthrough.rst
   using-ray.rst
   Ray Job Submission <ray-job-submission/overview.rst>
   configure.rst
   ray-dashboard.rst
   Tutorial and Examples <auto_examples/overview.rst>
   Design patterns and anti-patterns <ray-design-patterns/index.rst>
   package-ref.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Multi-node Ray

   cluster/index.rst
   cluster/quickstart.rst
   cluster/guide.rst
   cluster/reference.rst
   cluster/cloud.rst
   cluster/ray-client.rst
   cluster/deploy.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Ray Serve

   serve/index.rst
   serve/tutorial.rst
   serve/core-apis.rst
   serve/http-servehandle.rst
   serve/deployment.rst
   serve/ml-models.rst
   serve/pipeline.rst
   serve/performance.rst
   serve/architecture.rst
   serve/tutorials/index.rst
   serve/faq.rst
   serve/package-ref.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Ray Data

   data/dataset.rst
   data/dataset-pipeline.rst
   data/dataset-ml-preprocessing.rst
   data/dataset-execution-model.rst
   data/dataset-tensor-support.rst
   data/package-ref.rst
   data/examples/big_data_ingestion
   data/dask-on-ray.rst
   data/mars-on-ray.rst
   data/modin/index.rst
   data/raydp.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Ray Workflows

   workflows/concepts.rst
   workflows/basics.rst
   workflows/management.rst
   workflows/actors.rst
   workflows/events.rst
   workflows/comparison.rst
   workflows/advanced.rst
   workflows/package-ref.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Ray Tune

   tune/index.rst
   tune/key-concepts.rst
   tune/user-guide.rst
   tune/tutorials/overview.rst
   tune/examples/index.rst
   tune/api_docs/overview.rst
   tune/contrib.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Ray RLlib

   rllib/index.rst
   rllib-toc.rst
   rllib/core-concepts.rst
   rllib-training.rst
   rllib-env.rst
   rllib-models.rst
   rllib-algorithms.rst
   rllib-sample-collection.rst
   rllib-offline.rst
   rllib-concepts.rst
   rllib-examples.rst
   rllib/package_ref/index.rst
   rllib-dev.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Ray Train

   train/train.rst
   train/user_guide.rst
   train/examples.rst
   train/architecture.rst
   train/api.rst
   train/migration-guide.rst
   RaySGD v1: Distributed Training Wrappers <raysgd/raysgd.rst>

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: More Libraries

   multiprocessing.rst
   joblib.rst
   xgboost-ray.rst
   lightgbm-ray.rst
   ray-lightning.rst
   ray-collective.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Observability

   ray-metrics.rst
   ray-debugging.rst
   ray-logging.rst
   ray-tracing.rst

.. toctree::
   :hidden:
   :maxdepth: -1
   :caption: Contributor Guide

   getting-involved.rst
   development.rst
   fake-autoscaler.rst
   whitepaper.rst
   debugging.rst
   profiling.rst -->