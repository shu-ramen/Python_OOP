from character import Character
from warrior import Warrior
from hero import Hero

if __name__ == "__main__":
    taro = Character("太郎", 10)
    jiro = Warrior("次郎", 20)
    goro = Hero("五郎", 30)

    taro.attack(jiro)
    jiro.attack(taro)
    taro.attack(jiro)
    jiro.attack(taro)
    goro.attack(jiro)
    jiro.attack(goro)
    goro.super_attack(jiro)