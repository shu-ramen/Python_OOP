from character import Character

class Hero(Character):
    def __init__(self, name, level):
        super().__init__(name, level)
        self._job = "勇者"
        self._k_atk = 30
        self._k_def = 20
    
    def super_attack(self, enemy):
        print("{0:s}の 必殺技!!".format(self._name))
        damage = self.ATK * 2 - enemy.DEF
        enemy.hit(damage)