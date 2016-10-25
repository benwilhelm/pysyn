import warnings
import models.model
Model = models.model.Model

class Input(Model):
    def __init__(self, **kwargs):
        Model.__init__(self, **kwargs)


    def getStream(self):
        self._warnUnimplemented('getStream')
