import random
from class_river import *
from class_animal_bear_fish import *


def place_animals(river, n_bears, m_fish):
    # Располагает n медведей и m рыб в случайных ячейках реки
    if n_bears + m_fish > river.free_cells():
        # raise ValueError('Река переполнена')
        return False
    for i in range(n_bears):
        position = river.get_free_position()
        river.place_new_object(Bear(position), position)
    for i in range(m_fish):
        position = river.get_free_position()
        river.place_new_object(Fish(position), position)
    return True


def init_river(river, n_bears, m_fish):
    # Инициализация. Устанавливаем границы, затем размещаем животных
    Animal.set_bounds(0, len(river))
    return place_animals(river, n_bears, m_fish)


def do_step(river):
    # Выполнение шага симуляции
    new_bear_count, new_fish_count = 0, 0
    animal, position = river.get_next_object(0)
    if animal is None:
        print('В речке все умерли')
        return True
    while True:
        next_animal, next_position = river.get_next_object(position + 1)
        if next_animal is None:
            # Если справа уже нет ни медведей, ни рыб
            new_position = animal.go()
            river.move_object(position, new_position)
            if animal.is_dead():
                river.release_cell(new_position)
                animal.kill()
            if not place_animals(river, new_bear_count, new_fish_count):
                print('Река переполнена')
                return True
            return False

        if not Animal.is_meet(animal, next_animal):
            # Это если никто ни с кем не встретился
            new_position = animal.go()
            river.move_object(position, new_position)
            if animal.is_dead():
                river.release_cell(new_position)
                animal.kill()
            animal, position = next_animal, next_position
            continue

        if Bear.is_bear(animal) and Bear.is_bear(next_animal):
            # Если встретелись МЕДВЕДЬ с МЕДВЕДЕМ
            bear, next_bear = animal, next_animal
            new_bear_count += 1
            bear.stay()
            if bear.is_dead():
                river.release_cell(position)
                bear.kill()
            next_bear.stop()
            animal, position = next_animal, next_position
            continue

        if Fish.is_fish(animal) and Fish.is_fish(next_animal):
            # Если встретелись РЫБА с РЫБОЙ
            fish, next_fish = animal, next_animal
            new_fish_count += 1
            fish.stay()
            if fish.is_dead():
                river.release_cell(position)
                fish.kill()
            next_fish.stop()
            animal, position = next_animal, next_position
            continue

        if Bear.is_bear(animal) and Fish.is_fish(next_animal):
            # Если встретелись МЕДВЕДЬ с РЫБОЙ
            bear, fish = animal, next_animal
            bear.stay()
            bear.eat()
            fish.kill()
            river.release_cell(next_position)
            animal, position = river.get_next_object(next_position)
            if animal is None:
                # Если справа уже нет ни медведей, ни рыб
                if not place_animals(river, new_bear_count, new_fish_count):
                    print('Река переполнена')
                    return True
                return False
            continue

        if Fish.is_fish(animal) and Bear.is_bear(next_animal):
            # Если встретелись РЫБА с МЕДВЕДЕМ
            fish, bear = animal, next_animal
            river.release_cell(position)
            bear.eat()
            fish.kill()
            bear.stop()
            animal, position = next_animal, next_position
            continue


length = int(input('Введите длину реки N:'))
n = int(input('Введите число медведей:'))
m = int(input('Введите число рыб:'))
k = int(input('Максимальная жизнь медведя:'))

my_river = River(length)
Bear.set_max_hp(k)
init_river(my_river, n, m)

finish = False
while not finish:
    print(my_river)
    input(':')
    finish = do_step(my_river)
    if Bear.count() == 0:
        break

print(my_river)
print('Медведей: ' + str(Bear.count()) + ' Рыб: ' + str(Fish.count()) +
      ' Всего живых существ: ' + str(Animal.count()))
