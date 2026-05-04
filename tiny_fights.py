from typing import NoReturn
from random import choice, randint
from time import sleep

"""
    Program for running a small 1v1 fight between a player and a random enemy
"""

class Status:
    """Status effects
    """
    def __init__(self, name: str, isgood: bool,*, duration: int=3, chance_to_remove: int=20):
        """Status Class, all status effects are of this class

        Args:
            name (str): name of status effect
            isgood (bool): True/False value if the status is good or not
            duration (int, optional): Duration of status. Defaults to 3 turns.
            chance_to_remove (int, optional): Chance of status ending randomly, chance out of 100. Defaults to 20.
        """
        self.status_name = name
        self.isgood = isgood
        self.duration = duration
        self.chance = chance_to_remove

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"Status Type: {self.status_name}, isGood: {self.isgood}, Duration: {self.duration}, Chance To Remove: {self.chance}"

class Weapon:
    """Weapon Class
    """
    def __init__(self): 
        """Weapon Class, has attributes of weapon_type, dmg, accuracy, and crit_chance
        """
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
            case "Staff":
                self.weapon_type = "Staff"
                self.dmg = 10    
                self.accuracy = 90
                self.crit_chance = 40                
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
    """Person class
    """
    def __init__(self, *, title: str="", health: int=0, defense: int=0, magic_proficiency: int=0, speed: int=0, weapon: Weapon= Weapon(), magic: dict[str,int]={}, items: dict[str,int] = {}):
        """Initilizes all person attributes, and default values

        Args:
            title (str, optional): Title of Person. Defaults to "".
            health (int, optional): Health value. Defaults to 0.
            defense (int, optional): Defense value, reduces damage taken. Defaults to 0.
            magic_proficiency (int, optional): Magic Proficiency value, increases magic success chance. Defaults to 0.
            speed (int, optional): Speed Value, determines turn order. Defaults to 0.
            weapon (Weapon, optional): Weapon object. Defaults to Weapon().
            magic (dict[str,int], optional): Magic dictionary. Defaults to empty dictionary.
            items (dict[str,int], optional): Item dictionary. Defaults to empty dictionary.
        """
        #main attributes
        self.title: str = title
        self.weapon: Weapon = weapon     
        self.health: int = health
        self.defense: int = defense
        self.speed: int = speed
        self.magic_proficiency: int = magic_proficiency
        self.items: dict[str,int] = items
        self.magic: dict[str,int] = magic

        #status effects attributes
        self.status: list[Status] = []
        self.stopped: bool = False
        self.muted: bool = False
        self.paralyzed: bool = False

        #These regular values can change by effects in the game, so these are used to remember what the original values were
        self.default_speed: int = speed     
        self.default_defense: int = defense           
        self.max_health: int = health 
        self.base_dmg: int = 0      

        #edge case if a weapon was not assigned correctly
        if not(hasattr(self.weapon, "weapon_type")):
            self.weapon.assign("Fists")          

    def apply_status_effects(self) -> None:
        """Applies status effects that are currently afflicting the Person, and lowers the duration by 1 for each status effect
        """
        self.defense = self.default_defense
        self.speed = self.default_speed
        self.base_dmg = 0
        self.paralyzed = False
        self.muted = False
        self.stopped = False        
        if len(self.status) > 0:
            for value in self.status:
                match value.status_name:
                    case "Poison":
                        self.health -= int(self.max_health * 0.05)
                        print(f"{self.title} is poisoned and lost {int(self.max_health*0.05)} health")
                    case "Protect":
                        self.defense += 25
                        print(f"{self.title} is protected and gained 25 defense! They now have {self.defense} defense")
                    case "Burn":
                        self.health -= 10
                        print(f"{self.title} is burning and lost 10 HP! They now have {self.health}HP!")                        
                    case "Fast":
                        self.speed += 30       
                        print(f"{self.title} has been sped up! Their speed is currently: {self.speed}!")                                        
                    case "Slow":
                        self.speed = max(self.speed-30,0)  
                        print(f"{self.title} is slowed! Their speed is currently: {self.speed}!")                           
                    case "Stop":
                        self.stopped = True #cant attack at all
                        print(f"{self.title} is stopped! {value.duration} turn(s) remain til this expires")
                    case "Paralysis":
                        self.paralyzed = True #cant use weapons         
                        print(f"{self.title} is paralyized! {value.duration} turn(s) remain til this expires")                                       
                    case "Mute":
                        self.muted = True #cant use magic
                        print(f"{self.title} is muted! {value.duration} turn(s) remain til this expires")
                    case "Constrict":
                        self.defense = max(self.defense-30,0)  
                        print(f"{self.title} is constricted! Their defense is currently: {self.defense}!")                          
                    case "Strength":
                        self.base_dmg += 30  
                        print(f"{self.title} is strengthened! Their bonus damage is currently: {self.base_dmg}!")        
                    case "Weakness":
                        self.base_dmg -= 30  
                        print(f"{self.title} has been weakened! Their bonus damage is currently: {self.base_dmg}!")                                    
                    case _: #catchall
                        print("error, invalid status name")
                        print(value.status_name)
                        exit_game()
                sleep_func(1)

    def update_base_setting(self, setting):
        self.defense = self.default_defense
        self.speed = self.default_speed
        self.base_dmg = 0
        self.paralyzed = False
        self.muted = False
        self.stopped = False 

    def remove_status_effects(self) -> None: #ran right after user picks an option, before apply affects
        """Resets altered stats to base values, and removes status effects that expired
        """

        if len(self.status)>0:
            for value in self.status[:]: #compares against a copy of the list to not throw errors
                remove_val = randint(0,100)                 
                if value.duration <= 0:
                    self.status.remove(value)
                    # self.update_base_setting(value.status_name)
                    print(f"{self.title}'s <{value.status_name}> Expired")
                elif remove_val <= value.chance:
                    self.status.remove(value)
                    # self.update_base_setting(value.status_name)                    
                    print(f"{self.title}'s <{value.status_name}> Expired randomly")
                else:
                    print(f"{self.title} has <{value.status_name}> for {value.duration} more turn(s)")
                    value.duration -= 1
            sleep_func(1)
            print()
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"-{self.title}-\nHealth Points: {self.health}/{self.max_health}\nDefense: {self.defense}\nSpeed: {self.speed}\nMagic Proficiency: {self.magic_proficiency}\nWeapon: {self.weapon.weapon_type}"

class Player(Person):
    """Player Class, subclass of Person
    """
    def __init__(self, title: str, weapon: Weapon):
        """initilizes attributes for player

        Args:
            title (str): title of player
            weapon (Weapon): weapon chosen for player
        """
        self.assign_attributes(title)
        super().__init__(title=title, weapon=weapon, health=self.health, defense=self.defense, magic_proficiency=self.magic_proficiency, speed=self.speed, magic=self.magic, items=self.items)
    
    def assign_attributes(self, title: str) -> None:       
        """Assigns attributes based on the character selected

        Args:
            title (str): Title of Person.
        """        
        match title:
            case "Wizard":
                self.health = 250
                self.defense = 15
                self.speed = 30
                self.magic_proficiency = 30
                self.magic = {"Heal": 5, "Slow": 3, "Poison": 3, "Fireball": 4, "Lightning": 4, "Nuke": 2, "Instant_Death": 2, "Scar": 3} 
                self.items = {"Small_Healing_Potion": 2, "Antidote": 2, "Strength": 3}
            case "Waffle House Employee":
                self.health = 300
                self.defense = 10 
                self.speed = 40   
                self.magic_proficiency = 0               
                self.magic = {"Cure": 3, "Heal": 3, "Protect": 2, "Fast": 5, "Stop": 2, "Mute": 2, "Poison": 5, "Scar": 3} 
                self.items = {"Small_Healing_Potion": 3, "Mega_Healing_Potion": 1, "Grenade": 4, "Weakness": 3}
            case "Toddler":
                self.health = 175
                self.defense = 0
                self.speed = 100   
                self.magic_proficiency = 20                
                self.magic = {"Protect": 5, "Stop": 2, "Slow": 3, "Mute": 3, "Poison": 2, "Nuke": 3, "Instant_Death": 5, "Scar": 5, "Constrict": 2}
                self.items = {"Small_Healing_Potion": 5, "Grenade": 4, "Stick": 15, "Weakness": 10}
            case "Rouge":
                self.health = 200
                self.defense = 10 
                self.speed = 70   
                self.magic_proficiency = 0                
                self.magic = {"Cure": 2, "Heal": 3, "Protect": 3, "Slow": 3, "Fireball": 2, "Lightning": 2, "Constrict": 3}
                self.items = {"Mega_Healing_Potion": 3, "Grenade": 4, "Strength": 2}
            case _:
                print("Error, incorrect title")
                print(self.title)
                exit_game()

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()

