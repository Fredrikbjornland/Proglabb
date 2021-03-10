""" Rule file """

from inspect import isfunction


class Rule:
    """ Rule class """
    def __init__(self, s1, s2, signal, action):
        self.state1 = s1
        self.state2 = s2
        self.signal = signal
        self.action = action

    def helperMatch(self, match, value):
        if isfunction(match):
            return match(value)
        return value == match

    def match(self, state, signal):
        return self.helperMatch(self.state1, state) and self.helperMatch(self.signal, signal)
    def fire(self, agent, signal):
        if self.action is not None:
            self.action(agent, signal)
        return self.state2