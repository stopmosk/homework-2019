import random


class River:

    def __init__(self, length):
        random.seed()
        if length <= 0:
            raise ValueError('Длина реки должна быть больше нуля')
        self.storage = [None] * length

    def __str__(self):
        result = ''
        for position, cell in enumerate(self.storage):
            result += ' - ' if cell is None else str(cell)
            result += ' '
        return result

    def __len__(self):
        return len(self.storage)

    def check_pos(self, position):
        if not (0 <= position < len(self)):
            raise ValueError('Координата выходит за допустимый диапазон')

    def is_free(self, position):
        self.check_pos(position)
        return self.storage[position] is None

    def free_cells(self):
        return self.storage.count(None)

    def get_free_position(self):
        if self.free_cells() == 0:
            raise ValueError('В реке закончилось свободное место')
        while True:
            position = random.choice(range(len(self)))
            if self.is_free(position):
                return position

    def get_next_object(self, position):
        # Возвращает объект равный или правее position и его координату
        # Если объекта нет, возвращает None и -1
        if position < 0:
            raise ValueError('Некорректное значение аргумента')
        for i in range(position, len(self)):
            if self.storage[i] is not None:
                return self.storage[i], i
        return None, -1

    def place_new_object(self, obj, position):
        self.check_pos(position)
        if obj is None:
            raise RuntimeError('Объект не должен быть "None"')
        if self.storage[position] is not None:
            raise RuntimeError('Данная ячейка занята')
        self.storage[position] = obj

    def move_object(self, position, new_pos):
        # Перемещает объект в реке
        self.check_pos(position)
        self.check_pos(new_pos)
        if self.storage[position] is None:
            raise RuntimeError('Вы пытаетесь переместить пустое место')
        if position == new_pos:
            return
        if self.storage[new_pos] is not None:
            raise RuntimeError('Невозможно переместить в занятую ячейку')
        self.storage[new_pos], self.storage[position] = \
            self.storage[position], self.storage[new_pos]

    def release_cell(self, position):
        self.check_pos(position)
        if self.storage[position] is None:
            raise RuntimeError('Вы пытаетесь освободить и так пустую ячейку')
        self.storage[position] = None
