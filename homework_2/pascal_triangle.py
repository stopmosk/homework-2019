def pascal_triangle(n):
    if type(n) != int: raise TypeError('Введено не целое число')
    if n <= 0: raise ValueError('Введено не положительное число')

    pascal_t = [[1]]
    if n == 1: return pascal_t

    pascal_t.append([1, 1])
    if n == 2: return pascal_t

    for row in range(2, n):
        row_list = [1]      # Первая единичка в ряду

        for col in range(row - 1):
            row_list.append(pascal_t[row - 1][col] + pascal_t[row - 1][col + 1])

        row_list.append(1)  # Последняя единичка в ряду
        pascal_t.append(row_list)

    return pascal_t


# print(pascal_triangle(6))
