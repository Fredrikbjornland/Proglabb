""" Rule file """

from inspect import isfunction

class Rule:
    """ Rule class """
    def __init__(self, s1, s2, signal, action = None):
        """ Initiate class """
        self.state1 = s1
        self.state2 = s2
        self.signal = signal
        self.action = action

    def helper_match(self, match, value):
        """ Helper method """
        if isfunction(match):
            return match(value)
        return value == match

    def match(self, state, signal):
        """ Check if state and signal match """
        return self.helper_match(self.state1, state) and self.helper_match(self.signal, signal)
    def fire(self, agent, signal):
        """ use action """
        if self.action is not None:
            self.action(agent, signal)
        return self.state2
