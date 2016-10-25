import uuid
import warnings
from pyee import EventEmitter

CHANGE_EVENT = 'change'

class Dispatcher(object):
    
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




class Store(EventEmitter, object):

    def __init__(self, dispatcher):
        EventEmitter.__init__(self)
        self.__actionHandlers = {}
        self.__watchHandlers = []
        self.dispatcherKey = dispatcher.register(self.handleDispatch)
    
    def handleDispatch(self, action):
        for key in self.__actionHandlers:
            if key == action['type']:
                self.__actionHandlers[key](self, action)
        self.emit(CHANGE_EVENT)
    
    def registerAction(self, key, callback):
        self.__actionHandlers[key] = callback



class Renderable(object):

    def subscribeToStore(self, store):
        store.on('change', self.renderUpdate)
    
    def renderUpdate(self):
        className = type(self).__name__
        message = "%s subscribed to store, but didn't define a renderUpdate method"%(className)
        warnings.warn(message)
