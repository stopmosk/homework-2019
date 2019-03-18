from trades_logic import *

db, ex_list = database_read('trades.csv')

print('')
print('******** ОКНО С МАКСИМАЛЬНЫМ КОЛИЧЕСТВОМ СДЕЛОК **********')
print('  Окно             Кол-во сделок        Сумма сделок')
max_gap, max_qty, max_sum = max_qty_gap(db)
print(max_gap, max_qty, max_sum, sep='\t\t\t\t')
print('**********************************************************')
print()

print('****** ОКНА С МАКСИМАЛЬНЫМ КОЛИЧЕСТВОМ СДЕЛОК ПО БИРЖАМ ******')
for ex in ex_list:
    print('Биржа: ', end='')
    print(ex)
    max_gap, max_qty, max_sum = max_qty_gap_ex(db, ex)
    print('  Окно             Кол-во сделок        Сумма сделок')
    print(max_gap, max_qty, max_sum, sep='\t\t\t\t')
    print('******************************************************')
