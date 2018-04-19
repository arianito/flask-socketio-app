from Queue import Queue


class PubSub(object):
    def __init__(self):
        self.subscriber = None
        self.actions = Queue()

    def detach(self):
        self.subscriber = None

    def attach(self, func):
        self.subscriber = func

    def worker(self):
        while not self.actions.empty():
            ac = self.actions.get()
            if self.subscriber:
                self.subscriber(ac['action'], ac['message'])
                self.actions.task_done()

    def publish(self, action, message):
        self.actions.put({'action': action, 'message': message})
