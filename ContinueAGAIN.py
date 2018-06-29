import random

class Enemy:
    Hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh


    def getAtk(self):
        print("Attack is", self.atkl)        # need to reference the class then ...


    def getHp(self):
        print(self.Hp)

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()


enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()


#
# playerhp = 260
# enemyatkl = 60
# enemyatkh = 80
#
# while playerhp > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp = playerhp - dmg
#
#     if playerhp <= 30:
#         playerhp = 30
#
#     print("Enemy strikes for", dmg, "points of damage.  Current HP is", playerhp)
#
#     if playerhp > 30:
#         continue
#
#     print("Your health is low.  You've been teleported to the nearest inn.")
#     break
#
