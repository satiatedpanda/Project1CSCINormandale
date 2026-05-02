from typing import NoReturn
from random import choice, randint

"""
    doc comment for things
"""

class Status:
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
    def __init__(self, *, title="", health=0, defense=0, magic_proficiency=0, speed=0, weapon: Weapon= Weapon().assign("Fists"), magic={}, items = {}):
        self.title = title
        self.weapon = weapon        

        self.health = health
        self.defense = defense #reduces damage taken
        self.speed = speed
        self.magic_proficiency = magic_proficiency #adds to chance of magic working
        self.items = items
        self.magic = magic
        self.status: list[Status] = []
        self.stopped: bool = False
        self.muted: bool = False
        self.paralyzed: bool = False
        self.default_speed = speed     
        self.default_defense = defense           
        self.max_health = health        

    def apply_status_effects(self):
        if len(self.status) > 0:
            for value in self.status:
                match value.status_name:
                    case "Poison":
                        self.health -= int(self.max_health * 0.05)
                        print(f"{self.title} is poisoned and lost {int(self.max_health*0.05)} health")

                        print(f"{self.title} is paralyzed and cannot use weapons!")
                    case "Protect":
                        self.defense += 25
                        print(f"{self.title} is protected and gained 25 defense!")
                    case "Burn":
                        self.health -= 10
                    case "Fast":
                        self.speed += 30                    
                    case "Slow":
                        self.speed -= 30  
                    case "Stop":
                        self.stopped = True #cant attack at all
                    case "Paralysis":
                        self.paralyzed = True #cant use weapons                        
                    case "Mute":
                        self.muted = True #cant use magic

                    case _: #catchall
                        print("error, invalid status name")
                value.duration -= 1

    def remove_status_effects(self): #ran right after user picks an option, before apply affects
        self.defense = self.default_defense
        self.speed = self.default_speed
        self.paralyzed = False
        self.muted = False
        self.stopped = False

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
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.title}, {self.health} health, {self.defense} defense, {self.speed} speed, {self.magic_proficiency} magic pro, weapon: {self.weapon.weapon_type}"

class Player(Person):
    def __init__(self, title: str, weapon: Weapon):
        self.assign_attributes(title)
        super().__init__(title=title, weapon=weapon, health=self.health, defense=self.defense, magic_proficiency=self.magic_proficiency, speed=self.speed, magic=self.magic, items=self.items)
        self.weapon: Weapon = weapon
    
    def assign_attributes(self, title: str) -> None:     
        items_list = ["Small_Healing_Potion", "Mega_Healing_Potion", "Antidote", "Grenade", "Stick"]
        magic_LIST = ["Cure", "Heal", "Protect", "Fast", "Stop", "Slow", "Mute", "Poison", "Fireball", "Lightning", "Nuke", "Instant_Death", "Scar"]        
        match title:
            case "Wizard":
                self.health = 250
                self.defense = 15
                self.speed = 30
                self.magic_proficiency = 30
                self.magic = {"Heal": 5, "Slow": 3, "Poison": 3, "Fireball": 4, "Lightning": 4, "Nuke": 2, "Instant_Death": 2, "Scar": 3} 
                self.items = {"Small_Healing_Potion": 2, "Antidote": 2}
            case "Waffle House Employee":
                self.health = 300
                self.defense = 10 
                self.speed = 40   
                self.magic_proficiency = 0               
                self.magic = {"Cure": 3, "Heal": 3, "Protect": 2, "Fast": 5, "Stop": 2, "Mute": 2, "Poison": 5, "Scar": 3} 
                self.items = {"Small_Healing_Potion": 3, "Mega_Healing_Potion": 1, "Grenade": 4}
            case "Toddler":
                self.health = 175
                self.defense = 0
                self.speed = 100   
                self.magic_proficiency = 20                
                self.magic = {"Protect": 5, "Stop": 2, "Slow": 3, "Mute": 3, "Poison": 2, "Nuke": 3, "Instant_Death": 5, "Scar": 5}
                self.items = {"Small_Healing_Potion": 5, "Grenade": 4, "Stick": 10}
            case "Rouge":
                self.health = 200
                self.defense = 10 
                self.speed = 70   
                self.magic_proficiency = 0                
                self.magic = {"Cure": 2, "Heal": 3, "Protect": 3, "Slow": 3, "Fireball": 2, "Lightning": 2}
                self.items = {"Mega_Healing_Potion": 3, "Grenade": 4}
            case _:
                print("Error, incorrect title")
                print(self.title)
                exit()

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()

