import uuid

class Model:

    _defaults = {}
    
    def __init__(self, **kwargs):
        self.uuid = uuid.uuid4().hex
        for key, defaultVal in self._defaults.iteritems():
            val = kwargs.get(key, defaultVal)
            setattr(self, key, val)

    def update(self, params):
        for key, val in params.iteritems():
            if key in self._defaults:
                setattr(self, key, val)


class EffectsProcessor(Model):

    _defaults = {
        'enabled'    : 0,
        'multiplier' : 1,
        'offset'     : 0,
        'inertia'    : 0
    }

    def __init__(self, **kwargs):
        Model.__init__(self, **kwargs)
        

        
