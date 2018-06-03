import time
from util import kor_to_eng_converter as ktec
from gui_control import gui_control_wrapper as gcw

def execute_press(s):
    if ktec.isHanguel(s):
        gcw.press_hanguel_key()
        s = ktec.korTypeToEng(s)
        gcw.write_text(s)
        gcw.press_hanguel_key()
    else:
        gcw.press_key(s)
        
def mouse_click(obj, axis):
    obj.c.click((int(axis[0]), int(axis[1])))

def mouse_move(obj, axis):
    obj.c.move_mouse((int(axis[0]), int(axis[1])))

def mouse_only_click(obj):
    obj.c.only_click()

def mouse_tp_click(obj, axis):
    obj.c.triple_click((int(axis[0]), int(axis[1])))

def keypress_only(obj, value):
    if value == 'del':
        gcw.press_del()
    elif value == 'home':
        gcw.press_home()
    elif value == 'end':
        gcw.press_end()
    elif value == 'enter':
        gcw.press_enter()
    elif value == "backspace":
        gcw.press_backspace()
    elif value == "tab":
        gcw.press_tab()
    elif value == "right shift":
        gcw.press_shift()
    elif value == "left shift":
        gcw.press_shift()
    elif value == "right alt":
        gcw.press_hanguel_key()
    elif value == "caps lock":
        gcw.press_capslock()
    elif value == "hanguel":
        gcw.press_hanguel_key()
    elif value == "page down":
        gcw.press_page_down()
    elif value == "down":
        gcw.press_down()
    else:
        gcw.write_text(value)
        
def keypress(obj, axis, value, data):
    obj.c.click((int(axis[0]), int(axis[1])))
    gcw.press_ctrl_a()
    gcw.press_del()
    obj.c.click((int(axis[0]), int(axis[1])))
    if value[0] == '$':
        val = data[value]
        if ktec.isHanguel(val) == False:
            gcw.write_text(val)
        else:
            for s in val:
                execute_press(s)
    else:
        for s in value:
            execute_press(s)

def copy_and_paste(obj, axis, value, data):
    obj.c.click((int(axis[0]), int(axis[1])))
    gcw.press_ctrl_a()
    gcw.press_del()
    obj.c.click((int(axis[0]), int(axis[1])))
    if value[0] == '$':
        val = data[value]
        obj.c.copy(val)
    else:
        obj.c.copy(value)
    obj.c.click((int(axis[0]), int(axis[1])))
    time.sleep(0.15)
    obj.c.click((int(axis[0]), int(axis[1])))
    time.sleep(0.15)
    gcw.press_ctrl_v()

def get_text_value(obj, axis):
    obj.c.double_click((int(axis[0]), int(axis[1])))
    gcw.press_ctrl_c()
    text = obj.c.get_copy_value()
    return text

def get_text_and_write_to_file(obj, axis, brnc_nm):
    gcw.press_ctrl_a()
    gcw.press_ctrl_c()
    f = open('./exam_output.txt', 'a', encoding='utf8')
    f.write(brnc_nm + ',' + str(obj.c.get_copy_value()) + '\n')
    f.close()