class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.weapon = Weapon()
        self.magic = {}
        self.ai_type = []
        self.monster_type = ""

    def randomEnemy(self):
        enemy_list = ["Orc", "Wrym", "Hobgoblin", "Troll", "Wolf", "Ogre", "Werewolf", "Shark", "Ghost", "Lich", "Death Eye", "Hydra", "Elemental"]
        rand_enemy = choice(enemy_list)
        match rand_enemy:
            case "Orc":
                self.title = "Orc"
                self.monster_type = "Basic"                
                self.health = 150
                self.speed = 20
                self.magic_proficiency = 0
                self.items = {"Small_Healing_Potion": 5, "Mega_Healing_Potion": 1, "Stick": 5}
                self.weapon = Weapon().assign("Sword")
                self.ai_type = ["Agressive", "Weapon"]
            case "Wrym":
                self.title = "Wrym"
                self.monster_type = "Flying"                    
                self.health = 450
                self.defense = 20
                self.speed = 60
                self.magic_proficiency = 20
                self.magic = {"Fireball": 30, "Lightning": 30, "Nuke": 3, "Stop": 2, "Slow": 2, "Mute": 2, "Break": 2, "Scar": 4}
                self.items = {"Small_Healing_Potion": 2, "Antidote": 2}          
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
                self.weapon = Weapon().assign("Spear")
                self.ai_type = ["Agressive", "Mixed"]
            case "Troll":
                self.title = "Troll"
                self.monster_type = "Basic"                    
                self.health = 300
                self.defense = 40
                self.speed = 0
                self.magic_proficiency = 0
                self.items = {"Stick": 100}
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
                self.items = {"Small_Healing_Potion": 5, "Antidote": 4}        
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
                self.magic = {"Instant_Death": 100}      
                self.weapon = Weapon().assign("Fists")
                self.ai_type = ["Agressive", "Weapon"]
            case "Werewolf":
                self.title = "Werewolf"
                self.monster_type = "Basic"                    
                self.health = 200     
                self.defense = 10
                self.speed = 30
                self.magic_proficiency = 10
                self.magic = {"Cure": 10, "Heal": 10, "Protect": 2, "Fast": 2, "Lightning": 10, "Slow": 1, "Mute": 1, "Scar": 1}
                self.items = {"Small_Healing_Potion": 10, "Mega_Healing_Potion": 1, "Antidote": 5, "Stick": 4}
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
                self.magic = {"Mute": 3}
                self.items = {"Antidote": 2}   
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
                self.magic = {"Heal": 3, "Fireball": 10, "Stop": 2, "Slow": 2, "Mute": 2}         
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
                self.items = {"Small_Healing_Potion": 10}
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
                self.items = {"Heal": 10}
                self.weapon.weapon_type = "Haunting"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80     
                self.ai_type = ["Cautious", "Magic"]
            case "Hydra":
                self.title = "Hydra"
                self.monster_type = "Flying"                
                self.health = 100
                self.defense = 20
                self.speed = 50
                self.magic_proficiency = 0
                self.magic = {"Fireball": 10, "Lightning": 10, "Nuke": 3}           
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
                self.items = {"Antidote": 3, "Small_Healing_Potion":5}             
                self.weapon.weapon_type = "Spirit Swipe"
                self.weapon.dmg = 15               
                self.weapon.crit_chance = 90
                self.weapon.accuracy = 80   
                self.ai_type = ["Cautious", "Mixed"]

    def ai_action(self) -> str:
        attack = False
        action_choice = ""
        has_negative_status = False
        for i in range(len(self.status)):
            if self.status[i].isgood == False:
                has_negative_status = True
                break
        if self.ai_type[0] == "Agressive":
            if self.health >= int(0.6 * self.max_health):
                attack = True
            elif self.health <= int(0.1 * self.max_health):
                attack = False
            elif (self.health <= int(0.25 * self.max_health)) and has_negative_status:
                attack = False
                if "Antidote" in self.items.keys():
                    action_choice = "Item Antidote"
                    return action_choice
                elif "Cure" in self.magic.keys():
                    action_choice = "Magic Cure"
                    return action_choice
            else:
                attack_val = randint(0,100)
                if 80 > attack_val:
                    attack = True            
        elif self.ai_type[0] == "Cautious": #more focused on item usage
            if self.health >= int(0.8 * self.max_health):
                attack = True
            elif self.health <= int(0.2 * self.max_health):
                attack = False
            elif (self.health <= int(0.5 * self.max_health)) and has_negative_status:
                attack = False                
                if "Cure" in self.magic.keys():
                    action_choice = "Magic Cure"
                    return action_choice          
                elif "Antidote" in self.items.keys():
                    action_choice = "Item Antidote"
                    return action_choice
            else:
                attack_val = randint(0,100)
                if 50 > attack_val:
                    attack = True
        else:
            print("should not happen. ai_type needs to be Cautious or Agressive")
            exit()                    
        #attack should be set now
        if attack == True:
            rand_val = randint(0,100)
            magic_list = list(self.magic.keys())
            if "Heal" in magic_list:
                magic_list.remove("Heal")
            if "Cure" in magic_list:
                magic_list.remove("Cure")
            if (self.ai_type[1] == "Magic") and (len(magic_list)>0) and rand_val>20:
                action_choice = "Magic " + choice(magic_list)
            elif (self.ai_type[1] == "Mixed") and (len(magic_list)>0) and rand_val>50:
                action_choice = "Magic " + choice(magic_list)
            elif (self.ai_type[1] == "Weapon") and (len(magic_list)>0) and rand_val>80:
                action_choice = "Magic " + choice(magic_list)
            else:
                action_choice = "Weapon"
        else:
            heal_options = []
            if "Heal" in self.magic.keys():
                if self.magic["Heal"] > 0:
                    heal_options.append("HealMagic")
            if "Mega" in self.items.keys():
                if self.items["Mega_Healing_Potion"] > 0:
                    heal_options.append("Mega_Healing_Potion")
            if "Small" in self.items.keys():
                if self.items["Small_Healing_Potion"] > 0:
                    heal_options.append("Small_Healing_Potion")
            if len(heal_options) > 0:
                if self.ai_type[1] == "Magic" and heal_options == "HealMagic":
                    action_choice = "Magic Heal"
                else:
                    action_choice = choice(heal_options)
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
                    action_choice = "Weapon"
        return action_choice

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()

