class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage
    
    def attack(self):
        return f"Attacking with {self.name}, dealing {self.damage} damage."


class Sword(Weapon):
    def __init__(self, name: str = "Sword", damage: int = 10):
        super().__init__(name, damage)
    
    def attack(self):
        return f"Swinging the {self.name}, slashing for {self.damage} damage!"