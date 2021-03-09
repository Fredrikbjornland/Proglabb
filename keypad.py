""" keypad file """

from GPIOSimulator_v5 import *
GPIO = GPIOSimulator()
import time

class Keypad: 
    """ interface between the Keypad Controller agent and the simulated keypad """

    def __init__(self): 
        self.rows = [3, 4, 5, 6]
        self.columns = [7, 8, 9]

        self.symbols = {(3,7): "1", (3,8): "2", (3,9): "3", 
                        (4,7): "4", (4,8): "5", (4,9): "6", 
                        (5,7): "7", (5,8): "8", (5,9): "9", 
                        (6,7): "*", (6,8): "0", (6,9): "#"}
        self.setup()

    def setup(self): 
        """ initialize the row pins as outputs and the column pins as input """
        for row in self.rows:
            GPIO.setup(row, GPIO.OUT)
        for column in self.columns: 
            GPIO.setup(column, GPIO.IN, state=GPIO.LOW)

    def do_polling(self): 
        """ Use nested loops to determine the key currently being
        pressed on the keypad. """
        print("do polling")

        for row in self.rows: 
            GPIO.output(row, GPIO.HIGH)
            for column in self.columns: 
                if (GPIO.input(column) == GPIO.HIGH): 
                    """ sjekker om pin i column er high """
                    location = (row, column) 
                    for key in self.symbols.keys(): 
                        if location == key: 
                            return location
            GPIO.output(row,GPIO.LOW) #resetter til LOW siden bare én skal være HIGH om gangen
        return (-1, -1)

    def get_next_signal(self):
        """ This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected. """
        pressed_pin = self.do_polling()
        while pressed_pin == (-1, -1):
            time.sleep(0.5)
            pressed_pin = self.do_polling()
        print(self.symbols[pressed_pin])
        return self.symbols[pressed_pin]

def main(): 
    keypad = Keypad()
    keypad.get_next_signal()

if __name__ == '__main__':
    main()
