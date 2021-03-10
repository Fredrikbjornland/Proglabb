""" The KPC Agent file """
# from fsm import FSM

class KPCAgent:
    """ KPCAgent class """
    def __init__(self, keypad, led_board):
        self.keypad = keypad
        self.led_board = led_board
        self.password_path = "password.txt"
        self.current_password_buffer = ""
        self.override_signal = None
        self.lid = 0
        self.LDur = 0

    def reset_password_entry(self, signal):
        """- Clear the password-buffer and 
        initiate a “power up” lighting
        sequence on the LED Board."""
        print("Reset password")
        self.current_password_buffer = ""
        ## Light up LED
    def do_nothing(self, signal):
        pass
    def get_next_signal(self):
        """ Return the override signal, if it is non-blank; 
        otherwise query the keypad for the next pressed key. """
        print("get next signal")
        if self.override_signal != None:
            holder = self.override_signal
            self.override_signal = None
            return self.holder
        return self.keypad.get_next_signal()

    def append_next_password_digit(self, signal):
        print("Append next password digit")
        print("signal", signal)
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
                    # self.led_board.twinkle_all_leds(1)
                else:
                    self.override_signal = "N"
                    print("Not correct password")
                    # self.led_board.unsuccessfull()
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
            # self.led_board.unsuccessfull()
        else:
            with open(self.password_path, "w") as writer:
                writer.write(self.current_password_buffer)
                print("Passrod updated")
                # self.led_board.successfull()
                """ Initiate successfull LED lights """
            writer.close()
    def setLid(self, lid):
        self.lid = lid

    def setLDur(self, LDur):
        self.LDur = LDur
    
    def light_one_led(self):
        self.led_board.light_led(self.lid, self.LDur)

    def reset_agent(self, signal):
        print("Reset agent")
        self.reset_password_entry("sdf")
        self.override_signal = None

    def fully_active_agent(self, signal):
        print("Active agent")

