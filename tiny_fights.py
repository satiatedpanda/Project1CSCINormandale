from typing import NoReturn, TextIO

"""
    doc comment for things
"""



class StatModifiers: #includes weapons (?)
    """Updates and returns stat modifiers based on input
    """
    def __init__(self) -> None:
        pass

class Abilities:
    """Class of all abilites in the game
    """
    def __init__(self) -> None:
        pass

class Player(StatModifiers, Abilities):
    def __init__(self, title, health,*, weapon="", magic=[], abilites=[]):
        self.title: str = title
        self.weapon: str = weapon
        self.health: int = health
        self.magic: int = magic
        self.abilities: str = abilites

class WarriorOptions(Player):
    """
        Warrior type, good and bad
    """
    def __init__(self, Player) -> None:
        valid_titles: list[str] =[
        "wizard", "waffle house employee", "toddler", "rogue" 
        ]



class MainGame:
    """Main game object
    """
    def __init__(self) -> None:
        person = Player
        self.menu_screen()

    def menu_screen(self) -> None:
        """
            This function prints the main menu screen as well as handles all validations required from the user.
        """
        menu_text: str = "play, exit"
        print(menu_text)
        while True:
            menuinput: str = input("How do you want to proceed? Type \"Play\" or \"Exit\"\n-> ").upper()
            inputcheck: list = ["PL", "EX"] #checking substrings for higher chance of getting right thing
            try: #first layer of input validation
                if any((substring in menuinput for substring in inputcheck)) is False:
                    raise ValueError
                if "PL" in menuinput: #play
                    self.character_select()
                    break
                elif "EX" in menuinput: #exits program
                    leave_y = input("Are you really choosing the option of cowardice? Type \"Y\" if you are paralyzed by fear, or proceed with any other input\n-> ")
                    if leave_y == "Y":
                        print("The art of violent confrontation is not for the meek.")
                        print(".\n.\n.\nExiting Arena.")
                        self.exit_game()
                else: #this is for wrong inputs not caught
                    print("You weren't supposed to see this.\n")
                    raise KeyError
            except ValueError:
                print("Select a valid option.\n")
            except KeyError:
                self.exit_game()
        return None

    def character_select() -> WarriorOptions:
        """
            This function prints the character selection. 
        """
        menu_cs_text: str = "available warriors: wizard, waffle house employee, toddler, rogue"
        print(menu_cs_text)
        #validation stuff
        #confirmation stuff
        print("LET'S GET READY TO RUMBLE!!!!!!")

    def start_game(self) -> None:
        pass
    
    def game(self) -> None:
        pass

    def exit_game(self) -> NoReturn: #DO NOT USE RANDOM EXIT STATEMENTS, call to this function whenever you exit. 
        exit()









if __name__ == '__main__':
    while True:
        MainGame
