from flux import Store
from appDispatcher import eventDispatcher

__data = {
  'enableArtnet' : False
}

store = Store(eventDispatcher)

def toggle_artnet_handler(store, action):
    __data['enableArtnet'] = bool(action['value'])
    if __data['enableArtnet']:
        print 'artnet enabled'
    else:
        print 'artnet disabled'

store.registerAction('TOGGLE_ARTNET', toggle_artnet_handler)
