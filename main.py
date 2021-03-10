""" File to run program """

from fsm import FSM
from kpc_agent import KPCAgent
from keypad import Keypad
from led_board import LedBoard

def main():
    """ function to run program """
    keypad = Keypad()
    led_board = LedBoard()
    agent = KPCAgent(keypad, led_board)
    fsm = FSM(agent)

if __name__ == "__main__":
    main()