class Magic:
    """Class of functions for all magic spells
    """
    #defensive
    def Cure(self, caster: Person) -> bool:
        #removes bad status effects
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 50):
            positive_effects: list[Status] = []  
            for i in range(len(caster.status)):
                if caster.status[i].isgood == True:
                    positive_effects.append(caster.status[i])
            caster.status.clear()
            if len(positive_effects) > 0:
                caster.status.extend(positive_effects)
            print(f"{caster.title} Cured all negative effects!")
            return True
        else:
            print(f"{caster.title}'s Cure Failed")
            return False

    def Heal(self, caster: Person) -> bool:
        #heals user by 20% of max health. 100% chance of success
        cur_health = caster.health
        caster.health += int(caster.max_health * 0.2)
        if caster.health > caster.max_health:
            caster.health = caster.max_health
        delta_health = caster.health - cur_health
        print(f"{caster.title} gained {delta_health} health!")
        return True

    def Protect(self, caster: Person) -> bool:
        #raises defense
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 80):
            caster.status.append(Status("Protect", True, duration=2, chance_to_remove=0))
            print(f"{caster.title}'s defense rose by 20!")
            return True
        else:
            print(f"{caster.title}'s Protect failed")
            return False

    def Fast(self, caster: Person) -> bool:
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
        #fireball. small chance to inflict burn
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 65):
            damage = randint(40,60) - opponent.defense
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
        #lightning. chance to inflict paralysis
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 55):
            opponent_damage = randint(40,60) - opponent.defense
            opponent.health -= opponent_damage
            print(f"{opponent.title} lost {opponent_damage} health!")            
            success_val = randint(0,100)
            if success_val <= (20 - opponent.magic_proficiency):
                opponent.status.append(Status("Paralysis",False,duration=2,chance_to_remove=35))
                print(f"{opponent.title} got afflicted with Paralysis for 2 turns! They wont be able to use weapons til this expires!")

            return True
        else:
            print(f"{caster.title}'s Lightning spell missed!")
            return False

    def Nuke(self, caster: Person, opponent: Person) -> bool:
        #high damage, hits caster aswell. Low number of uses
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 75):
            opponet_damage = randint(100,150) - opponent.defense
            opponent.health -= opponet_damage
            print(f"{opponent.title} lost {opponet_damage} health!")
            caster_damage = randint(50,100) - opponent.defense
            caster.health -= caster_damage
            print(f"{caster.title} got hit by the shockwave!")
            print(f"{caster.title} lost {caster_damage} health!")
            return True
        else:
            print(f"{caster.title}'s Nuke missed! How does that even happen?!?")
            caster.health -= 5
            print(f"{caster.title} lost 5hp just from the shock of being that bad!")
            return False

    #offensive status effects
    def Poison(self, caster: Person, opponent: Person) -> bool:
        #posion. high chance to inflict poison
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 70):
            opponent.status.append(Status("Poison", False, duration=6))
            print(f"{opponent.title} got aflicted with Poison! They will lost 5%hp per turn til it expires!")
            return True
        else:
            print(f"{caster.title}'s Poison spell missed!")
            return False

    def Instant_Death(self, caster: Person, opponent: Person) -> bool:
        #chance to make an opponent die instantly. very low chance
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 5):
            opponent.health = -100
            print(f"{opponent.title} Died")
            return True
        else:
            print(f"{caster.title}'s Instant Death spell missed!")
            return False

    def Stop(self, caster: Person, opponent: Person) -> bool:
        #chance to make opponent lose a turn
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 15):
            opponent.status.append(Status("Stop", False, duration=2))
            print(f"{opponent.title} got Stopped! They will not be able to make a move until this expires!")
            return True
        else:
            print(f"{caster.title}'s Stop spell missed!")
            return False

    def Slow(self, caster: Person, opponent: Person) -> bool:
        #lowers opponent's speed
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 85):
            opponent.status.append(Status("Slow", False, duration=1, chance_to_remove=10))
            print(f"{opponent.title} got slowed! They lost 30 speed!")
            return True
        else:
            print(f"{caster.title}'s Slow spell missed!")
            return False

    def Mute(self, caster: Person, opponent: Person) -> bool:
        #chance to make opponent not able to cast spells
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 65):
            opponent.status.append(Status("Mute", False, duration=1))
            print(f"{opponent.title} got muted! They cannot cast spells till this runs out!")
            return True
        else:
            print(f"{caster.title}'s Slow spell missed!")
            return False

    def Break(self, caster: Enemy, opponent: Player) -> bool:
        #chance to break items in player inventory - enemy specific
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency + 50):
            if len(opponent.items) == 0:
                print(f"{opponent.title} is all out of items. Theres none to break!\n\n-- you got luck this time --\n")
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
        #chance to lower opponent max health by 7.5%
        success_val = randint(0,100)
        if success_val <= (caster.magic_proficiency * 2 + 30):
            opponent.max_health -= int(opponent.max_health * 0.05)
            if opponent.health > opponent.max_health:
                opponent.health = opponent.max_health
            print(f"{opponent.title} got Scarred! They permantly lost 5% of their max health")
            return True
        else:
            print(f"{caster.title}'s Scar spell missed!")
            return False        

