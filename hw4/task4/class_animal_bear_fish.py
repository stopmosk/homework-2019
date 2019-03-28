import random


class Animal:
    animals = set()  # Тут будем хранить существующих животных
    min_pos, max_pos = 0, 0  # Рамки позиций для животных

    def __init__(self, position):
        if not (Animal.min_pos <= position < Animal.max_pos):
            raise ValueError('Некорректное значение аргумента')
        random.seed()
        self.x = position
        self.direction = random.choice([-1, 0, 1])
        if not (Animal.min_pos <= self.x + self.direction < Animal.max_pos):
            self.direction = 0
        Animal.animals.add(self)

    def get_position(self):
        return self.x

    def is_dead(self):
        return self.hp == 0

    def stop(self):
        self.direction = 0

    def kill(self):
        Animal.animals.remove(self)

    @staticmethod
    def set_bounds(min_x, max_x):
        if min_x > max_x:
            raise ValueError('Некорректно заданы параметры')
        Animal.min_pos, Animal.max_pos = min_x, max_x

    @staticmethod
    def count():
        return len(Animal.animals)

    @staticmethod
    def is_meet(animal_1, animal_2):
        if animal_1.x > animal_2.x:
            raise ValueError('Второе животное должно быть правее первого')
        pos_1 = animal_1.x + animal_1.direction
        pos_2 = animal_2.x + animal_2.direction
        if pos_1 >= pos_2 or pos_1 >= pos_2 - animal_2.direction:
            return True
        return False


class Bear(Animal):
    max_hp = 10
    bears = set()  # Тут будем хранить существующих медведов

    def __init__(self, position):
        super().__init__(position)
        self.hp = Bear.max_hp  # max_life
        Bear.bears.add(self)

    def __str__(self):
        left, right = ' ', ' '
        if self.direction == -1:
            left = '<'
        if self.direction == 1:
            right = '>'
        # result = left + str(self.hp) + right
        result = left + '🐻' + right
        return result

    @staticmethod
    def is_bear(obj):
        return obj in Bear.bears

    @staticmethod
    def count():
        return len(Bear.bears)

    @staticmethod
    def set_max_hp(n):
        Bear.max_hp = n

    def go(self):
        Bear.bears.remove(self)
        self.x += self.direction
        self.direction = random.choice([-1, 0, 1])
        if not (Animal.min_pos <= self.x + self.direction < Animal.max_pos):
            self.direction = 0
        Bear.bears.add(self)
        self.hp -= 1
        return self.x

    def stay(self):
        self.direction = 0
        self.hp -= 1

    def kill(self):
        Bear.bears.remove(self)
        super().kill()

    def eat(self):
        self.hp = Bear.max_hp + 1


class Fish(Animal):
    fishes = set()  # Тут будем хранить существующих рыб

    def __init__(self, position):
        super().__init__(position)
        self.hp = 1  # max_life
        Fish.fishes.add(self)

    def __str__(self):
        left, right = ' ', ' '
        if self.direction == -1:
            left = '<'
        if self.direction == 1:
            right = '>'
        # result = left + str(self.hp) + right
        result = left + '🐟' + right
        return result

    @staticmethod
    def is_fish(obj):
        return obj in Fish.fishes

    @staticmethod
    def count():
        return len(Fish.fishes)

    def go(self):
        Fish.fishes.remove(self)
        self.x += self.direction
        self.direction = random.choice([-1, 0, 1])
        if not (Animal.min_pos <= self.x + self.direction < Animal.max_pos):
            self.direction = 0
        Fish.fishes.add(self)
        return self.x

    def stay(self):
        self.direction = 0

    def kill(self):
        Fish.fishes.remove(self)
        super().kill()
