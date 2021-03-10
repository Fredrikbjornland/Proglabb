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
        self.testInput = ["4", "5", "3", "4", "5", "2", "*", "Y", "*", "4", "3", "6", "6", "*"]
        self.run()

    def add_all_rules(self):
        self.add_rule(Rule("S-init", "S-Read", all_signals, KPCAgent.reset_password_entry))
        self.add_rule(Rule("S-Read", "S-Read", all_digits, KPCAgent.append_next_password_digit))
        self.add_rule(Rule("S-Read", "S-Verify", '*', KPCAgent.verify_login))
        self.add_rule(Rule("S-Read", "S-init", all_signals, KPCAgent.reset_agent))
        self.add_rule(Rule("S-Verify", "S-Active", 'Y', KPCAgent.fully_active_agent))
        self.add_rule(Rule("S-Verify", "S-init", all_signals, KPCAgent.reset_agent))
        self.add_rule(Rule("S-Active", "S-Led", all_digits, KPCAgent.setLid))
        self.add_rule(Rule("S-Led", "S-Time", "*"))
        self.add_rule(Rule("S-Led", "S-Time", all_digits, KPCAgent.setLDur))
        self.add_rule(Rule('S-Time', 'S-Active', '*', KPCAgent.light_one_led))
        self.add_rule(Rule('S-Active', 'S-Logout', '#'))
        self.add_rule(Rule('S-Logout', 'S-Init', '#', KPCAgent.reset_agent))

        self.add_rule(Rule('S-Active', 'S-Read2', '*', KPCAgent.reset_password_entry))
        self.add_rule(Rule('S-Read2', 'S-Read2', all_digits, KPCAgent.append_next_password_digit))
        self.add_rule(Rule('S-Read2', 'S-Read3', '*', KPCAgent.validate_passcode_change))
        self.add_rule(Rule('S-Read3', 'S-Active', all_signals, KPCAgent.fully_active_agent))

    def add_rule(self, rule):
        """ add rule to rule list"""
        self.rules.append(rule)

    def get_next_signal(self):
        """ Query the agent to get the next signal from the keypad"""
        return self.agent.get_next_signal()

    def run(self):
        """ Start looping though states """
        while self.state != 'S-done':
            self.signal  = self.get_next_signal()
            for rule in self.rules:
                """ Iterate through rules """
                if rule.match(self.state, self.signal):
                   self.state = rule.fire(self.agent, self.signal)
                   print("State: ", self.state)
                   break

        
