""" led board interface """
from GPIOSimulator_v5 import *
GPIO = GPIOSimulator()
import time


class LedBoard: 
    """ interface to the simulated Charlieplexed LED board """

    def __init__(self):
        self.pin_led_states = [
            [1, 0, -1], 
            [0, 1, -1], 
            [-1, 1, 0], 
            [-1, 0, 1],  
            [1, -1, 0], 
            [0, -1, 1], 
        ]

    def light_led(self, led_number): 
        """ light on one of the six leds """
        for pin_states in self.pin_led_states:
            if led_number == self.pin_led_states.index(pin_states):
                for pin in pin_states:
                    self.set_led_pin(pin_states.index(pin), pin)
        print(GPIO.show_leds_states())
                    

    def set_led_pin(self, led_pin, pin_state):
        """ set pin based on pin number and their state """
        if pin_state == -1:
            GPIO.setup(led_pin, GPIO.IN)
        else: 
            GPIO.setup(led_pin, GPIO.OUT)
            GPIO.output(led_pin, pin_state)

    def turn_off_all_pins(self):
        self.set_led_pin(0, -1)
        self.set_led_pin(1, -1)
        self.set_led_pin(2, -1)

    def turn_off_led(self, led_num):
        for led in self.pin_led_states:
            if (led_num == self.pin_led_states.index(led)):
                for pin in led:
                    self.set_led_pin(led.index(pin), -1)

    def flash_all_leds(self, k): 
        """ flash all leds in synchrony for k seconds """
        t_end = time.time() + k
        while time.time() < t_end:
            for pin_states in self.pin_led_states:
                for pin in pin_states:
                    self.set_led_pin(pin_states.index(pin), pin)
                    time.sleep(0.01)           
            print(GPIO.show_leds_states())
            time.sleep(0.01)
            self.turn_off_all_pins()
            print(GPIO.show_leds_states())
    
    def twinkle_all_leds(self, k): 
        """ turn on and off all leds in sequence for k seconds """
        t_end = time.time() + k
        while time.time() < t_end:
            for led in self.pin_led_states:
                self.light_led(self.pin_led_states.index(led))
                self.turn_off_led(self.pin_led_states.index(led)-1)
                time.sleep(0.01)
            print(GPIO.show_leds_states())

    def power_up(self): 
        self.flash_all_leds(1)
        self.twinkle_all_leds(1)

    def power_down(self): 
        self.twinkle_all_leds(1)
        self.flash_all_leds(1)
    

def main(): 
    ledboard = LedBoard()
    ledboard.light_led(4)
    ledboard.flash_all_leds(2)
    ledboard.twinkle_all_leds(2)
    ledboard.power_up()
    ledboard.power_down()

if __name__ == '__main__':
    main()
    