class Enemy(Person):
    """Enemy Class, subclass of Person
    """
    def __init__(self, *, chosen_enemy: str=""):
        """initilizes and selects a random enemy, or the enemy inputed

        Args:
            chosen_enemy (str, optional): chosen enemy. Must be in the enemy list. Defaults to "".
        """
        self.weapon = Weapon()
        self.ai_type = []
        self.monster_type = ""  
        if chosen_enemy != "":
            self.randomEnemy(chosen_enemy=chosen_enemy)      
        self.randomEnemy() #give this
        super().__init__(title=self.title, weapon=self.weapon, health=self.health, defense=self.defense, magic_proficiency=self.magic_proficiency, speed=self.speed, magic=self.magic, items=self.items)


    def randomEnemy(self, *, chosen_enemy: str="") -> None:
        """Selects random enemy and assigns their attributes, selects chosen_enemy if argument is provided

        Args:
            chosen_enemy (str, optional): user selected enemy. Useful for debugging. Defaults to "".
        """
        enemy_list = ["Orc", "Wrym", "Hobgoblin", "Troll", "Wolf", "Ogre", "Werewolf", "Shark", "Ghost", "Lich", "Death Eye", "Hydra", "Elemental"]
        if chosen_enemy != "":
            if chosen_enemy not in enemy_list:
                print("Incorrect enemy chosen, please refer to the code for all avaliable options")
                exit_game()
            else:
                rand_enemy = chosen_enemy
        else:
            rand_enemy = choice(enemy_list)
        match rand_enemy:
            case "Orc":
                self.title = "Orc"
                self.monster_type = "Basic"                
                self.health = 150
                self.speed = 20
                self.magic_proficiency = 0
                self.defense = 0
                self.magic = {"Constrict": 10}
                self.items = {"Small_Healing_Potion": 5, "Mega_Healing_Potion": 1, "Stick": 5}
                self.weapon.assign("Sword")
                self.ai_type = ["Agressive", "Weapon"]
            case "Wrym":
                self.title = "Wrym"
                self.monster_type = "Flying"                    
                self.health = 450
                self.defense = 20
                self.speed = 60
                self.magic_proficiency = 20
                self.magic = {"Fireball": 30, "Lightning": 30, "Nuke": 3, "Stop": 2, "Slow": 2, "Mute": 2, "Break": 2, "Scar": 4}
                self.items = {"Small_Healing_Potion": 2, "Antidote": 2, "Strength": 2, "Weakness": 10}          
                self.weapon.weapon_type = "Claws"
                self.weapon.dmg = 60                
                self.weapon.crit_chance = 12
                self.weapon.accuracy = 95
                self.ai_type = ["Cautious", "Mixed"]
            case "Hobgoblin":
                self.title = "Hobgoblin"
                self.monster_type = "Basic"                    
                self.health = 100
                self.defense = 5
                self.speed = 20
                self.magic_proficiency = 5
                self.magic = {"Heal": 10, "Protect": 5, "Fast": 5, "Fireball": 5, "Lightning": 5, "Nuke": 10, "Poison": 5, "Scar": 5}
                self.items = {"Small_Healing_Potion": 4, "Mega_Healing_Potion": 1, "Grenade": 10} 
                self.weapon.assign("Spear")
                self.ai_type = ["Agressive", "Mixed"]
            case "Troll":
                self.title = "Troll"
                self.monster_type = "Basic"                    
                self.health = 300
                self.defense = 40
                self.speed = 0
                self.magic_proficiency = 0
                self.magic = {"Constrict": 10}
                self.items = {"Stick": 100, "Strength": 2}
                self.weapon.weapon_type = "Club"
                self.weapon.dmg = 80                
                self.weapon.crit_chance = 25
                self.weapon.accuracy = 70
                self.ai_type = ["Cautious", "Weapon"]
            case "Wolf":
                self.title = "Wolf"
                self.monster_type = "Basic"                    
                self.health = 200
                self.defense = 5
                self.speed = 70
                self.magic_proficiency = 5
                self.magic = {"Protect": 5, "Slow": 10, "Lightning": 10, "Break": 1, "Scar": 1}
                self.items = {"Small_Healing_Potion": 5, "Antidote": 4, "Stick": 5}        
                self.weapon.weapon_type = "Claws"
                self.weapon.dmg = 40                
                self.weapon.crit_chance = 30
                self.weapon.accuracy = 95
                self.ai_type = ["Agressive", "Mixed"]
            case "Ogre":
                self.title = "Ogre"
                self.monster_type = "Basic"                    
                self.health = 500
                self.defense = 0
                self.speed = 5
                self.magic_proficiency = 3
                self.magic = {"Constrict": 10, "Heal": 10, "Scar": 3}   
                self.items = {}   
                self.weapon.assign("Fists")
                self.weapon.dmg = 50
                self.ai_type = ["Agressive", "Weapon"]
            case "Werewolf":
                self.title = "Werewolf"
                self.monster_type = "Basic"                    
                self.health = 200     
                self.defense = 10
                self.speed = 30
                self.magic_proficiency = 10
                self.magic = {"Cure": 10, "Heal": 10, "Protect": 2, "Fast": 2, "Lightning": 10, "Slow": 1, "Mute": 1, "Scar": 1}
                self.items = {"Small_Healing_Potion": 10, "Mega_Healing_Potion": 1, "Antidote": 5, "Stick": 4, "Weakness": 2}
                self.weapon.weapon_type = "Claws"
                self.weapon.dmg = 50                
                self.weapon.crit_chance = 25
                self.weapon.accuracy = 85
                self.ai_type = ["Agressive", "Mixed"]
            case "Shark":
                self.title = "Shark"
                self.monster_type = "Sea"                    
                self.health = 300
                self.speed = 60
                self.defense = 0
                self.magic_proficiency = 0
                self.magic = {"Mute": 3, "Break": 2, "Protect": 3}
                self.items = {"Antidote": 2, "Strength": 3}   
                self.weapon.weapon_type = "Fins"
                self.weapon.dmg = 40                
                self.weapon.crit_chance = 60
                self.weapon.accuracy = 35                
                self.ai_type = ["Agressive", "Magic"]
            case "Ghost":
                self.title = "Ghost"
                self.monster_type = "Intangible"                    
                self.health = 100
                self.defense = 0
                self.speed = 20
                self.magic_proficiency = 3
                self.magic = {"Heal": 6, "Fireball": 10, "Stop": 2, "Slow": 2, "Mute": 2}     
                self.items = {"Strength": 2, "Weakness": 2}    
                self.weapon.weapon_type = "Haunting"
                self.weapon.dmg = 50                
                self.weapon.crit_chance = 30
                self.weapon.accuracy = 50      
                self.ai_type = ["Cautious", "Magic"]
            case "Lich":
                self.title = "Lich"
                self.monster_type = "Intangible"                
                self.health = 250
                self.defense = 20
                self.speed = 20
                self.magic_proficiency = 10
                self.magic = {"Cure": 2, "Heal": 5, "Protect": 10, "Fast": 0, "Instant_Death": 1, "Stop": 2, "Slow": 1, "Mute": 5, "Break": 1}
                self.items = {"Small_Healing_Potion": 10, "Strength": 3, "Weakness": 3}
                self.weapon.weapon_type = "Staff"
                self.weapon.dmg = 90                
                self.weapon.crit_chance = 40
                self.weapon.accuracy = 70    
                self.ai_type = ["Agressive", "Magic"]
            case "Death Eye":
                self.title = "Death Eye"
                self.monster_type = "Intangible"                
                self.health = 100
                self.defense = 0
                self.speed = 100
                self.magic_proficiency = 10
                self.magic = {"Instant_Death": 100}
                self.items = {"Small_Healing_Potion": 10}
                self.weapon.weapon_type = "Haunting"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80     
                self.ai_type = ["Cautious", "Magic"]
            case "Hydra":
                self.title = "Hydra"
                self.monster_type = "Flying"                
                self.health = 400
                self.defense = 10
                self.speed = 50
                self.magic_proficiency = 3
                self.magic = {"Fireball": 10, "Lightning": 10, "Nuke": 3}     
                self.items = {"Mega_Healing_Potion": 2, "Weakness": 10}      
                self.weapon.weapon_type = "Stomp"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80   
                self.ai_type = ["Agressive", "Mixed"]
            case "Elemental":
                self.title = "Elemental"
                self.monster_type = "Flying"                
                self.health = 100
                self.defense = 5
                self.speed = 25
                self.magic_proficiency = 30
                self.magic = {"Fireball": 100, "Lightning": 100, "Poison": 100}
                self.items = {"Antidote": 3, "Small_Healing_Potion": 5, "Strength": 2, "Weakness": 3}             
                self.weapon.weapon_type = "Spirit Swipe"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80   
                self.ai_type = ["Cautious", "Mixed"]

    def ai_action(self) -> str:
        """Selects an action for the enemy, weighted by ai_type

        Returns:
            str: ai action, in form "main_action sub_action"
        """
        attack = False
        action_choice = ""
        has_negative_status = False
        heal = False
        heal_options = []
        if "Heal" in list(self.magic.keys()):
            heal_options.append("Magic Heal")
        if "Mega_Healing_Potion" in list(self.items.keys()):
            heal_options.append("Item Mega_Healing_Potion")
        if "Small_Healing_Potion" in list(self.items.keys()):
            heal_options.append("Item Small_Healing_Potion")        

        for i in range(len(self.status)):
            if self.status[i].isgood == False:
                has_negative_status = True
                break
        if self.stopped == True:
            action_choice = "Continue"
            return action_choice
        elif self.ai_type[0] == "Agressive":
            if self.health >= int(0.6 * self.max_health):
                attack = True
            elif self.health <= int(0.1 * self.max_health):
                attack = False
                heal = True
            elif (self.health <= int(0.25 * self.max_health)) and has_negative_status:
                attack = False
                cure_options = []
                if "Antidote" in list(self.items.keys()):
                    cure_options.append("Item Antidote")
                if ("Cure" in list(self.magic.keys())) and (self.muted == False):
                    cure_options.append("Magic Cure")
                cure_options_len = len(cure_options)
                if cure_options_len>0:
                    rand_val = randint(0,100)
                    if cure_options_len == 1:
                        action_choice = cure_options[0]
                    #if len = 2, magic will always be in it
                    elif self.ai_type[1] == "Magic" and rand_val > 20:
                        action_choice = "Magic Cure"
                    elif self.ai_type[1] == "Magic" and rand_val > 20:
                        action_choice = "Magic Cure"
                    elif self.ai_type[1] == "Magic" and rand_val > 20:
                        action_choice = "Magic Cure"
                    else:
                        action_choice = "Item Antidote"
                    return action_choice                                          
            else:
                attack_val = randint(0,100)
                if 80 > attack_val:
                    attack = True            
        elif self.ai_type[0] == "Cautious": #more focused on item usage
            if self.health >= int(0.8 * self.max_health):
                attack = True
            elif self.health <= int(0.3 * self.max_health):
                attack = False
                heal = True
            elif (self.health <= int(0.5 * self.max_health)) and has_negative_status:
                attack = False                
                cure_options = []
                if "Antidote" in list(self.items.keys()):
                    cure_options.append("Item Antidote")
                if ("Cure" in list(self.magic.keys())) and (self.muted == False):
                    cure_options.append("Magic Cure")
                cure_options_len = len(cure_options)
                if cure_options_len>0:
                    rand_val = randint(0,100)
                    if cure_options_len == 1:
                        action_choice = cure_options[0]
                    #if len = 2, magic will always be in it
                    elif self.ai_type[1] == "Magic" and rand_val > 20:
                        action_choice = "Magic Cure"
                    elif self.ai_type[1] == "Magic" and rand_val > 20:
                        action_choice = "Magic Cure"
                    elif self.ai_type[1] == "Magic" and rand_val > 20:
                        action_choice = "Magic Cure"     
                    else:
                        action_choice = "Item Antidote"
                    return action_choice                            
            else:
                attack_val = randint(0,100)
                if 50 > attack_val:
                    attack = True
        else:
            print("should not happen. ai_type needs to be Cautious or Agressive")
            exit_game()                   

        #attack should be set now
        if (self.muted == True) and (self.paralyzed == True): #can only use items
            if len(self.items.items()) == 0:
                action_choice = "Continue"
                return action_choice
            attack_items = []
            items_list = list(self.items.keys())
            if "Grenade" in items_list:
                attack_items.append("Item Grenade")
            if "Stick" in items_list:
                attack_items.append("Item Stick")
            if "Strength" in items_list:
                attack_items.append("Item Strength")         
            if "Weakness" in items_list:
                attack_items.append("Item Weakness")                         
            if "Magic Heal" in heal_options:
                heal_options.remove("Magic Heal")
            if heal == True and len(heal_options)>0:
                action_choice = choice(heal_options)
            elif attack == True and len(attack_items)>0:
                action_choice = choice(attack_items)
            else:
                action_choice = "Item " + choice(items_list)
        elif attack == True:
            rand_val = randint(0,100)
            magic_list = list(self.magic.keys())
            items_list = list(self.items.keys())
            item_attack_options = []
            if "Heal" in magic_list:
                magic_list.remove("Heal")
            if "Cure" in magic_list:
                magic_list.remove("Cure")
            if "Grenade" in items_list:
                items_list.remove("Grenade")
                item_attack_options.append("Item Grenade")
            if "Stick" in items_list:
                items_list.remove("Stick")
                item_attack_options.append("Item Stick")
            if "Strength" in items_list:
                items_list.remove("Strength")
                item_attack_options.append("Item Strength")            
            if "Weakness" in items_list:
                items_list.remove("Weakness")
                item_attack_options.append("Item Weakness")                      

            #first selection condition
            if self.muted == True: #use weapon or item (if got here, cannot be paralyzed)
                if len(item_attack_options) == 0:
                    action_choice = "Weapon"
                elif self.ai_type[0] == "Agressive":
                    rand_val = randint(0,100)
                    if rand_val > 40:
                        action_choice = "Weapon"
                    else:
                        action_choice = choice(item_attack_options)
                else:
                    rand_val = randint(0,100)
                    if rand_val > 60:
                        action_choice = "Weapon"
                    else:
                        action_choice = choice(item_attack_options)                  

            elif len(magic_list)>0: #checks magic options first
                if (self.ai_type[1] == "Magic") and rand_val>20:
                    action_choice = "Magic " + choice(magic_list)
                elif (self.ai_type[1] == "Mixed") and rand_val>50:
                    action_choice = "Magic " + choice(magic_list)
                elif (self.ai_type[1] == "Weapon") and rand_val>80:
                    action_choice = "Magic " + choice(magic_list)
                elif self.paralyzed == True: #can still use items and magic (cannot be muted if got here)
                    if len(item_attack_options) == 0:
                        action_choice = "Magic " + choice(magic_list)
                    else:
                        action_choice = choice(item_attack_options)
                else: #selects weapon, or item
                    if len(item_attack_options) == 0:
                        action_choice = "Weapon"
                    elif self.ai_type[0] == "Agressive":
                        rand_val = randint(0,100)
                        if rand_val > 40:
                            action_choice = "Weapon"
                        else:
                            action_choice = choice(item_attack_options)
                    else:
                        rand_val = randint(0,100)
                        if rand_val > 60:
                            action_choice = "Weapon"
                        else:
                            action_choice = choice(item_attack_options) 
            else:
                action_choice = "Weapon"
        else:
            if (len(heal_options) > 0) and (heal == True):
                if self.muted == False:
                    if (self.ai_type[1] == "Magic") and ("Magic Heal" in heal_options):
                        action_choice = "Magic Heal"
                    else:
                        action_choice = choice(heal_options)
                else:
                    if "Magic Heal" in heal_options:
                        heal_options.remove("Magic Heal")
                    if len(heal_options)>0:
                        action_choice = choice(heal_options)
                    else:
                        items_list = list(self.items.keys())                    
                        if "Antidote" in items_list:
                            items_list.remove("Antidote")                    
                        if len(items_list)>0:
                            action_choice = "Item " + choice(items_list)
                        else:
                            action_choice = "Weapon"
            else:
                items_list = list(self.items.keys())
                if "Mega_Healing_Potion" in items_list:
                    items_list.remove("Mega_Healing_Potion")
                if "Small_Healing_Potion" in items_list:
                    items_list.remove("Small_Healing_Potion")
                if "Antidote" in items_list:
                    items_list.remove("Antidote")
                if len(items_list)>0:
                    action_choice = "Item " + choice(items_list)
                else:
                    if self.paralyzed == True:
                        action_choice = "Continue"
                    else:
                        action_choice = "Weapon"
        return action_choice

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

