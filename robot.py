from weapon import Weapon

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 0 
        self.weapon = Weapon()
        pass

    def robot_attack(self, dinosaur):
        pass