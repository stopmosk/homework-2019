# Функция, определяющая, есть ли пересечение у двух шаров (кругов) на плоскости
def balls_collide(ball_1, ball_2):
    if len(ball_1) != 3 or len(ball_2) != 3:
        raise TypeError('Для каждого шара нужно три числа: x ,y ,r')

    r1, r2 = ball_1[2], ball_2[2]
    if r1 < 0 or r2 < 0:
        raise ValueError('Радиусы должны быть неотрицательными числами')
    # if r1 == 0 or r2 == 0: return False

    x1, y1, x2, y2 = ball_1[0], ball_1[1], ball_2[0], ball_2[1]
    balls_dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return balls_dist <= r1 + r2
