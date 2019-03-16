# Функция, определяющая, есть ли пересечение у двух шаров (кругов) на плоскости
def balls_collide(ball_1, ball_2):
    if not isinstance(ball_1, tuple) or not isinstance(ball_2, tuple):
        raise TypeError('Ваши аргументы - говно (должны быть два кортежа)')
    if len(ball_1) != 3 or len(ball_2) != 3:
        raise TypeError('Для каждого шара нужны три числа: две координаты и радиус')
    for i in range(3):
        if not isinstance(ball_1[i], (float, int)) or not isinstance(ball_2[i], (float, int)):
            raise TypeError('Координаты и радиусы должны быть float или int')
    if ball_1[2] < 0 or ball_2[2] < 0:
        raise ValueError('Радиусы должны быть неотрицательными числами')

    x1, y1, x2, y2 = ball_1[0], ball_1[1], ball_2[0], ball_2[1]
    balls_dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return balls_dist <= ball_1[2] + ball_2[2]


#print(balls_collide((5.5, 2.4, 8.0), (5.0, 5.7, 2.0)))
#print(balls_collide((0, 0, -1), (2, 2, 1)))