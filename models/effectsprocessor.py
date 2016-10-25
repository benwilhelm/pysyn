import models.model
Model = models.model.Model

class EffectsProcessor(Model):

    _defaults = {
        'enabled'    : 0,
        'multiplier' : 1,
        'offset'     : 0,
        'inertia'    : 0
    }

    def __init__(self, **kwargs):
        Model.__init__(self, **kwargs)
        

        
