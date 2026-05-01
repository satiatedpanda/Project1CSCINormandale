from typing import NoReturn
from random import choice, randint

"""
    doc comment for things
"""

class Status:
    def __init__(self, name: str, stype: bool,*, duration: int=3, chance_to_remove: int=20):
        self.status_name = name
        self.isgood = stype
        self.duration = duration
        self.chance = chance_to_remove

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"Status Type: {self.status_name}, isGood: {self.isgood}, Duration: {self.duration}, Chance To Remove: {self.chance}"

class Weapon: 
    def __init__(self): 
        self.weapon_type = ""
        self.dmg = 0
        self.accuracy = 0 
        self.crit_chance = 0
        
    def assign(self, weapon_type: str) -> None:
        """assigns correct weapon values to weapon object

        Args:
            weapon_type (str): Weapon chosen
        """
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
    def __init__(self, *, title="", health=0, defense=0, magic_proficiency=0, speed=0):
        self.title = title
        self.max_health = health
        self.health = health
        self.defense = defense #reduces damage taken
        self.speed = speed
        self.magic_proficiency = magic_proficiency #adds to chance of magic working
        self.status: list[Status] = []

    def apply_status_effects(self):
        if len(self.status) > 0:
            for value in self.status:
                match value.status_name:
                    case "Poison":
                        self.health -= int(self.max_health * 0.05)
                    case "Paralysis":
                        self.paralyzed = True #cant use weapons
                    case "Protect":
                        self.defense += 25
                    case "Burn":
                        self.health -= 10
                    case "Stop":
                        self.stopped = True #cant attack at all
                    case "Mute":
                        self.muted = True #cant use magic
                    case "Fast":
                        self.speed += 30
                    case _: #catchall
                        print("error, invalid status name")
                value.duration -= 1

    def remove_status_effects(self):
        if len(self.status)>0:
            for value in self.status[:]:
                if value.duration == 0:
                    self.status.remove(value)
                    print(f"{value.status_name} Expired")
                else:
                    remove_val = randint(0,100)
                    if remove_val <= value.chance:
                        self.status.remove(value)
                        print(f"{value.status_name} Expired randomly")

    def get_attributes(self) -> dict[str, object]:
        #found at: https://stackoverflow.com/questions/9058305/getting-attributes-of-a-class
        for attribute, value in self.__dict__.items():
            print(attribute + "=" + value)
        return self.__dict__

class Player(Person):
    def __init__(self, title: str, weapon: Weapon):
        super().__init__(title=title)
        self.weapon: Weapon = weapon

class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.weapon = Weapon()
        self.magic = {}
        self.ai_type = ""
        self.monster_type = ""

    def randomEnemy(self):
        enemy_list = ["Orc", "Wrym", "Hobgoblin", "Troll", "Wolf", "Ogre", "Werewolf", "Shark", "Ghost", "Lich", "Death Eye", "Hydra", "Elemental"]
        rand_enemy = choice(enemy_list)
        match rand_enemy:
            case "Orc":
                self.title = "Orc"
                self.monster_type = "Basic"                
                self.health = 150
                self.weapon = Weapon.assign("Sword")
                self.ai_type = "Agressive Weapon"
            case "Wrym":
                self.title = "Wrym"
                self.monster_type = "Flying"                    
                self.health = 450
                self.weapon.weapon_type = "Claws"
                self.weapon.dmg = 60                
                self.weapon.crit_chance = 12
                self.weapon.accuracy = 95
                self.ai_type = "Cautious Mixed"
            case "Hobgoblin":
                self.title = "Hobgoblin"
                self.monster_type = "Basic"                    
                self.health = 100
                self.weapon = Weapon.assign("Spear")
                self.ai_type = "Agressive Mixed"
            case "Troll":
                self.title = "Troll"
                self.monster_type = "Basic"                    
                self.health = 300
                self.weapon.weapon_type = "Club"
                self.weapon.dmg = 80                
                self.weapon.crit_chance = 25
                self.weapon.accuracy = 70
                self.ai_type = "Cautious Weapon"
            case "Wolf":
                self.title = "Wolf"
                self.monster_type = "Basic"                    
                self.health = 200
                self.weapon.weapon_type = "Claws"
                self.weapon.dmg = 40                
                self.weapon.crit_chance = 30
                self.weapon.accuracy = 95
                self.ai_type = "Agressive Mixed"
            case "Ogre":
                self.title = "Ogre"
                self.monster_type = "Basic"                    
                self.health = 500
                self.weapon = Weapon.assign("Fists")
                self.ai_type = "Agressive Weapon"
            case "Werewolf":
                self.title = "Werewolf"
                self.monster_type = "Basic"                    
                self.health = 200     
                self.weapon.weapon_type = "Claws"
                self.weapon.dmg = 50                
                self.weapon.crit_chance = 25
                self.weapon.accuracy = 85
                self.ai_type = "Agressive Mixed"
            case "Shark":
                self.title = "Shark"
                self.monster_type = "Sea"                    
                self.health = 300
                self.weapon.weapon_type = "Fins"
                self.weapon.dmg = 40                
                self.weapon.crit_chance = 60
                self.weapon.accuracy = 35                
                self.ai_type = "Agressive Magic"
            case "Ghost":
                self.title = "Ghost"
                self.monster_type = "Intangible"                    
                self.health = 100
                self.weapon.weapon_type = "Haunting"
                self.weapon.dmg = 50                
                self.weapon.crit_chance = 30
                self.weapon.accuracy = 50      
                self.ai_type = "Cautious Magic"
            case "Lich":
                self.title = "Lich"
                self.monster_type = "Intangible"                
                self.health = 250
                self.weapon.weapon_type = "Staff"
                self.weapon.dmg = 90                
                self.weapon.crit_chance = 40
                self.weapon.accuracy = 70    
                self.ai_type = "Agressive Magic"
            case "Death Eye":
                self.title = "Death Eye"
                self.monster_type = "Intangible"                
                self.health = 100
                self.weapon.weapon_type = "Haunting"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80     
                self.ai_type = "Cautious Magic"
            case "Hydra":
                self.title = "Hydra"
                self.monster_type = "Flying"                
                self.health = 100
                self.weapon.weapon_type = "Stomp"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80   
                self.ai_type = "Agressive Mixed"
            case "Elemental":
                self.title = "Elemental"
                self.monster_type = "Flying"                
                self.health = 100
                self.weapon.weapon_type = "Spirit Swipe"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80   
                self.ai_type = "Cautious Mixed"

    def ai_action(self):
        pass

