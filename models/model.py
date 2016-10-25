import uuid

class Model(object):

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

    def _warnUnimplemented(self, methodName):
        className = type(self).__name__
        message = "%s must define a %s method"%(className, methodName)
        warnings.warn(message)
    
