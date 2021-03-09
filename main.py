from fsm import FSM
from kpc_agent import KPCAgent
from keypad import Keypad

def main():
    keypad = Keypad()
    agent = KPCAgent(keypad, "led_board når klar")
    fsm = FSM(agent)

    """ Test at verify_login og validate_passcode_change funker """
    agent.verify_login()
    agent.validate_passcode_change("53452")

if __name__ == "__main__":
    main()