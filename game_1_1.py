

import random
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def special_attack(self, other):
        pass

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        print(f'{self.name} атакует {other.name}!')
        other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} получает {damage} урона! Осталось здоровья: {self.health}')

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        print(f'{self.name} восстанавливает {amount} здоровья! Осталось здоровья: {self.health}')


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

    def special_attack(self, other):
        damage = random.randint(10, self.attack_power * 2)
        print(f'{self.name} накладывает заклинание на {other.name}!')
        other.take_damage(damage)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=18)

    def special_attack(self, other):
        damage = random.randint(8, self.attack_power * 2)
        print(f'{self.name} стреляет стрелой в {other.name}!')
        other.take_damage(damage)


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=15)

    def special_attack(self, other):
        damage = random.randint(10, self.attack_power * 2)
        print(f'{self.name} наносит божественный удар по {other.name}!')
        other.take_damage(damage)
        self.heal(5)  # Восстанавливает немного здоровья


class Item:
    def __init__(self, name, heal_amount):
        self.name = name
        self.heal_amount = heal_amount

    def use(self, character):
        character.heal(self.heal_amount)
        print(f'{character.name} использует {self.name} и восстанавливает {self.heal_amount} здоровья!')


def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
        action = input(f'Выберите действие для {character1.name} (1 - атаковать, 2 - специальная атака, 3 - использовать предмет): ')

        if action == '1':
            character1.attack(character2)
        elif action == '2':
            character1.special_attack(character2)
        elif action == '3':
            if character1.inventory:
                print("Доступные предметы:")
                for idx, item in enumerate(character1.inventory):
                    print(f"{idx + 1}. {item.name} (восстановление: {item.heal_amount})")
                item_choice = input("Выберите предмет (номер): ")
                if item_choice.isdigit() and 1 <= int(item_choice) <= len(character1.inventory):
                    character1.inventory[int(item_choice) - 1].use(character1)
                    character1.inventory.pop(int(item_choice) - 1)  # Удалить использованный предмет
                else:
                    print("Некорректный выбор предмета.")
            else:
                print("У вас нет предметов для использования.")
        else:
            print("Некорректное действие. Попробуйте снова.")

        if not character2.is_alive():
            print(f'{character2.name} побежден! Вы победили!')
            break

        # Ход противника
        action = random.choice(['атаковать', 'специальная атака'])
        if action == 'атаковать':
            character2.attack(character1)
        else:
            character2.special_attack(character1)

        if not character1.is_alive():
            print(f'{character1.name} побежден! Вы проиграли...')
            break


def main():
    print('Добро пожаловать в игру Герои!')
    player_name = input('Введите имя вашего героя: \n')

    choice = input('Выберите класс (1 - воин, 2 - маг, 3 - лучник, 4 - паладин): ')
    if choice == '1':
        player = Warrior(player_name)
    elif choice == '2':
        player = Mage(player_name)
    elif choice == '3':
        player = Archer(player_name)
    elif choice == '4':
        player = Paladin(player_name)
    else:
        print('Некорректный выбор. Создается воин по умолчанию!')
        player = Warrior(player_name)

    # Добавим инвентарь для игрока
    player.inventory = [
        Item('Зелье здоровья', 20),
        Item('Большое зелье здоровья', 50),
        Item('Эликсир маны', 30)
    ]  # Пример предметов

    enemies = [
        Warrior('Дракон'),
        Mage('Темный маг'),
        Archer('Ловкий лучник'),
        Paladin('Святой паладин')
    ]

    enemy = random.choice(enemies)

    print(f'\n{player.name} начинает бой с {enemy.name}')
    battle(player, enemy)


if __name__ == "__main__":
    main()

