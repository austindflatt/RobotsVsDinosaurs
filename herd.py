import herd as Herd

import dinosaur
from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dino_herd = []

    def create_herd(self):
        dino1 = dinosaur.Dinosaur('Theropods', 100, 125, 75)
        dino2 = dinosaur.Dinosaur('Spinosaurus', 100, 100, 70,)
        dino3 = dinosaur.Dinosaur('T-Rex', 90, 125, 65)
        self.dino_herd.append(dino1, dino2, dino3)
        print(self.dino_herd)