""" keypad file """

from GPIOSimulator_v5 import *
GPIO = GPIOSimulator()
import time

class Keypad: 
    """ interface between the Keypad Controller agent and the simulated keypad """

    def __init__(self): 
        self.rows = [3, 4, 5, 6]
        self.columns = [7, 8, 9]
        self.symbols = {(0,0): "1", (0,1): "2", (0,2): "3", (1,0): "4", (1,1): "5", (1,2): "6", (2,0): "7", 
                        (2,1): "8", (2,2): "9", (3,0): "*", (3,1): "0", (2,3): "#"}
        self.setup()
            

    def setup(self): 
        """ initialize the row pins as outputs and the column pins as input """
        for row in self.rows:
            GPIO.setup(row, GPIO.OUT)
        for column in self.columns: 
            GPIO.setup(column, GPIO.IN, state=GPIO.LOW)

    def do_polling(self): #må legge til en listener i denne metoden
        """ Use nested loops to determine the key currently being
        pressed on the keypad. """
        print("do polling")
        for row in self.rows:
            GPIO.output(row,GPIO.HIGH)
            for column in self.columns: 
                print("hei")
                if (GPIO.input(column) == GPIO.HIGH):
                    location = (row, column) 
                    for key in self.symbols.keys(): #kanskje gjøre om til list her også
                        if location == key: 
                            print(list(self.symbols.values())[self.symbols.keys().index(key)])
                            return list(self.symbols.values())[self.symbols.keys().index(key)]
            GPIO.output(row,GPIO.LOW)
            return 0


    def get_next_signal(self):
        """ This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected. """
        time.sleep(3)
        while self.do_polling() != 0: 
            time.sleep(3)
            self.do_polling()


def main(): 
    print("hei")
    keypad = Keypad()
    keypad.setup()
    keypad.get_next_signal()

if __name__ == '__main__':
    main()

    