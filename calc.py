import cmath

def Calc_block(data):
    first_value, oper, sec_value = data
    if oper == '+':
        return sum(first_value, sec_value)
    if oper == '-':
        return sub(first_value, sec_value)
    if oper == '*':
        return mult(first_value, sec_value)
    if (oper =='/') and (sec_value != 0):
        return div(first_value, sec_value)
    else:
        return 'Ошибка!'

def sum(first_value, sec_value):
    return first_value + sec_value

def sub(first_value, sec_value):
    return first_value - sec_value

def mult(first_value, sec_value):
    return first_value * sec_value

def div(first_value, sec_value):
    return first_value / sec_value