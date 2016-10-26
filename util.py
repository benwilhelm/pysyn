from time      import time
from functools import wraps
from threading import Timer

class throttle(object):
    """
    Decorator that prevents a function from being called more than once every
    time period.
    To create a function that cannot be called more than once a minute:
        @throttle(0.1) # 100ms
        def my_fun():
            pass
    """
    def __init__(self, s=0.1):
        self.throttle_period = s
        self.time_of_last_call = time()

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            now = time()
            time_since_last_call = now - self.time_of_last_call
            if getattr(self, 'timer', None):
                self.timer.cancel()

            if time_since_last_call >= self.throttle_period:
                self.time_of_last_call = now
                return fn(*args, **kwargs)
            else:
                self.timer = Timer(self.throttle_period - time_since_last_call, wrapper, args)
                self.timer.start()

        return wrapper
