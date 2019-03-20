def database_read(filename):
    # Считывает базу данных из файла. В каждом окне транзакции суммируются по каждой фирме.
    db = dict()
    ex_list = set()
    with open(filename, 'r') as trades_file:
        trades_file.readline()   # Считали ненужную строку с заголовками
        for trade_line in trades_file:
            time, price, qty, exchange = trade_line.strip().split(',')
            gap = time[:8]   # Вычислили окно путём округления до секунд
            ex_sum = float(price) * int(qty)   # Сумма сделки
            if gap in db:
                gap_list = db[gap]
                if exchange in gap_list:
                    new_qty = gap_list[exchange][0] + 1
                    new_sum = gap_list[exchange][1] + ex_sum
                    db[gap].update({exchange: [new_qty, new_sum]})
                else:
                    db[gap].update({exchange: [1, ex_sum]})
                    ex_list.add(exchange)
            else:
                db[gap] = {exchange: [1, ex_sum]}
    return db, ex_list


def max_qty_gap_ex(db, ex):
    # Возвращает окно с максимальным кол-вом сделок для биржи ex.
    max_gap, max_qty, max_sum = '', 0, 0
    for gap in db:
        test_ex = db[gap].get(ex)
        if test_ex is not None:
            if test_ex[0] > max_qty:
                max_gap = gap
                max_qty = test_ex[0]
                max_sum = test_ex[1]
    return max_gap, max_qty, max_sum


def max_qty_gap(db):
    # Возвращает окно с максимальным кол-вом сделок для всей базы данных.
    max_gap, max_qty, max_sum = '', 0, 0
    for gap in db:
        s_qty, s_sum = 0, 0
        for ex in db[gap]:
            s_qty += db[gap][ex][0]
            s_sum += db[gap][ex][1]
        if s_qty > max_qty:
            max_gap = gap
            max_qty = s_qty
            max_sum = s_sum
    return max_gap, max_qty, max_sum
