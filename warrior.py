from character import Character

class Warrior(Character):
    def __init__(self, name, level):
        super().__init__(name, level)
        self._job = "戦士"
        self._k_atk = 20
        self._k_def = 5