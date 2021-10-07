from weapon import Weapon

class Robot:

    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.power = 70
        self.health = 100
        self.weapon = Weapon()
        
    def robot_attributes(self):
        print(f"Robots name is {self.robot_name} my health is at {self.health} my power level is {self.power} and the weapon im taking is {self.weapon}")

    def attack(self, dinosaurs):
        dinosaurs.health -= self.weapon_power
        print(f"{self.robot_name} attacks {dinosaurs.name} for {self.weapon_power}. Your health is at {dinosaurs.health}")

    
    
    
