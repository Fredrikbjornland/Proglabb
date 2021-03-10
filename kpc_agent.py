""" The KPC Agent file """

class KPCAgent:
    """ KPCAgent class """
    def __init__(self, keypad, led_board):
        """ Initiate class """
        self.keypad = keypad
        self.led_board = led_board
        self.password_path = "password.txt"
        self.current_password_buffer = ""
        self.override_signal = None
        self.lid = 0
        self.l_dur = 0

    def reset_password_entry(self, signal):
        """ Clear the password-buffer and
        initiate a “power up” lighting
        sequence on the LED Board."""
        self.current_password_buffer = ""
        self.led_board.power_up()

    def get_next_signal(self):
        """ Return the override signal, if it is non-blank;
        otherwise query the keypad for the next pressed key. """
        print("Type in the next signal: ")
        if self.override_signal is not None:
            holder = self.override_signal
            self.override_signal = None
            return holder
        return self.keypad.get_next_signal()

    def append_next_password_digit(self, signal):
        """ Append the signal to the current password """
        if signal:
            self.current_password_buffer += signal
            print("Current password: ", self.current_password_buffer)
        else:
            print("ERROR!")

    def verify_login(self, signal):
        """ Verify that the entered password matches the password from the txt file """
        print("verify login")
        with open(self.password_path, "r") as reader:
            try:
                password = reader.read()
                if self.current_password_buffer == password:
                    self.override_signal = "Y"
                    print("Validated password")
                    self.led_board.successfull()
                else:
                    self.override_signal = "N"
                    print("Not correct password")
                    self.led_board.unsuccessfull()
                    """ Initiate LED lights for failed login """
            except:
                print("Error when reading password")
        reader.close()

    def validate_passcode_change(self, signal):
        print("Validate passcode change")
        """ Check if password is valid, and write to password.txt if it is """
        print("password: ", self.current_password_buffer)
        if not self.current_password_buffer.isdigit() or len(self.current_password_buffer) < 4:
            """ Initiate failed led lights """
            print("New password not valid")
            self.led_board.unsuccessfull()
        else:
            with open(self.password_path, "w") as writer:
                writer.write(self.current_password_buffer)
                print("Password updated")
                self.led_board.successfull()
                """ Initiate successfull LED lights """
            writer.close()
    def set_lid(self, lid):
        """ Set id of the LED that will turn on """
        print("Set lid")
        self.lid = lid

    def set_l_dur(self, l_dur):
        """ Set duration of led """
        print("set dur")
        self.l_dur = l_dur

    def light_one_led(self, signal):
        """ Light the LED """
        print("light led")
        self.led_board.light_led(int(self.lid), int(self.l_dur))

    def reset_agent(self, signal):
        """ Reset agent """
        print("Reset agent")
        self.reset_password_entry("sdf")
        self.override_signal = None

    def power_down(self, signal):
        """ Power down"""
        self.reset_agent(signal)
        print("Powering down")
        self.led_board.power_down()

    def fully_active_agent(self, signal):
        """ Agent is logged in and active"""
        print("Active agent")

