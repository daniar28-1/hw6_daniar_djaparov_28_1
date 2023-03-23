import random
from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    STUN_BOSS = 5
    ACCEPT_DAMAGE = 6
    RECALL_HERO = 7

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value >= 0:
            self.__health = value
        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = random.choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if isinstance(ability, SuperAbility):
            self.__ability = ability
        else:
            raise ValueError('Wrong data type for ability')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = random.randint(2, 5)  # 2,3,4,5
        boss.health -= self.damage * coefficient
        print(f'Warrior hits critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_point = random.randint(2, 5)
        print(f'Magic gave boost for {boost_point}')
        for hero in heroes:
            if hero.health >= 0:
                hero.damage += boost_point


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes):
        if self.health >= 0:
            self.__blocked_damage += boss.damage
            print(f'Berserk save damage and revert {self.__blocked_damage}')
            self.damage += self.__blocked_damage
            boss.health -= self.damage

class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUN_BOSS)


    def apply_super_power(self, boss, heroes):
        stun = [1,2,3,4,5]
        stunned = random.choice(stun)
        if stunned == 2:
            boss.damage = 0
        else:
            boss.damage = 50

class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,SuperAbility.ACCEPT_DAMAGE)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            protection = boss.damage // 5
            hero.health += protection

class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.RECALL_HERO)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0:
                hero.health += self.health
                self.health = 0
round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} ------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.ability and hero.health > 0:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start():
    boss = Boss('Rashan', 450, 50)

    warrior = Warrior('Ahiles', 280, 10)
    doc = Medic('Estes', 250, 5, 15)
    magic = Magic('Merlin', 270, 15)
    berserk = Berserk('Thamus', 260, 10)
    assistant = Medic('Aibolit', 290, 5, 5)
    thor = Thor('Tor', 250, 15)
    galem = Golem('Loit', 400, 5)
    witcher = Witcher('lia', 250, 0 )
    heroes_list = [warrior, doc, magic, berserk, assistant, thor, galem, witcher]

    show_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start()
