from Tkinter import *
from appDispatcher import eventDispatcher
from flux import Renderable
import controllers.settings as settingsController
import controllers.effects  as effectsController

class EffectsPane(Frame, Renderable):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Grid.columnconfigure(self, 0, weight=1)
        self.processors = []
        self.subscribeToStore(effectsController.store)        
        newButton = Button(self, text="New Processor", command=self.__newProcessor)
        newButton.grid(column=0, sticky=E)
    
    def renderUpdate(self):        
        ids = map(lambda x: x.modelId, self.processors)
        for key, processor in effectsController.getProcessors().iteritems():
            if key not in ids:
                ep = EffectsProcessor(self, processor)
                self.processors.append(ep)

        

    def __newProcessor(self):
        params = {}
        
        eventDispatcher.dispatch({
          'type': 'NEW_EFFECTS_PROCESSOR',
          'value': params
        })


class EffectsProcessor(Frame, Renderable):
    
    def __init__(self, parent, model):
        Frame.__init__(self, parent, borderwidth=2,  relief=GROOVE)
        self.subscribeToStore(effectsController.store)
        
        self.__props = {
            'enabled'    : IntVar(),
            'multiplier' : IntVar(),
            'offset'     : IntVar(),
            'inertia'    : IntVar()
        }
        
        props = self.__props
        
        self.modelId = model.uuid
        self.enableButton = Checkbutton(
            self, 
            variable=props['enabled'], 
            command=self.dispatchUpdate
        )
        self.enableButton.grid(row=0, column=0)
        
        self.deleteButton = Button(self, command=self.dispatchDestroy, text="X")
        self.deleteButton.grid(row=0, column=2, sticky=E)
        
        self.label = Entry(self)
        self.label.grid(row=0, column=1, sticky=E+W)
        
        self.sliderFrame = Frame(self)
        self.sliderFrame.grid(row=1, column=2)
        
        self.multiplier = Scale(
            self.sliderFrame, 
            from_=100, to=-100, 
            variable=props['multiplier'],
            command=self.dispatchUpdate 
        )
        self.multiplier.grid(row=0, column=1)
        
        self.offset = Scale(
            self.sliderFrame, 
            from_=100, to=-100,
            variable=props['offset'],
            command=self.dispatchUpdate
        )
        self.offset.grid(row=0, column=2)

        self.inertia = Scale(
            self.sliderFrame, 
            from_=100, to=0,
            variable=props['inertia'],
            command=self.dispatchUpdate
        )
        self.inertia.grid(row=0, column=3)

        Grid.columnconfigure(self, 1, weight=1)
        self.grid(column=0, padx=2, pady=4, ipadx=15, ipady=15, sticky=E+W)
        self.updateProperties(model)
        
    def renderUpdate(self):
        model = effectsController.getProcessor(self.modelId)
        if model == None:
            self.destroy()
            return
        
        self.updateProperties(model)


    def updateProperties(self, model):
        for prop in self.__props:
            val = getattr(model, prop)
            self.__props[prop].set(val)
        
        enabled = self.__props['enabled'].get()
        print 'enabled %d'%(enabled)
            
    
    def dispatchUpdate(self, *args):
        params = { 'uuid': self.modelId }
        for prop, var in self.__props.iteritems():
            params[prop] = var.get()
        
        eventDispatcher.dispatch({
            'type': 'UPDATE_EFFECTS_PROCESSOR',
            'value': params
        })
    
    def dispatchDestroy(self):
        eventDispatcher.dispatch({
            'type': 'DESTROY_EFFECTS_PROCESSOR',
            'value': self.modelId
        })