class Magic:
    """Class of functions for all magic spells
    """
    #note: all of these functions returns a bool on whether it succeeded or not, but this functionality is unsed in the main game
    #defensive spells
    def Cure(self, caster: Person) -> bool: 
        """Removes negative status effects

        Args:
            caster (Person): Person to cure

        Returns:
            bool: If spell succeded or failed
        """

        if len(caster.status) == 0:
            print("You have no statuses! GG you just wasted a spell!")
            return False
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 50):
            positive_effects: list[Status] = []  
            for i in range(len(caster.status)):
                if caster.status[i].isgood == True:
                    positive_effects.append(caster.status[i])
            if len(positive_effects) == len(caster.status):
                print("You had no negative status effects! GG you just wasted a spell")
                return False
            caster.status.clear()
            if len(positive_effects) > 0:
                caster.status.extend(positive_effects)
            print(f"{caster.title} Cured all negative effects!")
            return True
        else:
            print(f"{caster.title}'s Cure Failed")
            return False

    def Heal(self, caster: Person) -> bool:
        """Heals user by 20% of max health. 100% chance of success

        Args:
            caster (Person): Person to heal

        Returns:
            bool: If spell succeded or failed
        """        
        if caster.max_health == caster.health:
            print("You fool, you just wasted a spell. Even your enemy is smarter than this!")
            return False
        cur_health = caster.health
        caster.health += int(caster.max_health * 0.2)
        if caster.health > caster.max_health: 
            caster.health = caster.max_health
        delta_health = caster.health - cur_health
        print(f"{caster.title} gained {delta_health} health!")
        return True

    def Protect(self, caster: Person) -> bool:
        """Raises Caster's defense by 20

        Args:
            caster (Person): Person to raise defense

        Returns:
            bool: If spell succeded or failed
        """   

        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 80):
            caster.status.append(Status("Protect", True, duration=2, chance_to_remove=0))
            print(f"{caster.title}'s defense rose by 20!")
            return True
        else:
            print(f"{caster.title}'s Protect failed")
            return False

    def Fast(self, caster: Person) -> bool:
        """Raises Caster's speed by 30

        Args:
            caster (Person): Person to raise speed

        Returns:
            bool: If spell succeded or failed
        """          
        #increases speed
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 80):
            caster.status.append(Status("Fast", True, duration=2, chance_to_remove=0))
            print(f"{caster.title}'s speed rose by 30!")
            return True
        else:
            print(f"{caster.title}'s Fast spell failed!")
            return False

    #offensive
    def Fireball(self, caster: Person, opponent: Person) -> bool:
        """Chance to hit opponent with a fireball doing 40-60 damage, with a chance to inflict Burn

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """          
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 65):
            damage = max(0,(randint(40,60) - opponent.defense + caster.base_dmg))
            opponent.health -= damage
            print(f"{opponent.title} lost {damage} health!")            
            success_val = randint(0,100)
            if success_val <= (30 - opponent.magic_proficiency):
                opponent.status.append(Status("Burn",False))
                print(f"{opponent.title} got afflicted with Burn for 3 turns!")
            return True
        else:
            print(f"{caster.title}'s fireball missed!")
            return False
            
    def Lightning(self, caster: Person, opponent: Person) -> bool:
        """Chance to hit opponent with a Lightning spell doing 40-60 damage, with a chance to inflict Paralysis

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """     
        title_boost = 1
        if "Shark" == opponent.title:
            title_boost = 2
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 55):
            opponent_damage = max(0,((randint(40,60) + caster.base_dmg) * title_boost - opponent.defense))
            opponent.health -= opponent_damage
            print(f"{opponent.title} lost {opponent_damage} health!")            
            success_val = randint(0,100)
            if success_val <= (20 - opponent.magic_proficiency+ 200*title_boost):
                opponent.status.append(Status("Paralysis",False,duration=2,chance_to_remove=35))
                print(f"{opponent.title} got afflicted with Paralysis for 2 turns! They wont be able to use weapons til this expires!")

            return True
        else:
            print(f"{caster.title}'s Lightning spell missed!")
            return False

    def Nuke(self, caster: Person, opponent: Person) -> bool:
        """Chance to hit opponent with a Nuke doing 100-150 damage, dealing 50-100 damage to yourself aswell

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        #high damage, hits caster aswell. Low number of uses
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 35):
            opponet_damage = max(0,((randint(100,150) + caster.base_dmg) - opponent.defense))
            opponent.health -= opponet_damage
            print(f"{opponent.title} lost {opponet_damage} health!")
            caster_damage = max(0,((randint(50,100) + caster.base_dmg) - caster.defense))
            caster.health -= caster_damage
            print(f"{caster.title} got hit by the shockwave!")
            print(f"{caster.title} lost {caster_damage} health!")
            return True
        else:
            print(f"{caster.title}'s Nuke missed! How does that even happen?!?")
            caster.health -= 5 + (abs(caster.base_dmg) // 2)
            print(f"{caster.title} lost 5 HP just from the shock of being that bad!")
            return False

    def Break(self, caster: Enemy, opponent: Player) -> bool:
        """Chance to break all of 1 random item in the opponent's item list 

        Args:
            caster (Enemy): Enemy casting the spell
            opponent (Player): Player affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        #chance to break items in player inventory - enemy specific
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 50):
            if len(opponent.items) == 0:
                print(f"{opponent.title} is all out of items. Theres none to break!\n\n-- you got lucky this time --\n")
                return False
            else:
                item_names = list(opponent.items.keys())
                random_item = choice(item_names)
                del opponent.items[random_item]
                print(f"All of {opponent.title}'s {random_item}'s got destroyed!")
                return True
        else:
            print(f"{caster.title}'s Break spell missed! Whew.")
            return False

    def Scar(self, caster: Person, opponent: Person) -> bool:
        """Chance to permantly lower opponent Max health by 7.5%, then deal 30-50 damage

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """              
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 30):
            old_max = opponent.max_health
            old_health = opponent.health
            opponent.max_health -= int(opponent.max_health * 0.075)
            if opponent.health > opponent.max_health:
                opponent.health = opponent.max_health
            opponent_damage = max(0,((randint(30,50) + caster.base_dmg) - opponent.defense))
            opponent.health -= opponent_damage
            print(f"{opponent.title} lost {old_health-opponent.health} health!")            
            print(f"{opponent.title} got Scarred! They permantly lost 5% of their max health ({old_max} -> {opponent.max_health})")
            return True
        else:
            print(f"{caster.title}'s Scar spell missed!")
            return False        

    #offensive status effects
    def Poison(self, caster: Person, opponent: Person) -> bool:
        """Chance to afflict opponent with Poison, dealing 5% of their max health per turn

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 70):
            opponent.status.append(Status("Poison", False, duration=6))
            print(f"{opponent.title} got aflicted with Poison! They will lose 5%MaxHP per turn til it expires!")
            return True
        else:
            print(f"{caster.title}'s Poison spell missed!")
            return False

    def Instant_Death(self, caster: Person, opponent: Person) -> bool:
        """Chance to kill opponent instantly, Base chance of 5%, scales with magic profficiency - max chance caps at 20%

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        success_val = randint(0,100)
        max_chance = min(caster.magic_proficiency * 2 + 5, 20)
        if success_val <= max_chance:
            opponent.health = -100
            print(f"{opponent.title} Died")
            return True
        else:
            print(f"{caster.title}'s Instant Death spell missed!")
            return False

    def Stop(self, caster: Person, opponent: Person) -> bool:
        """Chance to afflict opponent with Stop- opponent cannot make an action that turn

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 15):
            opponent.status.append(Status("Stop", False, duration=2))
            print(f"{opponent.title} got Stopped! They will not be able to make a move until this expires!")
            return True
        else:
            print(f"{caster.title}'s Stop spell missed!")
            return False

    def Slow(self, caster: Person, opponent: Person) -> bool:
        """Chance to lower opponent's speed by 30

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 85):
            old_speed = opponent.speed
            delta_speed = old_speed - max(0, opponent.speed-30)
            opponent.status.append(Status("Slow", False, chance_to_remove=10))
            print(f"{opponent.title} got slowed! They lost {delta_speed} speed!")
            return True
        else:
            print(f"{caster.title}'s Slow spell missed!")
            return False

    def Mute(self, caster: Person, opponent: Person) -> bool:
        """Chance to afflict opponent with Mute- opponent cannot use magic

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        #chance to make opponent not able to cast spells
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 45):
            opponent.status.append(Status("Mute", False, duration=1))
            print(f"{opponent.title} got muted! They cannot cast spells!")
            return True
        else:
            print(f"{caster.title}'s Mute spell missed!")
            return False

    def Constrict(self, caster: Person, opponent: Person) -> bool:
        """Chance to lower opponent's defennse by 30

        Args:
            caster (Person): Person casting the spell
            opponent (Person): Person affected by spell

        Returns:
            bool: If spell succeded or failed
        """             
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 55):
            old_def = opponent.defense
            delta_def = old_def - max(0, opponent.defense-30)
            opponent.status.append(Status("Constrict", False, chance_to_remove=10))
            print(f"{opponent.title} got constricted! They lost {delta_def} defense!")
            return True
        else:
            print(f"{caster.title}'s Slow spell missed!")
            return False

class Items:
    """Item Functions
    """
    def Small_Healing_Potion(self, caster: Person) -> bool:
        """Small healing potion, healing 30%MaxHP

        Args:
            caster (Person): Person using item

        Returns:
            bool: If item succeded or failed
        """
        if caster.health == caster.max_health:
            print("Your HP is maxed already! You just wasted an item GG")
            return False
        cur_health = caster.health
        caster.health += int(caster.max_health * 0.3)
        if caster.health > caster.max_health:
            caster.health = caster.max_health
        delta_health = caster.health - cur_health
        print(f"{caster.title} gained {delta_health} health!")
        return True

    def Mega_Healing_Potion(self, caster: Person):
        """Mega healing potion, healing 60%MaxHP

        Args:
            caster (Person): Person using item

        Returns:
            bool: If item succeded or failed
        """        
        if caster.health == caster.max_health:
            print("Your HP is maxed already! You just wasted a RARE item.\nGG you fool")
            return False
        cur_health = caster.health
        caster.health += int(caster.max_health * 0.6)
        if caster.health > caster.max_health:
            caster.health = caster.max_health
        delta_health = caster.health - cur_health
        print(f"{caster.title} gained {delta_health} health!")
        return True

    def Antidote(self, caster: Person) -> bool:
        """Antidote potion, cures all negative effects

        Args:
            caster (Person): Person using item

        Returns:
            bool: If item succeded or failed
        """   
        if len(caster.status) == 0:
            print("You have no statuses! GG you just wasted a spell!")
            return False        
        positive_effects: list[Status] = []  
        for i in range(len(caster.status)):
            if caster.status[i].isgood == True:
                positive_effects.append(caster.status[i])
        if len(positive_effects) == len(caster.status):
            print("You had no negative status effects! GG you just wasted a spell")
            return False                
        caster.status.clear()
        if len(positive_effects) > 0:
            caster.status.extend(positive_effects)
        print(f"{caster.title}'s Antidote cured all negative effects!")
        return True

    def Strength(self, caster: Person) -> bool:
        """Strength Potion

        Args:
            caster (Person): Person using item

        Returns:
            bool: If item succeded or failed
        """
        success_val = randint(0,100)
        if success_val <= 90:
            caster.status.append(Status("Strength", True, duration=4, chance_to_remove=5))
            print(f"{caster.title} base dmg rose by {30} for 4 turns!")
            if success_val <= 10:
                caster.status.append(Status("Strength", True, duration=2, chance_to_remove=5))
                print(f"Woah! Strength potion was super effective\n{caster.title} base dmg rose by another {30} for 2 turns!")            
            return True        
        print(f"{caster.title}'s Strength Item had no effect!")
        return False

    def Grenade(self, caster: Person, opponent: Person) -> bool:
        """Grenade item, Chance to deal 40-60 dmg

        Args:
            caster (Person): Person using item
            opponent (Person): Person affected by item

        Returns:
            bool: If item succeded or failed
        """         
        success_val = randint(0,100)
        if success_val <= 90:
            damage = max(0,((randint(40,60) + caster.base_dmg) - opponent.defense))
            opponent.health -= damage
            print(f"{opponent.title} lost {damage} health!")            
            return True
        else:
            print(f"{caster.title}'s grenade missed!")
            return False

    def Stick(self, caster: Person, opponent: Person) -> bool:
        """Stick Item, increases opponent's dmg by 2, and has a chance to deal 140-160 dmg to opponent

        Args:
            caster (Person): Person using item
            opponent (Person): Person affected by item

        Returns:
            bool: If item succeded or failed
        """        
        success_val = randint(0,100)
        title_boost = 0
        opponent.weapon.dmg += 2        
        print(f"{opponent.title}'s dmg has increased by 2!")
        if caster.title == "Toddler":
            title_boost = 30
        if success_val <= 5 + title_boost:
            damage = (randint(140,160) + int(caster.base_dmg * 1.5)) - opponent.defense
            opponent.health -= damage
            print(f".\n..\n...\n{opponent.title} got prodded massively, and lost {damage} health!")            
            return True
        else:
            print(f"{caster.title}'s prodding has slightly annoyed {opponent.title}.")
            return False

    def Weakness(self, caster: Person, opponent: Person) -> bool:
        """Weakness Potion

        Args:
            caster (Person): Person using item

        Returns:
            bool: If item succeded or failed
        """
        success_val = randint(0,100)
        if success_val <= 55:
            opponent.status.append(Status("Weakness", True, duration=2, chance_to_remove=10))
            print(f"{opponent.title} base dmg fell by {30} for 2 turns!")         
            return True      
        print(f"{caster.title}'s Weakness Item had no effect!")  
        return False


class MainGame:
    """Main game object
    """
    def __init__(self) -> None:
        """assigns base gamme attributes, then goes into menu_screen()
        """
        self.character = ""
        self.weapon = Weapon()
        self.player: Player
        self.enemy: Enemy
        self.enemies_killed = 0
        self.endless = False
        self.menu_screen()

    def action(self, caster: Person, opponent: Person, action: str) -> bool:
        """Does the action the caster selected

        Args:
            caster (Person): Person doing the action
            opponent (Person): Person affected by the action
            action (str): action str chosen

        Returns:
            bool: action_success 
        """
        action_list = action.split()
        main_action = ""
        sub_action = ""
        attack_success = False
        if len(action_list) > 2 or len(action_list) <= 0:
            print("action list len error")
            exit_game()
        if len(action_list) == 1:
            main_action = action_list[0]
            check = ["Weapon", "Continue"]
            if main_action not in check:
                print("main action is not weapon but length of list is 1")
                exit_game()
            sub_action = ""
        else:
            main_action = action_list[0]
            sub_action = action_list[1]

        match main_action:
            case "Continue":
                print("No action taken this turn")
                return attack_success
            case "Weapon":
                print(f"{caster.title} attacked with their {caster.weapon.weapon_type}!")
                success_val = randint(0,100)
                if success_val <= caster.weapon.accuracy:
                    success_val = randint(0,100)
                    if success_val <= caster.weapon.crit_chance:
                        delta_health = max(0,randint(int((caster.weapon.dmg + caster.base_dmg) * 1.5), int((caster.weapon.dmg + caster.base_dmg) * 2)) - opponent.defense)
                        opponent.health -= delta_health
                        print(f"{caster.title} crit! {opponent.title} lost {delta_health} health!")  
                    else: 
                        delta_health = max(0,randint(int((caster.weapon.dmg + caster.base_dmg) * 0.8), int((caster.weapon.dmg + caster.base_dmg) * 1.2)) - opponent.defense)
                        opponent.health -= delta_health
                        print(f"{opponent.title} lost {delta_health} health!")  
                    attack_success = True
                    return attack_success
                print(f"{caster.title}'s attack missed!")
                return attack_success
            case "Magic":
                print(f"{caster.title} used a <{sub_action}> spell!")
                magic_class = Magic()
                match sub_action:
                    case "Cure":
                        attack_success = magic_class.Cure(caster)
                    case  "Heal":
                        attack_success = magic_class.Heal(caster)
                    case "Protect":
                        attack_success = magic_class.Protect(caster)
                    case "Fast":
                        attack_success = magic_class.Fast(caster)
                    case "Fireball":
                        attack_success = magic_class.Fireball(caster, opponent)
                    case "Lightning":
                        attack_success = magic_class.Lightning(caster, opponent)
                    case "Nuke":
                        attack_success = magic_class.Nuke(caster, opponent)
                    case "Poison":
                        attack_success = magic_class.Poison(caster, opponent)
                    case "Instant_Death":
                        attack_success = magic_class.Instant_Death(caster, opponent)
                    case "Stop":
                        attack_success = magic_class.Stop(caster, opponent)
                    case "Slow":
                        attack_success = magic_class.Slow(caster, opponent)
                    case "Mute":
                        attack_success = magic_class.Mute(caster, opponent)
                    case "Break":
                        if type(caster).__name__ != "Enemy":
                            print("Break can only take enemy type")
                            exit_game()
                        attack_success = magic_class.Break(caster, opponent)
                    case "Scar":
                        attack_success = magic_class.Scar(caster, opponent)
                    case "Constrict":
                        attack_success = magic_class.Constrict(caster,opponent)    
                    case _:
                        print("Magic Edge case, this should not happen")
                        print(sub_action)
                        exit_game()
                caster.magic[sub_action] -= 1
                if caster.magic[sub_action] <= 0:
                    del caster.magic[sub_action]            
                return attack_success
            case "Item":
                item_class = Items()
                print(f"{caster.title} used a {sub_action} item!")                
                match sub_action:
                    case "Small_Healing_Potion":
                        attack_success = item_class.Small_Healing_Potion(caster)
                    case "Mega_Healing_Potion":
                        attack_success = item_class.Mega_Healing_Potion(caster)
                    case "Antidote":
                        attack_success = item_class.Antidote(caster)
                    case "Strength":
                        attack_success = item_class.Strength(caster)    
                    case "Grenade":
                        attack_success = item_class.Grenade(caster, opponent)
                    case "Stick":
                        attack_success = item_class.Stick(caster, opponent)
                    case "Weakness":
                        attack_success = item_class.Weakness(caster, opponent)
                    case _:
                        print("Item Edge case, this should not happen")
                        print(sub_action)
                        exit_game()             
                caster.items[sub_action] -= 1
                if caster.items[sub_action] <= 0:
                    del caster.items[sub_action]                    
                return attack_success   
            case _:
                print("Main Action edge case, this should not happen")
                print(main_action)
                exit_game()

    def selection_descriptions(self, main_selection: str, sub_selection: str) -> None:   
        """Gets and prints descritions for the selected action

        Args:
            main_selection (str): Main selection, either Attack, Magic, or Item
            sub_selection (str): Sub selection in the main selection
        """
        match main_selection:
            case "Attack":
                print(f"{self.player.weapon}")
            case "Magic":
                match sub_selection:
                    case "Cure":
                        max_percent = min(100, 2*self.player.magic_proficiency+15)
                        print(f"---Cure Spell---\nChance to succeed: 50% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Cures all negative status effects\n---Cure Spell---")
                    case  "Heal":
                        heal_hp = int(self.player.max_health*0.2)
                        if heal_hp+self.player.health > self.player.max_health:
                            heal_hp = self.player.max_health - self.player.health
                        print(f"---Heal Spell---\nChance to succeed: 100%")
                        print(f"Description: Heals 20% of max health ({heal_hp}HP)\n---Heal Spell---")
                    case "Protect":
                        max_percent = min(100, self.player.magic_proficiency+80)
                        print(f"---Protect Spell---\nChance to succeed: 80% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Raises defense by 20 \n---Protect Spell---")
                    case "Fast":
                        max_percent = min(100, self.player.magic_proficiency+80)
                        print(f"---Fast Spell---\nChance to succeed: 80% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Raises speed by 30 for 2 turns\n---Fast Spell---")
                    case "Fireball":
                        max_percent = min(100, self.player.magic_proficiency+65)
                        print(f"---Fireball Spell---\nChance to succeed: 65% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Deals between 40-60 dmg, minus enemy defense")
                        print(f"Extra Effects: Has a 30% chance (minus enemy magic profficiency) to inflict Burn for 3 turns\n---Fireball Spell---")
                    case "Lightning":
                        max_percent = min(100, self.player.magic_proficiency+55)
                        print(f"---Lightning Spell---\nChance to succeed: 55% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Deals between 40-60 dmg, minus enemy defense (+secret effect)")
                        print(f"Extra Effects: Has a 20% chance (minus enemy magic profficiency) to inflict Paralysis for 2 turns\n---Lightning Spell---")
                    case "Nuke":
                        max_percent = min(100, 2*self.player.magic_proficiency+35)
                        print(f"---Nuke Spell---\nChance to succeed: 35% + 2 * {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Deals between 100-150 dmg, minus enemy defense")
                        print(f"Extra Effects: Deals 50-100 dmg, minus your defense to yourself as well (+secret effect)\n---Nuke Spell---")
                    case "Poison":
                        max_percent = min(100, self.player.magic_proficiency+70)
                        print(f"---Poison Spell---\nChance to succeed: 70% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Afflicts enemy with Poison for 6 turns, causing them to lose 5% of their max hp per turn\n---Poison Spell---")
                    case "Instant_Death":
                        max_percent = min(2*self.player.magic_proficiency + 5, 20)
                        print(f"---Instant_Death Spell---\nChance to succeed (max of 20%): 5% + 2*{self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Instantly kills opponent\n---Instant_Death Spell---")
                    case "Stop":
                        max_percent = min(100, 2*self.player.magic_proficiency+15)
                        print(f"---Stop Spell---\nChance to succeed: 15% + 2*{self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Opponent loses 2 turns\n---Stop Spell---")
                    case "Slow":
                        max_percent = min(100, self.player.magic_proficiency+85)
                        print(f"---Slow Spell---\nChance to succeed: 85% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Opponent loses 30 speed for 3 turns\n---Slow Spell---")
                    case "Mute":
                        max_percent = min(100, 2*self.player.magic_proficiency+45)
                        print(f"---Mute Spell---\nChance to succeed: 45% + 2*{self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Opponent cannot use magic for 1 turn\n---Mute Spell---")
                    case "Break":
                        max_percent = min(100, self.player.magic_proficiency+50)
                        print(f"---Break Spell---\nChance to succeed: 50% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Opponent loses all items of 1 random item\n---Break Spell---")
                    case "Scar":
                        max_percent = min(100, 2*self.player.magic_proficiency+30)
                        print(f"---Scar Spell---\nChance to succeed: 30% + 2*{self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Opponent permantly loses 7.5% of their Max HP and deals 30-50 dmg\n---Scar Spell---")
                    case "Constrict":
                        max_percent = min(100, self.player.magic_proficiency+55)                        
                        print(f"---Constrict Spell---\nChance to succeed: 55% + {self.player.magic_proficiency} magic profficiency = {max_percent}%")
                        print(f"Description: Opponent loses 30 defense for 3 turns\n---Constrict Spell---")                        
                    case _:
                        print("Magic DESCRIPTION edge case, this should not happen")
                        print(main_selection,sub_selection)
                        exit_game()
            case "Item":
                match sub_selection:
                    case "Small_Healing_Potion":
                        heal_hp = int(self.player.max_health*0.3)
                        if heal_hp+self.player.health > self.player.max_health:
                            heal_hp = self.player.max_health - self.player.health
                        print(f"---Small_Healing_Potion Item---\nChance to succeed: 100%")
                        print(f"Description: Heals 30% of max health ({heal_hp}HP)\n---Small_Healing_Potion Item---")
                    case "Mega_Healing_Potion":
                        heal_hp = int(self.player.max_health*0.6)
                        if heal_hp+self.player.health > self.player.max_health:
                            heal_hp = self.player.max_health - self.player.health
                        print(f"---Mega_Healing_Potion Item---\nChance to succeed: 100%")
                        print(f"Description: Heals 60% of max health ({heal_hp}HP)\n---Mega_Healing_Potion Item---")
                    case "Antidote":
                        print(f"---Antidote Item---\nChance to succeed: 100%")
                        print(f"Description: Cures all negative status effects\n---Antidote Item---")
                    case "Strength":
                        print(f"---Strength Item---\nChance to succeed: 90%")
                        print(f"Description: Adds 30 base damage to all sources\n---Strength Item---")                        
                    case "Grenade":
                        print(f"---Grenade Item---\nChance to succeed: 90%")
                        print(f"Description: Deals between 40-60 dmg, minus enemy defense\n---Grenade Item---")
                    case "Stick":
                        print(f"---Stick Item---\nChance to succeed: 5%")
                        print(f"Description: Deals between [obfuscated] dmg, minus enemy defense")
                        print(f"Extra Effects: Has a 100% chance to annoy your enemy (enemy's dmg goes up by 2)\n---Stick Item---")
                    case "Weakness":
                        print(f"---Weakness Item---\nChance to succeed: 55%")
                        print(f"Description: Lowers opponent's base damage to all sources by 30\n---Weakness Item---")                     
                    case _:
                        print("Item DESCRIPTION Edge case, this should not happen")
                        print(main_selection, sub_selection)
                        exit_game()             
            case _:
                print("Main Selection DESCRIPTION edge case, this should not happen")
                print(main_selection)
                exit_game()

    def user_action_select(self) -> str:
        """Gets user action, restricting it allowed actions by game state

        Returns:
            str: string in form 'main_action sub_action'
        """
        has_magic = False
        has_items = False           
        if len(self.player.magic)>0:
            if any(self.player.magic.values()):
                has_magic = True
        if len(self.player.items)>0:
            if any(self.player.items.values()):
                has_items = True   
        main_user_options = ["Attack", "Use Magic", "Use Item", "Exit Game"] 
        if has_items == False:
            main_user_options.pop(2)
        if has_magic == False:
            main_user_options.pop(1)
        if self.player.muted == True:
            if "Use Magic" in main_user_options:
                main_user_options.remove("Use Magic")
            print(f"You are Muted! You cannot use magic this turn")

        if self.player.paralyzed == True:
            main_user_options.pop(0)
            print(f"You are Paralyzed! You cannot use your Weapon this turn")

        if self.player.stopped == True:
            main_user_options = ["Continue", "Exit Game"]       
            print("You are Stopped! You cannot make any actions this turn")

        if len(main_user_options) <= 1:
            main_user_options = ["Continue", "Exit Game"]  
        main_acceptable_input_nums = []             
        for idx, string in enumerate(main_user_options):
            main_acceptable_input_nums.append(str(idx+1))
        main_print_str_nums = ", ".join(main_acceptable_input_nums)            
        user_input = ""
        option_chose = ""
        item_chose = ""
        magic_chose = ""               
        confirmed_selection = False
        #get user selection            
        while confirmed_selection == False:
            while True:
                try:
                    for idx, string in enumerate(main_user_options):
                        print(idx+1, "| " + string)
                    user_input = input(f"Pick the option corresponding to the numbers: {main_print_str_nums}\n-> ")
                    print()
                    if not(user_input.isnumeric()):
                        raise ValueError
                    elif user_input not in main_acceptable_input_nums:
                        raise ValueError
                    else:
                        option_chose = main_user_options[int(user_input)-1]
                        if option_chose.startswith("Use "):
                            option_chose = option_chose[4:]
                        break
                except ValueError:
                    print("Invalid Input.") 

            if option_chose == "Exit Game":
                user_input = input("Do really want to exit? Your progress will be lost 'Y'/'N'\n-> ").upper()
                print()
                if "Y" in user_input:
                    exit_game()
            elif option_chose == "Continue":
                confirmed_selection = True                    
            elif option_chose == "Attack":
                while True:
                    self.selection_descriptions(option_chose, "")                             
                    user_input = input("Type 'Y' to confirm you want to attack, or 'B' or 'N' to go back\n-> ").upper()
                    print()
                    if ("N" in user_input) or ("B" in user_input):
                        break
                    elif "Y" in user_input:
                        confirmed_selection = True
                        break
                    else:
                        print("Incorrect letter(s)")                 
            elif option_chose ==  "Item":
                acceptable_input_nums = []                
                user_options = self.player.items
                for idx, (key, value) in enumerate(user_options.items()):
                    if idx == 0:
                        print(idx+1, "| " + key + ":", value, "Uses left")
                    else:
                        print(idx+1, "| " + key + ":", value)
                    acceptable_input_nums.append(str(idx+1))                    
                acceptable_input_nums.append("b")     
                print_str_nums: str = ", ".join(acceptable_input_nums) + "ack"
                #get user selection            
                while True:
                    try:
                        user_input = input(f"Pick the option corresponding to the numbers, or 'back' to go back: {print_str_nums}\n-> ").upper()
                        print()
                        if "B" in user_input:
                            break
                        elif not(user_input.isnumeric()):
                            raise ValueError
                        elif user_input not in acceptable_input_nums:
                            raise ValueError
                        else:
                            while True:
                                temp_chosen = list(user_options.keys())[int(user_input)-1]    
                                print()
                                self.selection_descriptions(option_chose, temp_chosen)
                                print()                               
                                user_input = input(f"Type 'Y' to confirm you want to use <{temp_chosen}>, or 'B' or 'N' to go back\n-> ").upper()
                                if ("N" in user_input) or ("B" in user_input):
                                    break
                                elif "Y" in user_input:
                                    item_chose = temp_chosen
                                    confirmed_selection = True      
                                    break              
                                else:
                                    print("Invalid letter(s)")                    
                            break
                    except ValueError:
                        print("Invalid Input.")  
            elif option_chose == "Magic":
                acceptable_input_nums = [] 
                user_options = self.player.magic
                for idx, (key, value) in enumerate(user_options.items()):
                    if idx == 0:
                        print(idx+1, "| " + key + ":", value, "Casts remaining")
                    else:
                        print(idx+1, "| " + key + ":", value)
                    acceptable_input_nums.append(str(idx+1)) 
                acceptable_input_nums.append("b")     
                print_str_nums: str = ", ".join(acceptable_input_nums) + "ack"
                #get user selection            
                while True:
                    try:
                        user_input = input(f"Pick the option corresponding to the numbers, or 'back' to go back: {print_str_nums}\n-> ").upper()
                        print()
                        if "B" in user_input:
                            break
                        elif not(user_input.isnumeric()):
                            raise ValueError
                        elif user_input not in acceptable_input_nums:
                            raise ValueError
                        else:
                            while True:
                                temp_chosen = list(user_options.keys())[int(user_input)-1]
                                print()
                                self.selection_descriptions(option_chose, temp_chosen)   
                                print()                                      
                                user_input = input(f"Type 'Y' to confirm you want to use <{temp_chosen}>, or 'B' or 'N' to go back\n-> ").upper()
                                if ("N" in user_input) or ("B" in user_input):
                                    break
                                elif "Y" in user_input:
                                    magic_chose = temp_chosen 
                                    confirmed_selection = True
                                    break
                                else:
                                    print("Invalid letters(s)")
                            break
                    except ValueError:
                        print("Invalid Input.")
            else:
                print("option chose error")
                print(option_chose)
                exit_game() 
        
        #find action associated with user selection
        if option_chose == "Attack":
            option_chose = "Weapon"
        player_choice = option_chose + " " + item_chose + magic_chose  
        return player_choice      

    def menu_screen(self) -> None:
        """This function prints the main menu screen as well as handles all validations required from the user, then goes into character_select()
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
                    break
                elif "EX" in menuinput: #exits program
                    leave_y = input("Are you really choosing the option of cowardice? Type \"Y\" if you are paralyzed by fear, or proceed with any other input\n-> ").upper()
                    if leave_y == "Y":
                        print("The art of violent confrontation is not for the meek.")
                        print(".\n.\n.\nExiting Arena.")
                        exit_game()
                else: #this is for wrong inputs not caught
                    print("You weren't supposed to see this.\n")
                    raise KeyError
            except ValueError:
                print("Select a valid option.\n")
            except KeyError:
                exit_game()
        self.character_select()                
        return None

    def character_select(self) -> None:
        """Gets character selection from user, then goes into weapon_select_menu()
        """
        while True:
            menu_cs_text: str = """
                ------------------------------------------
                            Pick Your Character
                ------------------------------------------
                              |  
                     Wizard   |      Type Wizard To Pick
                              |  
                ------------------------------------------
                     Waffle   |      
                      House   |      Type Waffle To Pick
                    Employee  |          
                ------------------------------------------
                              |  
                    Toddler   |      Type Toddler To Pick
                              | 
                ------------------------------------------
                              |
                     Rogue    |      Type Rogue To Pick
                              |
                -------------------------------------------
                """
            print(menu_cs_text)
            menuinput: str = input("Enter Fighter type or \"Exit\"\n-> ").upper()
            inputcheck: list = ["WI", "WA", "TO", "RO", "EX"] #checking substrings for higher chance of getting right thing
            character: str = ""
            try: #first layer of input validation
                if menuinput[0:2] not in inputcheck:
                    raise ValueError
                elif "EX" in menuinput: #exits program
                    leave_y = input("Do you really want to leave? Type \"Y\" if so or anything else to continue.\n-> ")
                    if leave_y == "Y":
                        print(".\n.\n.\nExiting Arena.")
                        exit_game()
                elif "WI" or "WA" or "TO" or "RO" in menuinput: #continues with char select
                    character_list = ["WIZARD", "WAFFLE HOUSE EMPLOYEE", "TODDLER", "ROUGE"]
                    #https://stackoverflow.com/questions/2170900/get-first-list-index-containing-sub-string
                    #we can restrict menuinput to only be the first two characters because inputcheck above only checks the first two characters (kinda)
                    character: str = character_list[[idx for idx, string in enumerate(character_list) if menuinput[0:2] in string][0]].title() 
                    confirm_y = input(f"Is {character} the Fighter you want? Enter Y/N\n-> ").upper() #or confirm
                    if "Y" in confirm_y[0:5]:
                        self.character = character
                        break
                    #else:
                        #kick back to prev option
                else: #this is for wrong inputs not caught
                    print("You weren't supposed to see this.\n")
                    raise KeyError
            except ValueError:
                print("Select a valid option.\n")
        self.weapon_select_menu()                
        return None

    def weapon_select_menu(self) -> None: 
        """Gets user input for their chosen weapon, then assigns that weapon as an attribute 'weapon', then goes into start_game()
        """
        character = self.character.upper()
        weapon_list = []
        print("\n")
        print_statement = ""
        match character:
            case "WIZARD":
                print_statement = """
                ------------------------------------------------------
                                Pick Your Weapon
                ------------------------------------------------------
                                Damage:      10 
                    Staff       Hit Chance:  90   Type Staff To Pick
                                Crit Chance: 40
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
                weapon_list = ["Staff","Spear","Tome"]
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
                if response[0:2] not in imput_check:
                    raise ValueError
                else:
                    choice = weapon_list[[idx for idx, string in enumerate(weapon_list) if response[0:2].title() in string][0]]
                    self.weapon.assign(choice)
                    break                
            except ValueError:
                print("Invalid Input: Please Try Again")     
        self.start_game()                           
        
    def start_game(self) -> None:
        """Initializes everything with enemy and player, with defined values, then goes into game()
        """
        if self.enemies_killed == 0:
            self.player: Player = Player(self.character, self.weapon)
            del self.character
            del self.weapon
        print("\nYour Character is...")
        print("----------------------")
        print(self.player)
        print("----------------------")
        sleep_func(4)
        self.enemy = Enemy()
        print("\nYour opponent is...")
        print("----------------------")
        print(self.enemy)
        print("----------------------\n\n")     
        sleep_func(4)
        print("\n_-‾-_-‾-_-‾-_-‾-_\nStarting game...\n‾-_-‾-_-‾-_-‾-_-‾\n")
        self.game()
 
    def game(self) -> None:
        """Main game loop, plays until a Person's health is below 0 or user inputs Exit
        """
        ending_type: int = 0
        turn = 0
        while ending_type == 0:
            turn += 1
            player_cur_health = self.player.health
            enemy_cur_health = self.enemy.health
            print(f"\n\n    Turn {turn}:\n---------------")
            sleep_func(1)
            print(f"{self.player.title}: {self.player.health}/{self.player.max_health}HP, {self.player.speed} Speed", end="")
            if self.player.base_dmg != 0:
                print(f", dmg modifer: {self.player.base_dmg}")
            else:
                print()
            print(f"{self.enemy.title}: {self.enemy.health}/{self.enemy.max_health}HP, {self.enemy.speed} Speed", end="")    
            if self.enemy.base_dmg != 0:
                print(f", dmg modifer: {self.enemy.base_dmg}")  
            else:
                print()                  
            sleep_func(2)
            #get turn order
            first_player = ""
            if self.player.speed < self.enemy.speed:
                first_player = "Enemy"
            elif self.player.speed == self.enemy.speed:
                first_player = choice(["Player", "Enemy"])
            else:
                first_player = "Player"
                  
            #do actions
            if first_player == "Player":
                #1st attack                   
                print(f"\n\n{self.player.title}'s Turn:\n-‾-‾-‾-‾-‾-‾-‾-‾-‾-")                         
                player_choice = self.user_action_select()               
                print()
                sleep_func(1)         
                self.action(self.player, self.enemy, player_choice)
                sleep_func(1)
                #edit choices for next round                 
                self.player.remove_status_effects()      
                #apply status effects -> check for winner                            
                self.enemy.apply_status_effects()                                  
                if self.enemy.health <= 0:
                    print(f"{self.enemy.title} died!")
                    ending_type = 1
                    if self.player.health <= 0:
                        ending_type = 3
                    break          
                if self.enemy.health != enemy_cur_health:
                    print(f"{self.enemy.title} has {self.enemy.health}/{self.enemy.max_health} HP remaining")   
                if self.player.health != player_cur_health:                        
                    print(f"{self.player.title} has {self.player.health}/{self.player.max_health} HP remaining")                                   
                print("-_-_-_-_-_-_-_-_-_-")

                sleep_func(2)
                #2nd attack               
                print(f"\n\n{self.enemy.title}'s Turn:\n-‾-‾-‾-‾-‾-‾-‾-‾-‾-")           
                ai_choice = self.enemy.ai_action()                                                       
                sleep_func(1.5)             
                self.action(self.enemy, self.player, ai_choice)
                sleep_func(1)
                #edit choices for next round                 
                self.enemy.remove_status_effects()                   
                #apply status effects -> check for winner
                self.player.apply_status_effects() 
                if self.player.health <= 0:
                    ending_type = 2          
                    if self.enemy.health <= 0:
                        ending_type = 3         
                    break                
                if self.enemy.health != enemy_cur_health:
                    print(f"{self.enemy.title} has {self.enemy.health}/{self.enemy.max_health} HP remaining")   
                if self.player.health != player_cur_health:                        
                    print(f"{self.player.title} has {self.player.health}/{self.player.max_health} HP remaining")                 
                print("-_-_-_-_-_-_-_-_-_-\n")                 
            elif first_player == "Enemy":
                #1st attack           
                print(f"\n\n{self.enemy.title}'s Turn:\n-‾-‾-‾-‾-‾-‾-‾-‾-‾-")                            
                ai_choice = self.enemy.ai_action()   
                sleep_func(1.5)     
                self.action(self.enemy, self.player, ai_choice)
                sleep_func(1)
                #edit choices for next round                 
                self.enemy.remove_status_effects()                    
                #apply status effects -> check for winner
                self.player.apply_status_effects() 
                if self.player.health <= 0:
                    ending_type = 2   
                    if self.enemy.health <= 0:
                        ending_type = 3       
                    break                
                if self.enemy.health != enemy_cur_health:
                    print(f"{self.enemy.title} has {self.enemy.health}/{self.enemy.max_health} HP remaining")   
                if self.player.health != player_cur_health:                        
                    print(f"{self.player.title} has {self.player.health}/{self.player.max_health} HP remaining")         
                print("-_-_-_-_-_-_-_-_-_-\n")                                       
                sleep_func(2)

                #2nd attack
                print(f"\n\n{self.player.title}'s Turn:\n-‾-‾-‾-‾-‾-‾-‾-‾-‾-")                                                            
                player_choice = self.user_action_select()               
                print() 
                sleep_func(1.5)                                               
                self.action(self.player, self.enemy, player_choice)
                sleep_func(1)
                #edit choices for next round                 
                self.player.remove_status_effects()                 
                #apply status effects -> check for winner
                self.enemy.apply_status_effects() 
                if self.enemy.health <= 0:
                    ending_type = 1     
                    if self.player.health <= 0:
                        ending_type = 3
                    break                
                if self.enemy.health != enemy_cur_health:
                    print(f"{self.enemy.title} has {self.enemy.health}/{self.enemy.max_health} HP remaining")   
                if self.player.health != player_cur_health:                        
                    print(f"{self.player.title} has {self.player.health}/{self.player.max_health} HP remaining")                 
                print("-_-_-_-_-_-_-_-_-_-\n")         
            sleep_func(1)              
        self.ending(ending_type)

    def ending(self, endings: int) -> None:
        """Gets correct ending for inputed ending type

        Args:
            endings (_type_): Win condition, 1=Win, 2=Lose, 3=Both died (tie) 
        """
        print("\n\n\n")
        match endings:
            case 1:
                print("You Won !!")
                if self.endless == True:
                    self.enemies_killed += 1
                    print(f"{self.enemies_killed} Enimies killed")                    
                    self.start_game()
            case 2:
                print("You lost! ;c")
                if self.endless == True:
                    print(f"Total Enemies killed: {self.enemies_killed}!")
            case 3:
                print("You both died!")
                print("Ties may end up friendly in most games, but here, youre dead.\nYou lost!")
                if self.endless == True:
                    print(f"Total Enemies killed: {self.enemies_killed}!")                
            case _:
                print("ending edge case, this should not happen")
                print(endings)
                exit_game()
        sleep_func(5)
        if self.endless == False and endings == 1:
            user_input = input("Do you want to try to fight more monsters? 'Y'/'N'\n-> ").upper()
            if "Y" in user_input:
                self.enemies_killed += 1
                self.endless = True
                print(f"{self.enemies_killed} Enemy killed")
                self.start_game()
            else:
                exit_game(noexit=True)
        else:
            print("\nGame Over\n")
            exit_game(noexit=True)

def exit_game(noexit=False) -> NoReturn:
    """Exit game function

    Args:
        noexit (bool, optional): Paramater if you dont want to exit the game. Defaults to False.

    Returns:
        NoReturn: exit program class
    """
    if noexit == False:
        exit()
    print("restarting game...\n")

def sleep_func(n: int | float) -> None:
    """checks if debug mode is enabled (true/false value) in main block. If yes removes all sleep functions.

    Args:
        n (int | float): int for how long to sleep
    """
    global debugmode
    if debugmode == True: #this function is the goat, best addition I added. this has saved me HOURS
        return
    else:
        sleep(n)
        return


if __name__ == '__main__':
    debugmode = False
    while True:
        game = MainGame()