class Items:
    """Item Functions
    """
    def Small_Healing_Potion(self, caster: Person) -> bool:
        cur_health = caster.health
        caster.health += int(caster.max_health * 0.3)
        if caster.health > caster.max_health:
            caster.health = caster.max_health
        delta_health = caster.health - cur_health
        print(f"{caster.title} gained {delta_health} health!")
        return True

    def Mega_Healing_Potion(self, caster: Person):
        cur_health = caster.health
        caster.health += int(caster.max_health * 0.6)
        if caster.health > caster.max_health:
            caster.health = caster.max_health
        delta_health = caster.health - cur_health
        print(f"{caster.title} gained {delta_health} health!")
        return True

    def Antidote(self, caster: Person) -> bool:
        positive_effects: list[Status] = []  
        for i in range(len(caster.status)):
            if caster.status[i].isgood == True:
                positive_effects.append(caster.status[i])
        caster.status.clear()
        if len(positive_effects) > 0:
            caster.status.extend(positive_effects)
        print(f"{caster.title}'s Antidote all negative effects!")
        return True

    def Grenade(self, caster: Person, opponent: Person) -> bool:
        success_val = randint(0,100)
        if success_val <= 90:
            damage = randint(40,60) - opponent.defense
            opponent.health -= damage
            print(f"{opponent.title} lost {damage} health!")            
            return True
        else:
            print(f"{caster.title}'s grenade missed!")
            return False

    def Stick(self, caster: Person, opponent: Person) -> bool:
        success_val = randint(0,100)
        title_boost = 0
        if caster.title == "Toddler":
            title_boost = 30
        if success_val <= 5 + title_boost:
            damage = randint(140,160) - opponent.defense
            opponent.health -= damage
            print(f"{opponent.title} got prodded massively, and lost {damage} health!")            
            return True
        else:
            print(f"{caster.title}'s prodding has slightly annoyed {opponent.title}.")
            return False

