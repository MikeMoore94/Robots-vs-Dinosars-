from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robot = []
        self.create_fleet()
    
    def create_fleet(self):
        terminator = Robot("Terminator")
        cowboy = Robot("cowboy")
        r2d2 = Robot("R2-D2")
        self.robot.append(terminator)
        self.robot.append(cowboy)
        self.robot.append(r2d2)

    

    


        

  