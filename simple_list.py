import os
import sys
import string

#  Three Classes
#  SimpleList, simpleKey, Color

class SimpleList:

    CURSOR_UP_ONE = "\x1b[1A"
    ERASE_LINE = "\x1b[2K"

    def __init__(self, clear=False):
        self.simple_key = simpleKey()
        self.color = Color()
        if clear:
            self.clear_window()

    def clear_window(self):
        os.system("cls" if os.name == "nt" else "clear")

    def delete_last_lines(self, n=1):
        for _ in range(n):
            sys.stdout.write(SimpleList.CURSOR_UP_ONE)
            sys.stdout.write(SimpleList.ERASE_LINE)
        
    def print_alternatives(self, question, alternatives, alternative_index, go_back):
        print("[{}] {}: {}".format(
            self.color.return_colored("!", "yellow"),
            question,
            self.color.return_colored(alternatives[alternative_index], "bold")
        ))
        for i, alternative in enumerate(alternatives):
            if i == alternative_index:
                if alternative == alternatives[-1] and go_back:
                    print()
                    print("   {}".format(self.color.return_colored("> " + str(alternative), "red")))
                else:
                    print("   {}".format(self.color.return_colored("> " + str(alternative), "cyan")))
            else:
                if alternative == alternatives[-1]:
                    print()
                print("     {}".format(alternative))

    def choose_one(self, question, alternatives, answer_key='answer', get_chosen_index=False, go_back=False):
        """ from a list of alternatives, let user choose one of them """
        
        alternative_index = 0
        answer_from_user = ""
        if go_back:
            alternatives.append(go_back)
        #print the alternatives
        self.print_alternatives(
            question,
            alternatives,
            alternative_index,
            go_back
        )
        while not answer_from_user: # run until the user chooses an alternative
            key = self.simple_key.getKey()
            if key == "up":
                if alternative_index != 0:
                    alternative_index -= 1
            elif key == "down":
                if alternative_index != len(alternatives) - 1:
                    alternative_index += 1
            elif key == "right":
                if get_chosen_index:
                    answer_from_user = {
                        answer_key: alternatives[alternative_index], 
                        "index": alternative_index
                    }
                    if alternative_index == len(alternatives) - 1 and go_back:
                        answer_from_user["index"] = alternatives[alternative_index]
                else:
                    answer_from_user = { answer_key: alternatives[alternative_index] }
            elif key == "left":
                pass
            else:
                if os.name == "nt": # for Windows
                    key = key.decode("utf-8")
                if key not in string.digits and key not in string.ascii_letters and key not in string.punctuation: 
                    if get_chosen_index:
                        answer_from_user = {
                            answer_key: alternatives[alternative_index], 
                            "index": alternative_index
                        }
                        if alternative_index == len(alternatives) - 1 and go_back:
                            answer_from_user["index"] = alternatives[alternative_index]
                    else:
                        answer_from_user = { answer_key: alternatives[alternative_index] }
            self.delete_last_lines(len(alternatives) + 2)
            self.print_alternatives(
                question,
                alternatives,
                alternative_index,
                go_back
            )

        # return answer
        return answer_from_user

    def single_list(self, alternative='Go back'):
        """ 
            Only one alternative. Useful when for instance only giving 
            "Go back" alternative to the user 
        """
        print()
        print(" {}".format(self.color.return_colored("> " + alternative, "red"))) 

        pressed = False

        while not pressed:
            key = self.simple_key.getKey() # get key_press from user
            enter_key = string.digits + string.ascii_letters + string.punctuation
            if key not in enter_key and key != "down" and key != "up":
                pressed = True
            self.delete_last_lines(1)
            print(" {}".format(self.color.return_colored("> " + alternative, "red")))

class simpleKey:

    def __init__(self):
        self.msvcrt = ""

    def get_character(self):
        """ get character input from user """
        try: # Unix
            # only accessible for unix devices
            import termios 
            import tty
            fd = sys.stdin.fileno() 
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                char = sys.stdin.read(1) # read 1 character
            finally:
                # set system instruction on how to get char
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
                return char
        except ModuleNotFoundError: # Windows
            import msvcrt
            self.msvcrt = msvcrt # to use the module in getKey function
            firstChar = msvcrt.getch() # get character that use presses
            return firstChar

    def getKey(self):
        """ 
            format character to key if special key was pressed and return it, 
            else return character unchanged 
        """ 
        firstChar = self.get_character()
        # if statement for Unix
        if firstChar == "\x1b":  # looks like this: ^[
            return {
                "[A": "up", # \x1b[A
                "[B": "down",
                "[C": "right",
                "[D": "left",
            }[self.get_character() + self.get_character()]
        # elif for Windows
        elif firstChar == b"\xe0": # if special key is pressed, for instance arrow keys
            # return "up" if Windows version of arrow key "up" is b"\xe0H etc...
            return {
                b"H": "up", 
                b"P": "down", 
                b"M": "right", 
                b"K": "left"
            }[self.msvcrt.getch()]
        # else
        return firstChar

class Color:
    COLORS = { # define colors that can be used within this class. 
        "CYAN": "\033[96m",
        "DARKCYAN": "\033[36m",
        "BLUE": "\033[94m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "RED": "\033[91m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m", 
    }
    END = "\033[0m" # is used to stop the program from rendering text in X color

    def print_colored(self, text, color):
        """ print a string with colored text """
        print("{}{}{}".format(
            self.COLORS[color.upper()],
            text,
            self.END
        ))

    def return_colored(self, text, color):
        """ return a string with colored text """
        return "{}{}{}".format(
            self.COLORS[color.upper()],
            text,
            self.END
        )