class Magic:       
    """Class of functions for all magic spells
    """
    #defensive
    def Cure(self, person: Person) -> bool:
        #removes bad status effects
        success_val = randint(0,100)
        if success_val <= (person.magic_proficiency + 50):
            positive_effects: list[Status] = []  
            for i in range(len(person.status)):
                if person.status[i].isgood == True:
                    positive_effects.append(person.status[i])
            person.status.clear()
            if len(positive_effects) > 0:
                person.status.extend(positive_effects)
            print(f"{person.title} Cured all negative effects!")
            return True
        else:
            print(f"{person.title}'s Cure Failed")
            return False

    def Heal(self, person: Person) -> bool:
        #heals user by 20% of max health. 100% chance of success
        cur_health = person.health
        person.health += int(person.max_health * 0.2)
        if person.health > person.max_health:
            person.health = person.max_health
        delta_health = person.health - cur_health
        print(f"{person.title} gained {delta_health} health!")
        return True

    def Protect(self, person: Person) -> bool:
        #raises defense
        success_val = randint(0,100)
        if success_val <= (person.magic_proficiency + 80):
            person.defense += 20
            print(f"{person.title}'s defense rose by 20!")
            return True
        else:
            print(f"{person.title}'s Protect failed")
            return False

    #offensive
    def Fireball(self, person: Person, opponent: Person) -> bool:
        #fireball. small chance to inflict burn
        success_val = randint(0,100)
        if success_val <= (person.magic_proficiency + 65):
            opponent.health -= randint(40,60) - opponent.defense
            success_val = randint(0,100)
            if success_val <= (30 - opponent.magic_proficiency):
                opponent.status.append(Status("Burn",False))
            

    def Lightning(self, person: Person) -> bool:
        #lightning. chance to inflict paralysis
        pass

    def Nuke(self, person: Person) -> bool:
        #high damage, hits caster aswell. Low number of uses
        pass

    #offensive status effects
    def Poison(self, person: Person) -> bool:
        #posion. high chance to inflict poison
        pass

    def Instant_Death(self, person: Person) -> bool:
        #chance to make an opponent die instantly. very low chance
        pass

    def Stop(self, person: Person) -> bool:
        #chance to make opponent lose a turn
        pass

    def Fast(self, person: Person) -> bool:
        #increases speed
        pass

    def Slow(self, person: Person) -> bool:
        #lowers opponent's speed
        pass

    def Mute(self, person: Person) -> bool:
        #chance to make opponent not able to cast spells
        pass

    def Break(self, person: Person) -> bool:
        #chance to break items in player inventory - enemy specific
        pass




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
        player = Player(self.character, self.weapon)
        enemy = Enemy()
    
    def game(self) -> None:
        #main game loop
        while True:
            pass
            #print user options
            #get user selection
            #edit avaliable options for next round based upon selection
            #get turn order
            #1st attack
            #effects -> check for winner
            #2nd attack
            #effects -> check for winner
        
        
        self.ending()

    def ending(self):
        self.exit_game(noexit=True)


    def exit_game(self, noexit=False) -> NoReturn: #DO NOT USE RANDOM EXIT STATEMENTS, call to this function whenever you exit. 
        if noexit == False:
            exit()
        print("restarting game...\n")










if __name__ == '__main__':
    while True:
        game = MainGame()
        