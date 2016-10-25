from flux import Store
from appDispatcher import eventDispatcher

__data = {
  'enableArtnet' : False
}

store = Store(eventDispatcher)

def toggle_artnet_handler(store, action):
    __data['enableArtnet'] = bool(action['value'])    
    print 'artnet enabled' if __data['enableArtnet'] else 'artnet disabled'

store.registerAction('TOGGLE_ARTNET', toggle_artnet_handler)


def get_artnet_enabled():
    return __data['enableArtnet']
