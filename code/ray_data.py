from ray import serve


@serve.deployment
class MyFirstDeployment:  # (1)
    # Take the message to return as an argument to the constructor.
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, request):
        return self.msg

    def other_method(self, arg):
        return self.msg

MyFirstDeployment.deploy("Hello world!")
