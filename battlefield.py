from fleet import Fleet
from herd import Herd 

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def display_welcome(self):
        print("Welcome to the battle of Robots VS Dinosaurs")

    def run_game(self):
        self.display_welcome()
        self.dino_turn()
        self.robo_turn()
        self.battle()

    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robot) > 0:
            self.show.dino_options()
            self.show.robot_option()

    def dino_turn(self):
        print("Choose the Dinosaur you want send into battle")
        self.show_dino_options()
        chosen_dino = int(input())
        print("Choose Robot you want to fight the Dinosaur")
        self.show_robot_options()
        chosen_robot = int(input())
        self.herd.dinosaurs[chosen_dino].attack(self.fleet.robot[chosen_robot])
        if self.fleet.robot[chosen_robot].health <= 0:
            print(f"{self.herd.dinosaurs[chosen_dino]} has fallen")
            self.herd.dinosaurs.remove(self.fleet.robot[chosen_robot])


    def robot_turn(self):
        print("Chosoe the Robot you want to send into battle")
        self.show_robot_options()
        chosen_robot = int(input())
        print("choose a Dinosaur you want to fight the Robot")
        self.show_dino_options()
        chosen_dino = int(input())
        self.fleet.robot[chosen_robot].attack(self.herd.dinosaurs[chosen_dino])
        if self.herd.dinosaurs[chosen_dino].health <= 0: 
            print(f"{self.fleet.robot[chosen_robot]} has fallen")
            self.fleet.robot.remove(self.herd.dinosaurs[chosen_dino])


    def show_dino_options(self):
        dino_index = 0 
        for dino in self.herd.dinosaurs:
            print(f"press {dino_index} for {dino.dino_name}")
            dino_index += 1 

    def show_robot_options(self):
        robot_index = 0
        for robot in self.fleet.robot:
            print(f"Press {robot_index} for {robot.robot_name}")
            robot_index += 1

    def display_winner(self):
        print("Congratulations we have found a winner")
        if len(self.fleet.robot) > 0:
            print("Robots are the Winners")
        else:
            print("Dinosaurs are the")
