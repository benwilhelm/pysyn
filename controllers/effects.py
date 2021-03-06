from models.effectsprocessor import AudioProcessor, factory as effectsFactory
from flux import Store
from appDispatcher import eventDispatcher

__data = {
  'processors': {},
  'streamRegistry': {}
}

store = Store(eventDispatcher)

def newEffectsProcessor(store, action):
    params = action['value']
    processor = effectsFactory(**params)
    processorId = processor.uuid
    __data['processors'][processorId] = processor

store.registerAction('NEW_EFFECTS_PROCESSOR', newEffectsProcessor)


def updateEffectsProcessor(store, action):
    params = action['value']
    processorId = params['uuid']
    processor = __data['processors'][processorId]
    processor.update(params)

store.registerAction('UPDATE_EFFECTS_PROCESSOR', updateEffectsProcessor)


def destroyEffectsProcessor(store, action):
    processorId = action['value']
    __data['processors'].pop(processorId)

store.registerAction('DESTROY_EFFECTS_PROCESSOR', destroyEffectsProcessor)





def getProcessors():
    return __data['processors']
    
def getProcessor(id):
    return __data['processors'].get(id, None)
