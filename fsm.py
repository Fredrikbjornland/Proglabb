""" Finite State Machine file """
from inspect import isfunction

from rule import Rule
from kpc_agent import KPCAgent


def all_signals(signals):
    return signals.isdigit()

def all_digits(test):
    return True

class FSM:
    """ Finite State Machine Class """
    def __init__(self, agent):
        self.rules = []
        self.agent = agent
        self.add_all_rules()
        self.state = "S-init"
        self.signal = None

    def add_all_rules(self):
        self.add_rule(Rule("S-init", "S-Read", all_signals, KPCAgent.reset_password_entry))
        self.add_rule(Rule("S-Read", "S-Read", all_digits, KPCAgent.append_next_password_digit))
        self.add_rule(Rule("S-Read", "S-Verify", '*', KPCAgent.verify_login))
        self.add_rule(Rule("S-Read", "S-init", all_signals, KPCAgent.reset_agent))
        self.add_rule(Rule("S-Verify", "S-Active", 'Y', KPCAgent.fully_active_agent))
        self.add_rule(Rule("S-Verify", "S-init", all_signals, KPCAgent.reset_agent))

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_next_signal(self):
        pass

    def run(self):
        while self.state != 'fsm-end-state':
            self.signal = self.get_next_signal()
            for rule in self.rules:
                if rule.state1 == self.state:
                    self.state = rule.state2
                    rule.action(agent, signal)
        
