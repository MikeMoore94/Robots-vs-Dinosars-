class Dinosaurs:
    def __init__(self, dino_name):
        self.dino_name = dino_name 
        self.health = 100
        self.attack_power = 80
        self.attack_robot = "roar"
        

    def dino_attributes(self):
        print(f"I am a {self.dino_name}, with {self.health} points, and my attacking power is {self.attack_power}")


    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.dino_name} attack {robot} for {self.attack_power}. Your new health is {robot.health}")

    