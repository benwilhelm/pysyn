from flux import Dispatcher, Store, CHANGE_EVENT

d = Dispatcher()

s1 = Store(d)
s2 = Store(d)

def action_handler(store, action):
    print 'handler'
    store.data["value"] = action["value"]

s1.registerAction('SET_VALUE', action_handler)
# s2.registerAction('ACTION_TWO', action_handler)

@s1.on(CHANGE_EVENT)
def on_change(data):
    print 'change: ' + str(data['value'])

action = {
    'type': 'SET_VALUE',
    'value': 4
}

d.dispatch(action)