class MainGame:
    """Main game object
    """
    def __init__(self) -> None:
        self.character = ""
        self.weapon = Weapon()
        self.player: Player
        self.enemy: Enemy = Enemy()
        self.menu_screen()
        self.exit_game(noexit=True)

    def action_select(self, person: Player, opponent: Player, action: str) -> None:
        pass

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
        self.player: Player = Player(self.character, self.weapon)
        print(self.player)
        self.enemy.randomEnemy()
        del self.character
        del self.weapon
        print("\nYour opponent is...")
        print(self.enemy)
        self.game()
 
    def game(self) -> None:
        #main game loop

        while True:

            #get turn order
            first_player = ""
            if self.player.speed < self.enemy.speed:
                first_player = "Enemy"
            elif self.player.speed == self.enemy.speed:
                first_player = choice(["Player", "Enemy"])
            else:
                first_player = "Player"

            #print user options            
            has_magic = False
            has_items = False
            if len(self.player.magic)>0:
                if any(self.player.magic.values()):
                    has_magic = True
            if len(self.player.items)>0:
                if any(self.player.items.values()):
                    has_items = True        
            user_options = ["Attack", "Use Magic", "Use Item"]                                
            if has_items == False:
                user_options.pop(2)
            if has_magic == False:
                user_options.pop(1)
            for idx, string in enumerate(user_options):
                print(idx, "|" + string)
            acceptable_input_nums = []
            for i in range(len(user_options)):
                acceptable_input_nums.append(i+1)
            print_str_nums = ", ".join(acceptable_input_nums)
            option_chose = ""
            #get user selection            
            while True:
                try:
                    user_input = input(f"Pick the option corresponding to the numbers: {print_str_nums}")
                    if not(user_input.isnumeric()):
                        raise ValueError
                    elif int(user_input) not in acceptable_input_nums:
                        raise ValueError
                    else:
                        option_chose = user_options[int(user_input)-1]
                        if option_chose.startswith("Use "):
                            option_chose = option_chose[3:]
                        break
                except ValueError:
                    print("Invalid Input.")
            item_chose = ""
            magic_chose = ""    
            if option_chose == "Attack":
                test= ""
            elif option_chose ==  "Use Item":
                user_options = self.player.items
                for idx, (key, value) in enumerate(user_options):
                    print(idx, "|" + key, value)
                acceptable_input_nums = []
                for i in range(len(user_options)):
                    acceptable_input_nums.append(i+1)
                print_str_nums = ", ".join(acceptable_input_nums)
                #get user selection            
                while True:
                    try:
                        user_input = input(f"Pick the option corresponding to the numbers: {print_str_nums}")
                        if not(user_input.isnumeric()):
                            raise ValueError
                        elif int(user_input) not in acceptable_input_nums:
                            raise ValueError
                        else:
                            item_chose = list(user_options.keys())[int(user_input)-1]
                            self.player.items[item_chose] -= 1
                            break
                    except ValueError:
                        print("Invalid Input.")       
            elif option_chose == "Use Magic":
                user_options = self.player.magic
                for idx, (key, value) in enumerate(user_options):
                    print(idx, "|" + key, value)
                acceptable_input_nums = []
                for i in range(len(user_options)):
                    acceptable_input_nums.append(i+1)
                print_str_nums = ", ".join(acceptable_input_nums)
                #get user selection            
                while True:
                    try:
                        user_input = input(f"Pick the option corresponding to the numbers: {print_str_nums}")
                        if not(user_input.isnumeric()):
                            raise ValueError
                        elif int(user_input) not in acceptable_input_nums:
                            raise ValueError
                        else:
                            magic_chose = list(user_options.keys())[int(user_input)-1]
                            break
                    except ValueError:
                        print("Invalid Input.")
            else:
                print("option chose error")
                print(option_chose)
                exit() 

            player_choice = option_chose + " " + item_chose + magic_chose
            ai_choice = self.enemy.ai_action()

            if first_player == "Player":
                #1st attack
                self.action_select(self.player, self.enemy, player_choice) #action needs to be done!!!!!!
                #effects -> check for winner

                #2nd attack
                self.action_select(self.enemy, self.player, ai_choice)
                #effects -> check for winner
            elif first_player == "Enemy":
                #1st attack
                self.action_select(self.enemy, self.player, ai_choice)    
                #effects -> check for winner 

                #2nd attack
                self.action_select(self.player, self.enemy, player_choice)                   
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
        