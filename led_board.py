""" led board interface """
import time
from GPIOSimulator_v5 import *
GPIO = GPIOSimulator()

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

    def light_led(self, led_number, k):
        """ light on one of the six leds """
        for pin_states in self.pin_led_states:
            if led_number == self.pin_led_states.index(pin_states):
                for pin in pin_states:
                    self.set_led_pin(pin_states.index(pin), pin)
        GPIO.show_leds_states()
        time.sleep(k)
        self.turn_off_led(led_number)
        GPIO.show_leds_states()

    def set_led_pin(self, led_pin, pin_state):
        """ set pin based on pin number and their state """
        if pin_state == -1:
            GPIO.setup(led_pin, GPIO.IN)
        else:
            GPIO.setup(led_pin, GPIO.OUT)
            GPIO.output(led_pin, pin_state)

    def turn_off_all_pins(self):
        """ method to turn off all leds by setting all pins to -1 """
        self.set_led_pin(0, -1)
        self.set_led_pin(1, -1)
        self.set_led_pin(2, -1)

    def turn_off_led(self, led_num):
        """" turn off one specific led """
        for led in self.pin_led_states:
            if led_num == self.pin_led_states.index(led):
                for pin in led:
                    self.set_led_pin(led.index(pin), -1)

    def flash_all_leds(self, k):
        """ flash all leds in synchrony for k seconds """
        t_end = time.time() + k
        while time.time() < t_end:
            for pin_states in self.pin_led_states:
                for pin in pin_states:
                    self.set_led_pin(pin_states.index(pin), pin)
                    time.sleep(0.1)
            GPIO.show_leds_states()
            time.sleep(0.02)
            self.turn_off_all_pins()
            GPIO.show_leds_states()

    def twinkle_all_leds(self, k):
        """ turn on and off all leds in sequence for k seconds """
        t_end = time.time() + k
        while time.time() < t_end:
            for led in self.pin_led_states:
                self.light_led(self.pin_led_states.index(led), 0.05)
            GPIO.show_leds_states()

    def power_up(self):
        """ shown when powering up """
        self.flash_all_leds(0.25)
        self.twinkle_all_leds(0.25)

    def power_down(self):
        """ shown when powering down """
        self.twinkle_all_leds(0.25)
        self.flash_all_leds(0.25)

    def successfull(self):
        """ Successfull login LED pattern """
        self.twinkle_all_leds(0.25)

    def unsuccessfull(self):
        """ Unsuccessfull login LED pattern """
        self.flash_all_leds(0.25)

def main():
    """ test """
    ledboard = LedBoard()
    ledboard.light_led(4, 2)
    ledboard.flash_all_leds(2)
    ledboard.twinkle_all_leds(2)

if __name__ == '__main__':
    main()
    