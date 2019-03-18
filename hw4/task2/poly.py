from poly_logic import derivative_poly_s

# poly = '4x^8 + 2x^3 + 20x - 8x + 20 + 10x^20 + 2x^8'
poly = input('Введите многочлен: ')
# poly = '5x2'
print('Ваш многочлен: ' + poly)
print('Производная многочлена: ' + derivative_poly_s(poly))
