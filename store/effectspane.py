from flux import Store
from appDispatcher import eventDispatcher

__data = {
  'pitchText' : '--'
}

store = Store(eventDispatcher)

def update_pitch_text(store, action):
    __data['pitchText'] = str(action['value'])

store.registerAction('UPDATE_PITCH', update_pitch_text)



def get_pitch_text():
    return __data['pitchText']
