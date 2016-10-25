from Tkinter import *
from appDispatcher import eventDispatcher
from flux import Renderable
import controllers.settings as settingsController
import controllers.effects  as effectsController
import random

class EffectsPane(Frame, Renderable, object):
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


class EffectsProcessor(Frame, Renderable, object):
    
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
        self.deleteButton.grid(row=0, column=3, sticky=E)
        
        self.label = Entry(self)
        self.label.grid(row=0, column=1, columnspan=2, sticky=E+W)
        
        self.scalingFrame = ScalingFrame(
            self,
            multiplierVar=props['multiplier'],
            offsetVar=props['offset'],
            inertiaVar=props['inertia'],
            command=self.dispatchUpdate
        )
        self.scalingFrame.grid(row=1, column=2)
                
        self.eqDisplayIn = EQDisplay(self)
        self.eqDisplayIn.grid(row=1, column=1, padx=2, pady=2, sticky=NW)

        self.eqDisplayOut = EQDisplay(self)
        self.eqDisplayOut.grid(row=2, column=1, padx=2, pady=2, sticky=NW)

        Grid.columnconfigure(self, 1, weight=1)
        self.grid(column=0, padx=2, pady=4, ipadx=15, ipady=15, sticky=E+W)
        self.updateProperties(model)
        
    def renderUpdate(self):
        model = effectsController.getProcessor(self.modelId)
        if model == None:
            self.destroy()
            return
        
        self.updateProperties(model)
        
        if self.__props['enabled'].get():
            self.eqDisplayOut.show()
        else:
            self.eqDisplayOut.hide()


    def updateProperties(self, model):
        for prop in self.__props:
            val = getattr(model, prop)
            self.__props[prop].set(val)
        
        enabled = self.__props['enabled'].get()
            
    
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


class ScalingFrame(Frame, object):
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent)
        self.multiplier = Scale(
            self, 
            from_=100, to=-100, 
            variable=kwargs['multiplierVar'],
            command=kwargs['command'] 
        )
        self.multiplier.grid(row=0, column=1)
        
        self.offset = Scale(
            self, 
            from_=100, to=-100,
            variable=kwargs['offsetVar'],
            command=kwargs['command']
        )
        self.offset.grid(row=0, column=2)

        self.inertia = Scale(
            self, 
            from_=100, to=0,
            variable=kwargs['inertiaVar'],
            command=kwargs['command']
        )
        self.inertia.grid(row=0, column=3)
        

class EQDisplay(Frame, object):
    
    EQ_WIDTH=350
    EQ_HEIGHT=100
    
    def __init__(self, parent):
        Frame.__init__(self, parent, width=self.EQ_WIDTH, height=self.EQ_HEIGHT)
        w = self.EQ_WIDTH
        h = self.EQ_HEIGHT
        
        Grid.columnconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 0, weight=1)
        self.canv = Canvas(self, width=w, height=h, bg='#EEEEEE')
        for left in range(w):
            length = random.randrange(h)
            self.canv.create_line(left, h, left, h-length, fill='black')
        self.show()

    def show(self):
        self.canv.grid(column=0, row=0)
        self.update() # necessary for immediate render

    def hide(self):
        self.canv.grid_forget()