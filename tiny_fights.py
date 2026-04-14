"""
    doc comment for things
"""
class WarriorOptions:
    """
        Warrior type, good and bad
    """
    def __init__(self) -> None:
        valid_titles: list[str] =[
        "wizard", "waffle house employee", "toddler", "rogue" 
        ]

        title: str = ""
        weapon: str = "" #calls another class
        health: int = 0
        magic: int = 0
        abilities: str = "" #calls to ability class

def character_select() -> None:
    """
        This function prints the character selection. 
    """
    menu_cs_text: str = "available warriors: wizard, waffle house employee, toddler, rogue"
    print(menu_cs_text)
    #validation stuff
    #confirmation stuff
    print("LET'S GET READY TO RUMBLE!!!!!!")

def menu_screen() -> None:
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
                character_select()
                break
            elif "EX" in menuinput: #exits program
                leave_y = input("Are you really choosing the option of cowardice? Type \"Y\" if you are paralyzed by fear, or proceed with any other input\n-> ")
                if leave_y == "Y":
                    print("The art of violent confrontation is not for the meek.")
                    print(".\n.\n.\nExiting Arena.")
                    exit()
            else: #this is for wrong inputs not caught
                print("You weren't supposed to see this.\n")
                raise KeyError
        except ValueError:
            print("Select a valid option.\n")
        except KeyError:
            exit()
    return None

if __name__ == '__main__':
    menu_screen()
