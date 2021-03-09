""" Finite State Machine file """
from inspect import isfunction

from rule import Rule
from kpc_agent import KPCAgent


def all_signals(signal): return True

def all_digits(signal): return 48 <= ord(signal) <= 57

class FSM:
    """ Finite State Machine Class """
    def __init__(self, agent):
        self.rules = []
        self.agent = agent
        self.add_all_rules()
        self.state = "S-init"
        self.signal = None
        self.testInput = ["4", "5", "3", "4", "5", "2", "*"]
        self.run()

    def add_all_rules(self):
        self.add_rule(Rule("S-init", "S-Read", all_signals, KPCAgent.reset_password_entry))
        self.add_rule(Rule("S-Read", "S-Read", all_digits, KPCAgent.append_next_password_digit))
        self.add_rule(Rule("S-Read", "S-Verify", '*', KPCAgent.verify_login))
        self.add_rule(Rule("S-Read", "S-init", all_signals, KPCAgent.reset_agent))
        self.add_rule(Rule("S-Verify", "S-Active", 'Y', KPCAgent.fully_active_agent))
        self.add_rule(Rule("S-Verify", "S-init", all_signals, KPCAgent.reset_agent))
        self.add_rule(Rule("S-Active", "S-led", all_digits, KPCAgent.setLid))
        self.add_rule(Rule("S-led", "S-time", "*", KPCAgent.do_nothing))
        self.add_rule(Rule("S-led", "S-time", "*", KPCAgent.setLDur))


    def add_rule(self, rule):
        self.rules.append(rule)

    def get_next_signal(self):
        return self.agent.get_next_signal()

    def run(self):
        i = 0
        while self.state != 'fsm-end-state' and i < len(self.testInput):
            # self.signal = self.get_next_signal()
            self.signal = self.testInput[i]
            for rule in self.rules:
                if isfunction(rule.signal):
                    print(self.signal)
                    if rule.state1 == self.state and rule.signal(self.signal):
                        self.state = rule.state2
                        rule.action(self.agent, self.signal)
                        break
                else:
                    if rule.state1 == self.state and rule.signal == self.signal:
                        self.state = rule.state2
                        rule.action(self.agent, self.signal)
                        break
            i += 1
        
