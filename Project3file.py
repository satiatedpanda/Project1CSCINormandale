
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
    



class Weapon: 
    def __init__(self, weapon_type = 0): 
        self.dmg = 30 
        self.accuracy = 90 
        self.crit_chance = 10
        
        if weapon_type == "Sword":
            self.dmg = 30    
            self.accuracy = 90
            self.crit_chance = 10
    
        if weapon_type == "Spear":
            self.dmg = 40    
            self.accuracy = 80
            self.crit_chance = 20
    

        if weapon_type == "Axe":
            self.dmg = 50    
            self.accuracy = 80
            self.crit_chance = 30
    

        if weapon_type == "Tome":
            self.dmg = 30    
            self.accuracy = 50
            self.crit_chance = 50
    

        if weapon_type == "Spatula":
            self.dmg = 35   
            self.accuracy = 85
            self.crit_chance = 10
    
        if weapon_type == "Blankie":
            self.dmg = 10    
            self.accuracy = 100
            self.crit_chance = 1

        else: 
            self.dmg = 20    
            self.accuracy = 100
            self.crit_chance = 20
    
    

    def selected_character(self): 
         pass
if __name__ == "__main__": 

    
   
