class Character(object):
    def __init__(self, name, level):
        self._job = "一般人"
        self._name = name
        self._hp = level * 100
        self._pow = level * 1
        self._vit = level * 1
        self._k_atk = 10
        self._k_def = 10

    @property
    def ATK(self):
        return self._k_atk * self._pow

    @property
    def DEF(self):
        return self._k_def * self._vit
    
    @property
    def STATUS(self):
        return "{0:s}<{1:s}>: HP {2:d}  ATK {3:d}  DEF {4:d}".format(self._name, self._job, self._hp, self.ATK, self.DEF)

    def hit(self, damage):
        if damage > 0:
            print("{0:s} に {1:d} のダメージ!".format(self._name, damage))
            self._hp = self._hp - damage
            if self._hp <= 0:
                self._hp = 0
                print("{0:s} は殺された...".format(self._name))
            else:
                print(self.STATUS)
        else:
            print("{0:s} には効いていない...".format(self._name))
            print(self.STATUS)
        print()

    def attack(self, enemy):
        print("{0:s}の 攻撃!!".format(self._name))
        damage = self.ATK - enemy.DEF
        enemy.hit(damage)