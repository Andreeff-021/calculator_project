import view as c_ui
from fractions import Fraction
import cmath
from calc import Calc_block as calc
import actions_data as d_t


def actions_data(data):
    data_type, first_value, oper, sec_value = data

    if data_type == '1':

        first_value = complex(first_value)

        sec_value = complex(sec_value)

    elif data_type == '2':

        a = first_value
        first_value = Fraction(int(a[0: a.index(
            '/')]), int(a[a.index('/')+1:len(a)]))

        g = sec_value
        sec_value = Fraction(int(g[0: g.index(
            '/')]), int(g[g.index('/')+1:len(g)]))

    return (first_value, oper, sec_value)