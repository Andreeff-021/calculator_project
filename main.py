from calc import Calc_block as calc
from logger import result_logger as write_log
import actions_data as a_d
import view as calc_w


def button_click():
    j = a_d.actions_data(calc_w.input_data())
    calc_result = calc(j)
    calc_w.view_data(calc_result, 'Ответ:')
    write_log(j, calc_result)

button_click()