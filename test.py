from flux import Dispatcher, Store 

d = Dispatcher.Dispatcher()

s1 = Store.Store(d)
s2 = Store.Store(d)

def action_handler(store, action):
    print 'handler'
    store.data["value"] = action["value"]

s1.registerAction('SET_VALUE', action_handler)
# s2.registerAction('ACTION_TWO', action_handler)

@s1.on(Store.CHANGE_EVENT)
def on_change(data):
    print 'change: ' + str(data['value'])

action = {
    'type': 'SET_VALUE',
    'value': 4
}

d.dispatch(action)
