from typing import NoReturn
from random import randint

"""
    doc comment for things
"""



class StatModifiers:
    """Updates and returns stat modifiers based on input
    """
    def __init__(self) -> None:
        pass

class Abilities:
    """Class of all abilites in the game - in form
    """
    def __init__(self) -> None:
        pass

    def assign_magic(self):
        pass

    def assign_items(self):
        pass

class Items:
    def __init__(self):
        pass

class Magic:
    def __init__(self):
        pass



class Weapon: 
    def __init__(self): 
        self.weapon_type = ""
        self.dmg = 0
        self.accuracy = 0 
        self.crit_chance = 0
        
    def assign(self, weapon_type):
        match weapon_type:
            case "Sword":
                self.weapon_type = "Sword"
                self.dmg = 30    
                self.accuracy = 90
                self.crit_chance = 10
        
            case "Spear":
                self.weapon_type = "Spear"
                self.dmg = 40    
                self.accuracy = 80
                self.crit_chance = 20
        

            case "Axe":
                self.weapon_type = "Axe"
                self.dmg = 50    
                self.accuracy = 80
                self.crit_chance = 30
        

            case "Tome":
                self.weapon_type = "Tome"
                self.dmg = 30    
                self.accuracy = 50
                self.crit_chance = 50
        

            case "Spatula":
                self.weapon_type = "Spatula"
                self.dmg = 35   
                self.accuracy = 85
                self.crit_chance = 10
        
            case "Blankie":
                self.weapon_type = "Blankie"
                self.dmg = 10    
                self.accuracy = 100
                self.crit_chance = 1

            case _: 
                self.weapon_type = "Fists"
                self.dmg = 20    
                self.accuracy = 100
                self.crit_chance = 20
    
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"Weapon Type: {self.weapon_type}, Dmg: {self.dmg}, Accuracy: {self.accuracy}, Crit Chance: {self.crit_chance}"

class Person:
    def __init__(self, *, title="", health=0, abilities = Abilities()):
        self.health = health
        self.title = title

    def assign_items(self):
        if self.title != "":
            return "error"
        
    def assign_magic(self):
        pass

    def apply_status_effects(self):
        pass

class Player(Person):
    def __init__(self, title: str, health: int,*, weapon = Weapon(), abilities = Abilities()):
        super().__init__(title=title, health=health)
        self.weapon: Weapon = weapon

class Enemy(Person):
    def __init__(self):
        super().__init__()

        self.title
        self.health
        self.weapon
        self.magic


class MainGame:
    """Main game object
    """
    def __init__(self) -> None:
        self.character = ""
        self.weapon = Weapon()
        self.menu_screen()
        self.exit_game(noexit=True)

    def menu_screen(self) -> None:
        """
            This function prints the main menu screen as well as handles all validations required from the user.
        """
        # menu_text: str = "play, exit"
        # print(menu_text)
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
            menu_cs_text: str = "available warriors: Wizard, Waffle House Employee, Toddler, Rogue"
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
                        self.exit_game()
                elif "WIZ" or "WAF" or "TO" or "RO" in menuinput: #continues with char select
                    character_list = ["WIZARD", "WAFFLE HOUSE EMPLOYEE", "TODDLER", "ROUGE"]
                    #https://stackoverflow.com/questions/2170900/get-first-list-index-containing-sub-string
                    #we can restrict menuinput to only be the first two characters because inputcheck above only checks the first two characters (kinda)
                    character: str = character_list[[idx for idx, string in enumerate(character_list) if menuinput[0:2] in string][0]].title() 
                    confirm_y = input(f"Is {character} the Fighter you want? Enter Y/N\n-> ").upper() #or confirm
                    if "Y" in confirm_y[0:5]:
                        self.character = character
                        self.weapon_select_menu()
                        break
                    #else:
                        #kick back to prev option
                else: #this is for wrong inputs not caught
                    print("You weren't supposed to see this.\n")
                    raise KeyError
            except ValueError:
                print("Select a valid option.\n")
            return None

    def weapon_select_menu(self) -> None: 
        character = self.character.upper()
        weapon_list = []
        print_statement = ""
        match character:
            case "WIZARD":
                print_statement = """
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
                """
                weapon_list = ["Sword","Spear","Tome"]
            case "WAFFLE HOUSE EMPLOYEE":
                print_statement = """
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
                """
                weapon_list = ["Sword","Axe","Spatula"]
            case "TODDLER":
                print_statement = """
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

                """
                weapon_list = ["Sword","Spatula","Blankie"]
            case "ROUGE":
                print_statement = """
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
                """
                weapon_list = ["Sword","Spear","Axe"]
        print(print_statement)
        imput_check = [value[0:2].upper() for value in weapon_list]
        while True:
            try:
                response = input("\n-> ").upper()
                any((substring in response for substring in imput_check))
                if any((substring in response for substring in imput_check)): #checks if response
                    choice = weapon_list[[idx for idx, string in enumerate(weapon_list) if response[0:2].title() in string][0]]
                    self.weapon.assign(choice)
                    self.start_game()
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input: Please Try Again")                
        

    def start_game(self) -> None:
        #initialize everything with enemy and player here, with defined values
        pass
    
    def game(self) -> None:
        #main game loop
        pass


    def exit_game(self, noexit=False) -> NoReturn: #DO NOT USE RANDOM EXIT STATEMENTS, call to this function whenever you exit. 
        if noexit == False:
            exit()
        print("restarting game...\n")










if __name__ == '__main__':
    while True:
        game = MainGame()
        