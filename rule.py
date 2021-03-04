""" Rule file """
class Rule:
    """ Rule class """
    def __init__(self, s1, s2, signal, action):
        self.state1, self.state2, self.signal, self.action = s1, s2, signal, action

    def match(self):
        pass
    def fire(self):
        pass