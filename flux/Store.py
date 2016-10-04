from pyee import EventEmitter

CHANGE_EVENT = 'change'

class Store(EventEmitter):
    
    def __init__(self, dispatcher):
        EventEmitter.__init__(self)
        self.data = {}
        self.__actionHandlers = {}
        self.__watchHandlers = []
        self.dispatcherKey = dispatcher.register(self.handleDispatch)
    
    def handleDispatch(self, action):
        for key in self.__actionHandlers:
            if key == action['type']:
                self.__actionHandlers[key](self, action)
        print 'emitting ' + CHANGE_EVENT
        self.emit(CHANGE_EVENT, self.data)
    
    def registerAction(self, key, callback):
        self.__actionHandlers[key] = callback

    
