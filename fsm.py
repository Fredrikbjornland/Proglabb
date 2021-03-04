""" Finite State Machine file """
form inspect import isfunction

from rule import Rule

class FSM:
    """ Finite State Machine Class """
    def __init__(self, agent):
        self.rules = []
        self.agent = agent
        self.add_all_rules()

    def add_all_rules(self):
        self.add_rule("S-init", "S-Read", all_signals, KPC.reset_password_accumulator)
        self.add_rule("S-Read", "S-Read", all_digits, KPC.append_next_password_digit)
        self.add_rule("S-Read", "S-Verify", '*', KPC.verify_password)
        self.add_rule("S-Read", "S-init", all_signals, KPC.reset_agent)
        self.add_rule("S-Verify", "S-Active", 'Y', KPC.fully_active_agent)
        self.add_rule("S-Verify", "S-init", all_signals, KPC.reset_agent)





    def add_rule(self, rule):
        self.rules.append(rule)

    def get_next_signal(self):

    def run(self):
        while self.state =! 'fsm-end-state':
            self.signal = self.get_next_signal()
        

