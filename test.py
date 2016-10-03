from flux import Dispatcher, Store 

d = Dispatcher.Dispatcher()

s1 = Store.Store(d)
s2 = Store.Store(d)

def action_handler(action):
    print "handled: '%s'"%(action['message'])

s1.registerAction('ACTION_ONE', action_handler)
s2.registerAction('ACTION_TWO', action_handler)


action1 = {
    'type': 'ACTION_ONE',
    'message': 'this is a message one'
}

action2 = {
    'type': 'ACTION_TWO',
    'message': 'this is a message two'
}

d.dispatch(action1)
d.dispatch(action2)
