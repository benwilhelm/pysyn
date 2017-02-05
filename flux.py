import uuid
import warnings
from pyee import EventEmitter
from Tkinter import Widget

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



class Renderable(Widget, EventEmitter, object):
    
    def __init__(self):
        EventEmitter.__init__(self)
        self._rendering = False

    def subscribeToStore(self, store):
        store.on('change', self.render)
    
    def unsubscribeFromStore(self, store):
        store.remove_listener('change', self.render)
    
    def renderUpdate(self):
        pass
    
    def render(self):
        self.emit('renderStart')
        self._rendering = True
        self.renderUpdate()
        self._rendering = False
        self.emit('renderEnd')
    
    def safeDestroy(self):
        if self._rendering:
            self.once('renderEnd', self.destroy)
            return
        
        self.destroy()
