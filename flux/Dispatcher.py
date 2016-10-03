import uuid

class Dispatcher():
    
    def __init__(self):
        self.__callbacks = {}
    
    def register(self, callback):
        key = uuid.uuid4().hex
        self.__callbacks[key] = callback
        return key
    
    def dispatch(self, action):
        callbacks = self.__callbacks
        for key in callbacks:
            callbacks[key](action)
