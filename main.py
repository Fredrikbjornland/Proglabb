from fsm import FSM
from kpc_agent import KPCAgent
from keypad import Keypad

def main():
    keypad = Keypad()
    agent = KPCAgent(keypad, "led_board når klar")
    fsm = FSM(agent)


if __name__ == "__main__":
    main()