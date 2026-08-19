class Character:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self.__hp = max_hp

def take_damage(self, amount: int) -> None:
    self.__hp -= amount
    if self.__hp < 0:
        self.__hp = 0

def heal(self, amount: int) -> None:
    self.__hp += amount
    if self.__hp > self.max_hp:
        self.__hp = self.max_hp

def is_alive(self) -> bool:
    return self.hp > 0