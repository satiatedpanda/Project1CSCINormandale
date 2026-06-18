from random import choice, random

class enemy:
    def __init__(self, name): 
        enemy_dict: dict = {
            "brute" : [50, 70],
            "worlock" : [40, 80],
            "joker" : [30, 90]
        }
        self.name = name
        self.dmg = enemy_dict[name][0]
        self.health = enemy_dict[name][1]
enemy_list: list[str] = ["brute", "worlock", "joker"]
curr_enemy = random.choice(enemy_list)
enemy(curr_enemy)
