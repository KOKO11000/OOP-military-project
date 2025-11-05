from military_simulation import *
from abc import ABC, abstractmethod

class StrikeOption(ABC):
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
    
    @abstractmethod
    def strike(self):
        pass

class Tank(StrikeOption):
    def strike(self):
        print("This Tank can shoot shells")
    
class Drone(StrikeOption):
    def strike(self):
        print("This weapon can fly attack")

tank = Tank("tank1", 1)
test_tank = tank.strike() 
