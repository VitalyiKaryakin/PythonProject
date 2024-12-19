# This is a sample Python script.


import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        print(f'{self.name} атакует {other.name}!')
        other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(
            f'{self.name} получает {damage} урона! '
            f'Осталось здоровья: {self.health}'
        )

    def is_alive(self):
        return self.health > 0


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

    def special_attack(self, other):
        damage = random.randint(5, self.attack_power * 2)
        print(f'{self.name} проводит специальную атаку на {other.name}!')
        other.take_damage(damage)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack_power=15)

    def cast_spell(self, other):
        damage = random.randint(10, self.attack_power * 2)
        print(f'{self.name} накладывает заклинание на {other.name}!')
        other.take_damage(damage)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=18)

    def shoot_arrow(self, other):
        damage = random.randint(8, self.attack_power * 2)
        print(f'{self.name} стреляет стрелой в {other.name}!')
        other.take_damage(damage)


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=15)

    def divine_strike(self, other):
        damage = random.randint(10, self.attack_power * 2)
        print(f'{self.name} наносит божественный удар по {other.name}!')
        other.take_damage(damage)
        self.health += 5  # Восстанавливает немного здоровья


def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
        action = random.choice(['attack', 'spec_attack'])

        if isinstance(character1, Warrior) and action == 'spec_attack':
            character1.special_attack(character2)
        elif isinstance(character1, Mage) and action == 'spec_attack':
            character1.cast_spell(character2)
        elif isinstance(character1, Archer) and action == 'spec_attack':
            character1.shoot_arrow(character2)
        elif isinstance(character1, Paladin) and action == 'spec_attack':
            character1.divine_strike(character2)
        else:
            character1.attack(character2)

        if not character2.is_alive():
            print(f'{character2.name} побежден! Вы победили!')
            break

        action = random.choice(['attack', 'spec_attack'])

        if isinstance(character2, Warrior) and action == 'spec_attack':
            character2.special_attack(character1)
        elif isinstance(character2, Mage) and action == 'spec_attack':
            character2.cast_spell(character1)
        elif isinstance(character2, Archer) and action == 'spec_attack':
            character2.shoot_arrow(character1)
        elif isinstance(character2, Paladin) and action == 'spec_attack':
            character2.divine_strike(character1)
        else:
            character2.attack(character1)

        if not character1.is_alive():
            print(f'{character1.name} побежден! Вы проиграли...')
            break


def main():
    print('Добро пожаловать в игру Герои!')
    player_name = input('Введите имя вашего героя: \n')

    choice = input('Выберите класс (воин / маг / лучник / паладин): ').lower()
    if choice == 'воин':
        player = Warrior(player_name)
    elif choice == 'маг':
        player = Mage(player_name)
    elif choice == 'лучник':
        player = Archer(player_name)
    elif choice == 'паладин':
        player = Paladin(player_name)
    else:
        print('Некорректный выбор. Создается воин по умолчанию!')
        player = Warrior(player_name)

    enemies = [
        Warrior('Дракон'),
        Mage('Темный маг'),
        Archer('Ловкий лучник'),
        Paladin('Святой паладин')
    ]

    enemy = random.choice(enemies)

    print(f'\n{player.name} начинает бой с {enemy.name}')
    battle(player, enemy)


main()



# import random
#
# class Character:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
#
#     def attack(self, other):
#         damage = random.randint(1, self.attack_power)
#         print(f'{self.name} атакует {other.name} !')
#         other.take_damage(damage)
#
#     def take_damage(self, damage):
#         self.health -= damage
#         print(
#             f'{self.name} получает {damage} урона! '
#             f'Осталось здоровья: {self.health}'
#         )
#
#     def is_alive(self):
#         return self.health > 0
#
#
# class Warrior(Character):
#     def __init__(self, name):
#         super().__init__(name, health=100, attack_power=20)
#
#     def special_attack(self, other):
#         damage = random.randint(5, self.attack_power * 2)
#         print(f'{self.name} проводит специальную атаку на {other.name}!')
#         other.take_damage(damage)
#
# class Mage(Character):
#     def __init__(self, name):
#         super().__init__(name, health=70, attack_power=15)
#
#     def cast_spell(self, other):
#         damage = random.randint(10, self.attack_power * 2)
#         print(f'{self.name} накладывает заклинание на {other.name}!')
#         other.take_damage(damage)
#
#
# def battle(character1, character2):
#     while character1.is_alive() and character2.is_alive():
#         action = random.choice(['attack', 'spec_attack'])
#
#         if isinstance(character1, Warrior) and action == 'spec_attack':
#             character1.special_attack(character2)
#         else:
#             character1.attack(character2)
#
#         if not character2.is_alive():
#             print(f'{character2.name} побежден! Вы победили!')
#             break
#
#         action = random.choice(['attack', 'spec_attack'])
#
#         if isinstance(character2, Warrior) and action == 'spec_attack':
#             character2.special_attack(character1)
#         else:
#             character2.attack(character1)
#
#         if not character1.is_alive():
#             print(f'{character1.name} побежден! Вы проиграли...')
#             break
#
#
# def main():
#     print('Добро пожаловать в игру Герои!')
#     player_name = input('Введите имя вашего героя: \n')
#
#     choice = input('Выберите класс (воин / маг): ').lower()
#     if choice == 'воин':
#         player = Warrior(player_name)
#     elif choice == 'маг':
#         player = Mage(player_name)
#     else:
#         print('Некорректный выбор. Создается воин по умолчанию!')
#         player = Warrior(player_name)
#
#     enemy = Warrior('Дракон')
#
#     print(f'\n{player.name} начинает бой с {enemy.name}')
#     battle(player, enemy)
#
#
# main()