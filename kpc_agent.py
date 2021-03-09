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

    def reset_password_entry(self):
        """- Clear the password-buffer and 
        initiate a “power up” lighting
        sequence on the LED Board."""
        self.current_password_buffer = ""
        ## Light up LED

    def get_next_signal(self):
        """ Return the override signal, if it is non-blank; 
        otherwise query the keypad for the next pressed key. """
        if self.override_signal != None:
            return self.override_signal
        self.keypad.get_next_signal()

    def append_next_password_digit(self):
        self.current_password_buffer += "digit"

    def verify_login(self):
        """ Verify that the entered password matches the password from the txt file """
        with open(self.password_path, "r") as reader:
            try:
                password = reader.read()
                print(password)
                if self.current_password_buffer == password:
                    self.override_signal = "Y"
                    """ Initiate LED lights for successfull login """
                else:
                    self.override_signal = "N"
                    """ Initiate LED lights for failed login """
            except:
                print("Error when reading password")
        reader.close()

    def validate_passcode_change(self, new_password):
        """ Check if password is valid, and write to password.txt if it is """
        if not new_password.isdigit() or len(new_password) < 4:
            """ Initiate failed led lights """
            print("New password not valid")
        else:
            try:
                with open(self.password_path, "w") as writer:
                    writer.write(new_password)
                    """ Initiate successfull LED lights """
            except:
                print("Error writing to file")
                """ Initiate error LED lights """
        writer.close()

    def light_one_led(self):
        pass

    def reset_agent(self):
        self.reset_password_entry()

    def fully_active_agent(self):
        return True

