class Store():
    
    def __init__(self, dispatcher):
        self.__data = {}
        self.__actionHandlers = {}
        self.__watchHandlers = []
        self.dispatcherKey = dispatcher.register(self.handleDispatch)
    
    def handleDispatch(self, action):
        for key in self.__actionHandlers:
            if key == action['type']:
                self.__actionHandlers[key](action)
    
    def registerAction(self, key, callback):
        self.__actionHandlers[key] = callback

    
