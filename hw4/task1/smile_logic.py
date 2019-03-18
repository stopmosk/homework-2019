# Функция, считающая парность скобочек
def is_correct(string):
    skob_list = []
    for s in string:
        s_type = 0
        if s == '{' or s == '}':
            s_type = 1
        if s == '[' or s == ']':
            s_type = 2
        if s == '(' or s == ')':
            s_type = 3
        if s in set('{[('):
            skob_list.append(s_type)
        if s in set('}])'):
            if len(skob_list) == 0 or s_type != skob_list[-1]:
                return False
            else:
                skob_list.pop()
    return len(skob_list) == 0
