from models.effectsprocessor import AudioProcessor, factory as effectsFactory
from flux import Store
from appDispatcher import eventDispatcher

__data = {
  'processors': {},
  'streamData': {}
}

store = Store(eventDispatcher)
streamStore = Store(eventDispatcher)

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
    processor = __data['processors'][processorId]
    processor.removeListeners()
    __data['processors'].pop(processorId)

store.registerAction('DESTROY_EFFECTS_PROCESSOR', destroyEffectsProcessor)



def streamChunk(store, action):
    params = action['value']
    uuid = params['uuid']
    chunks = {
        'raw': params['raw'],
        'processed': params['processed']
    }
    __data['streamData'][uuid] = chunks

streamStore.registerAction('STREAM_CHUNK', streamChunk)    




def getProcessors():
    return __data['processors']
    
def getProcessor(id):
    return __data['processors'].get(id, None)
    
def getStreamChunk(key):
    (processorId, streamId) = key.split('.')
    if processorId in __data['streamData']:
        return __data['streamData'][processorId][streamId]
    else:
        return None
