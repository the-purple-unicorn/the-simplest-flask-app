# Class taken from seldon-core example: https://docs.seldon.io/projects/seldon-core/en/latest/python/python_wrapping_docker.html
class MyModel:
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing")

    def predict_raw(self, msg):
        """
        Return a prediction.

        Parameters
        ----------
        msg (dict): this is the json payload of the request
        """
        
        print("adding a field to prove you were here")
        msg["was_hit?"] = 1 
        return msg