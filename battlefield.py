from fleet import Fleet
from herd import Herd 
import random 

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.turn = 1
        self.user_turn = 1
        self.opponent_turn = 0
        self.opponent_select = 0
        self.user_team = None
        self.opponent_team = None
        self.user_attacker = None
        self.user_defender = None
        self.opponent_attacker = None
        self.opponent_defender = None

    def run_game(self):
        self.display_welcome()
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.user_choice = input("pick a team, enter 1 for Dinosaurs, Enter 2 for Robots")
        while(self.user_choice != '1') & (self.user_choice != "2"):
            self.user_choice = input("Enter a 1 or 2")
        if(self.user_choice == '1'):
            self.user_team = self.herd.dinosaurs
            self.user_opponent = self.fleet.robot
        elif(self.user_choice == '2'):
            self.user_team = self.fleet.robot
            self.user_opponent = self.herd.dinosaurs

    def display_welcome(self):
        print("Welcome to the battle field, Dinosaurs vs Robots!!")
        
    def battle(self):
        while()

        pass

       

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    #def show_dino_oppenent_options(self):
        pass

    #def show_robo_oppenent_options(self):
        pass

    def display_winners(self):

        pass