from typing import NoReturn
from random import randint

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


class Weapon: 
    def __init__(self, weapon_type = 0): 
        self.dmg = 30 
        self.accuracy = 90 
        self.crit_chance = 10
        
        if weapon_type == "Sword":
            self.weapon_type = "Sword"
            self.dmg = 30    
            self.accuracy = 90
            self.crit_chance = 10
    
        if weapon_type == "Spear":
            self.weapon_type = "Spear"
            self.dmg = 40    
            self.accuracy = 80
            self.crit_chance = 20
    

        if weapon_type == "Axe":
            self.weapon_type = "Axe"
            self.dmg = 50    
            self.accuracy = 80
            self.crit_chance = 30
    

        if weapon_type == "Tome":
            self.weapon_type = "Tome"
            self.dmg = 30    
            self.accuracy = 50
            self.crit_chance = 50
    

        if weapon_type == "Spatula":
            self.weapon_type = "Spatula"
            self.dmg = 35   
            self.accuracy = 85
            self.crit_chance = 10
    
        if weapon_type == "Blankie":
            self.weapon_type = "Blankie"
            self.dmg = 10    
            self.accuracy = 100
            self.crit_chance = 1

        else: 
            self.weapon_type = "Fists"
            self.dmg = 20    
            self.accuracy = 100
            self.crit_chance = 20

    def start_game(self) -> None:
        pass
    
    def game(self) -> None:
        pass

    def exit_game(self, noexit=False) -> NoReturn: #DO NOT USE RANDOM EXIT STATEMENTS, call to this function whenever you exit. 
        if noexit == False:
            exit()
        print("restarting game...\n")

class Person:
    def __init__(self, *, title="", health=0, magic=[]):
        self.health = health
        self.title = title
        self.magic = magic
    
    def assign_items(self):
        if self.title != "":
            return "error"
        

    def assign_magic(self):
        pass

class Player(Person):
    def __init__(self, title: str, health: int,*, weapon = Weapon("Fists"), magic: list[str]=[], items: list[str]=[]):
        super().__init__(title=title, health=health, magic=magic)
        self.weapon: Weapon = weapon
        self.items: str = items

class Enemy(Person):
    def __init__(self):
        super().__init__()

        self.title
        self.health
        self.weapon
        self.magic
        self.items

class WarriorOptions:
    """
        Warrior type, good and bad
    """
    def __init__(self) -> None:
        valid_titles: list[str] =[
        "wizard", "waffle house employee", "toddler", "rogue" 
        ]

