from weapon import Weapon

class Robot:

    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.power = 70
        self.health = 100
        self.weapon = "cannon"
        self.weapon_power = 47
        self.attack = "BOMB"

    def robot_attack(self, robot):
        robot.health -= self.weapon_power
        print(f"{self.robot_name} attacks {dino_name} for {self.weapon_power}. Your health is at {dinosaurs.health}")
        
    
