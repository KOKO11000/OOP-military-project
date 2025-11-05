from abc import ABC, abstractmethod
from strike_options import *
class Weapon:
    total_weapons = 0
    def __init__(self, name: str, ammo: int):
        self.name = name
        self.ammo = ammo
        total_weapons += 1
    
class Soldier:
    def __init__(self, name: str, rank: str, weapon: Weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon
    def report(self):
        print(f"name: {self.name}, \nrank: {self.rank},\nweapom: {self.weapon}")
    
class Unit:
    def __init__(self, unit_name: str, commander: Soldier,soldiers: list[Soldier], strike_option):
        self.unit_name = unit_name
        self.commander = commander
        self.soldiers = soldiers
        self.strike_option = strike_option

    def briefing(self):
        print(f"{self.unit_name}, {self.commander.report()}")




