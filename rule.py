""" Rule file """
class Rule:
    """ Rule class """
    def __init__(self, s1, s2, signal, action):
        self.state1 = s1
        self.state2 = s2
        self.signal = signal
        self.action = action

    def match(self):
        pass
    def fire(self):
        pass