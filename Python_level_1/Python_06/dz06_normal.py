# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.level = 1
        self.experience = 0
        self.next_level_expirience = 100

    def _increase_level(self):
        self.level += 1

    def add_experience(self, count):
        self.experience += count
        if self.experience >= self.next_level_expirience:
            self._increase_level()
            self.next_level_expirience *= 2

    def _calc_damage(self, who_attack, who_defend): #должна быть инкапсулирована!!!
        return who_attack.damage // who_defend.armor

    def attack(self, who_attack, who_defend):
        who_defend.health -= self._calc_damage(who_attack, who_defend)

    def say(self):
        print('Hi!')

class Player(Person):
    def say(self):
        print('Hi, wild enemy!')

class Enemy(Person):

    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)
        self.level = 3

    def say(self):
        print('Grrr! Run, Vasya, run!')

player1 = Player('White_Knight_Vasya', 1000, 777, 50)
print(player1.name, player1.level, player1.health, player1.damage, player1.armor, player1.experience)
player1.say()

player2 = Enemy('Worm_ZukuZuku', 1500, 2450, 10)
print(player2.name, player2.level, player2.health, player2.damage, player2.armor, player2.experience)
player2.say()

attacker = player1

while player1.health > 0 and player2.health > 0:
    if attacker == player1:
        player1.attack(player1, player2)
        attacker = player2
        if player2.health > 0:
            print('{} нанёс {} урона {}, у того осталось {} здоровья.'.format(player1.name, player2.name,
                                                                            player1._calc_damage(player1, player2),
                                                                            player2.health))
        else:
            print('{} нанёс {} урона {}, у того осталось не осталось здоровья.'.format(player1.name, player2.name,
                                                                            player1._calc_damage(player1, player2)))
    else:
        player2.attack(player2, player1)
        attacker = player1
        if player1.health > 0:
            print('{} нанёс {} урона {}, у того осталось {} здоровья.'.format(player2.name, player1.name,
                                                                              player2._calc_damage(player2, player1),
                                                                              player1.health))
        else:
            print('{} нанёс {} урона {}, у того осталось не осталось здоровья.'.format(player2.name, player1.name,
                                                                                       player2._calc_damage(player2, player1)))
if player1.health > 0:
    print(player1.name, ' одержал победу в битве!')
else:
    print(player2.name, ' одержал победу...')
