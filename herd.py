from dinosaurs import Dinosaurs 

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    def create_herd(self):
        trex = Dinosaurs("T-rex")
        raptor = Dinosaurs("Raptor")
        triceratops = Dinosaurs("Triceratop")

        self.dinosaurs.append(trex)
        self.dinosaurs.append(raptor)
        self.dinosaurs.append(triceratops)

        

    


