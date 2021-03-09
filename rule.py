""" Rule file """
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

    def match(self):
        return helperMatch(self.state1, current_state) and helperMatch(self.signal, current_signal)
    def fire(self):
        if self.action is not None:
            self.action(agent, signal)
        return self.state2