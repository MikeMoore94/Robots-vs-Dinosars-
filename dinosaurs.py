class Dinosaurs:
    def __init__(self, dino_name):
        self.dino_name = dino_name 
        self.health = 100
        self.attack_power = 80
        self.attack = "roar"


    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.dino_name} attack {robot} for {self.attack_power}. Your new health is {robot.health}")

    def __init__(self):
        return self.dino_name 