class MainGame:
    """Main game object
    """
    def __init__(self) -> None:
        self.menu_screen()
        self.exit_game(noexit=True)

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
                    character_selected = self.character_select()
                    break
                elif "EX" in menuinput: #exits program
                    leave_y = input("Are you really choosing the option of cowardice? Type \"Y\" if you are paralyzed by fear, or proceed with any other input\n-> ").upper()
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

    def character_select(self) -> None:
        """
            This function prints the character selection. 
        """
        while True:
            menu_cs_text: str = "available warriors: wizard, waffle house employee, toddler, rogue"
            print(menu_cs_text)
            menuinput: str = input("Choose your Fighter. Enter Fighter type or \"Exit\"\n-> ").upper()
            inputcheck: list = ["WIZ", "WAF", "TO", "RO", "EX"] #checking substrings for higher chance of getting right thing
            character: str = "" #temporary variable
            try: #first layer of input validation
                if any((substring in menuinput for substring in inputcheck)) is False:
                    raise ValueError
                elif "EX" in menuinput: #exits program
                    leave_y = input("Do you really want to leave? Type \"Y\" if so or anything else to continue.\n-> ")
                    if leave_y == "Y":
                        print(".\n.\n.\nExiting Arena.")
                        exit()
                elif "WIZ" or "WAF" or "TO" or "RO" in menuinput: #continues with char select
                    character_list = ["WIZARD", "WAFFLE HOUSE EMPLOYEE", "TODDLER", "ROUGE"]
                    #https://stackoverflow.com/questions/2170900/get-first-list-index-containing-sub-string
                    character: str = character_list[[idx for idx, string in enumerate(character_list) if menuinput in string][0]].title() 
                    confirm_y = input(f"Is {character} the Fighter you want? Enter Y/N\n-> ") #or confirm
                    if confirm_y == "Y":
                        self.weapon_slecect_menu()
                        break
                    #else:
                        #kick back to prev option
                else: #this is for wrong inputs not caught
                    print("You weren't supposed to see this.\n")
                    raise KeyError
            except ValueError:
                print("Select a valid option.\n")
            return character

    def weapon_select_menu(character: str) -> None: 
        if character == "WIZ":
            print("""
            ------------------------------------------------------
                            Pick Your Weapon
            ------------------------------------------------------
                            Damage:      30 
                Sword       Hit Chance:  90   Type Sword To Pick
                            Crit Chance: 10
            ------------------------------------------------------
                            Damage:      40
                Spear       Hit Chance:  80   Type Spear To Pick
                            Crit Chance: 20     
            ------------------------------------------------------
                            Damage:      30
                Tome        Hit Chance:  50   Type Tome To Pick
                            Crit Chance  50
            ------------------------------------------------------
    """)
            weapon_list = ["Sword","Spear","Tome"]
            response = input(str())
            if response in weapon_list:
                choice: str = str(response)
                selected_weapon = Weapon(weapon_type=choice)
                return
            else: 
                print("Invalid Input: Please Try Again")

        elif character == "WAF":
            print("""
            ------------------------------------------------------
                            Pick Your Weapon
            ------------------------------------------------------
                            Damage:      30 
                Sword       Hit Chance:  90   Type Sword To Pick
                            Crit Chance: 10
            ------------------------------------------------------
                            Damage:      50
                Axe         Hit Chance:  70   Type Axe To Pick
                            Crit Chance: 30     
            ------------------------------------------------------
                            Damage:      35
                Spatula     Hit Chance:  85   Type Spatula To Pick
                            Crit Chance  10
            ------------------------------------------------------
    """)
            weapon_list = ["Sword","Axe","Spatula"]
            response = input(str())
            if response in weapon_list:
                choice: str = str(response)
                selected_weapon = Weapon(weapon_type=choice)
                return 
            else: 
                print("Invalid Input: Please Try Again")
        elif character == "TO":
            print("""
            ------------------------------------------------------
                            Pick Your Weapon
            ------------------------------------------------------
                            Damage:      30 
                Sword       Hit Chance:  90   Type Sword To Pick
                            Crit Chance: 10
            ------------------------------------------------------
                            Damage:      35
                Spatula     Hit Chance:  85   Type Spatula To Pick
                            Crit Chance: 10     
            ------------------------------------------------------
                            Damage:      10
                Blankie     Hit Chance:  100  Type Blankie To Pick
                            Crit Chance  10
            ------------------------------------------------------

    """)
            weapon_list = ["Sword","Spatula","Blankie"]
            response = input(str())
            if response in weapon_list:
                choice: str = str(response)
                selected_weapon = Weapon(weapon_type=choice)
                return 
            else: 
                print("Invalid Input: Please Try Again")
        elif character == "RO":
            print("""
            ------------------------------------------------------
                            Pick Your Weapon
            ------------------------------------------------------
                            Damage:      30 
                Sword       Hit Chance:  90   Type Sword To Pick
                            Crit Chance: 10
            ------------------------------------------------------
                            Damage:      40
                Spear       Hit Chance:  80   Type Spear To Pick
                            Crit Chance: 20     
            ------------------------------------------------------
                            Damage:      50
                Axe         Hit Chance:  70   Type Axe To Pick
                            Crit Chance  30
            ------------------------------------------------------
    """)
            weapon_list = ["Sword","Spear","Axe"]
            response = input(str())
            if response in weapon_list:
                choice: str = str(response)
                selected_weapon = Weapon(weapon_type=choice)
                return 
            
            else: 
                print("Invalid Input: Please Try Again")
        










if __name__ == '__main__':
    while True:
        game = MainGame()
        