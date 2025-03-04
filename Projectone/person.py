from weapon import Sword

class Person:
    def __init__(self, name: str, health: int = 100, armor: int = 50):
        self.name = name
        self.health = health
        self.armor = armor
    
    def introduce(self):
        return f"Hello, my name is {self.name}."
    
    def take_damage(self, damage: int):
        absorbed = min(self.armor, damage)
        self.armor -= absorbed
        self.health -= (damage - absorbed)
        return f"{self.name} took {damage - absorbed} damage, armor absorbed {absorbed}. Health: {self.health}, Armor: {self.armor}"
    
    def heal(self, amount: int):
        self.health += amount
        return f"{self.name} healed by {amount}. Current health: {self.health}" 


class Knight(Person):
    def __init__(self, name: str):
        super().__init__(name, health=120, armor=70)
        self.weapon = Sword()
    
    def attack(self):
        return f"{self.name} attacks! {self.weapon.attack()}"