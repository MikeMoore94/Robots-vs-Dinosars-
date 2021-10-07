from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robot = []
        self.create_fleet()
    
    def create_fleet(self):
        terminator = Robot("Terminator", "gun", 15)
        cowboy = Robot("cowboy", "whip", 10)
        r2d2 = Robot("R2-D2", "stunner", 5)
        self.robot.append(terminator)
        self.robot.append(cowboy)
        self.robot.append(r2d2)

    

    


        

  