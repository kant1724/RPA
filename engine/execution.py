import time
from engine import action
from engine.selenium_ctrl import selenium_action 
from engine import image_processor as ip
from engine import value_processor as vp
from excel import excel_manager as em
from engine import event_processor as ep
import win32api, win32con
from engine import axis_adjustment

stop_yn = False

def diable_all_keyboard_mode(obj):
    is_caps_on = win32api.GetKeyState(win32con.VK_CAPITAL)
    if is_caps_on == 1:
        action.keypress_only(obj, 'caps lock')

def execute(obj, adjust_yn):
    global stop_yn
    diable_all_keyboard_mode(obj)
    excel_data = em.read_excel(obj)
    obj.showMinimized()
    sa = selenium_action.Selenium_action()
    for data in excel_data:
        next_step = 1
        while next_step - 1 < len(obj.action_arr):            
            if stop_yn == True:
                stop_yn = False
                return
            i = next_step - 1
            interval = float(obj.interval_arr[i])
            time.sleep(interval)
            axis = obj.axis_arr[i].split(",")
            img = obj.image_arr[i]
            if adjust_yn == 'Y':
                axis = axis_adjustment.adjust(axis, img)
            value = vp.reprocess_value(obj.keypress_arr[i])
            ns = obj.next_step_arr[i].split(",")
            next_step = int(ns[0])            
            if obj.action_arr[i] == 'IE_OPEN':
                sa.ie_open()
            elif obj.action_arr[i] == 'IE_FULL_SCREEN':
                sa.ie_full_screen()
            elif obj.action_arr[i] == 'IE_GO_TO_SITE':
                sa.ie_go_to_site(value)
            elif obj.action_arr[i] == 'MOUSE_CLICK':
                action.mouse_click(obj, axis)
            elif obj.action_arr[i] == 'MOUSE_ONLY_CLICK':
                action.mouse_only_click(obj)
            elif obj.action_arr[i] == 'MOUSE_TP_CLICK':
                action.mouse_tp_click(obj, axis)
            elif obj.action_arr[i] == 'KEYPRESS_ONLY':
                action.keypress_only(obj, value)
            elif obj.action_arr[i] == 'KEYPRESS':
                action.keypress(obj, axis, value, data)
            elif obj.action_arr[i] == 'COPY_AND_PASTE':
                action.copy_and_paste(obj, axis, value, data)
            elif obj.action_arr[i] == 'GET_TEXT_VALUE':
                text = action.get_text_value(obj, axis)
                if value[0] == '$':
                    value = data[value]
                if text == value:
                    next_step = int(ns[0])
                else:
                    next_step = int(ns[1])
            elif obj.action_arr[i] == 'GET_TEXT_AND_WRITE_TO_FILE':
                action.get_text_and_write_to_file(obj, axis, data[value])
            elif obj.action_arr[i] == 'MOVE_TO_IMAGE':
                while True:
                    axis = ip.scan_image(obj, img)
                    relative_dist = obj.relative_dist_arr[i].split(",")
                    if axis != None:
                        differ_axis(axis, relative_dist)
                        action.mouse_move(obj, axis)
                        break
            elif obj.action_arr[i] == 'CLICK_BY_IMAGE':
                axis = ip.scan_image(obj, img)
                relative_dist = obj.relative_dist_arr[i].split(",")
                differ_axis(axis, relative_dist)
                action.mouse_click(obj, axis)                
            elif obj.action_arr[i] == 'KEYPRESS_BY_IMAGE':
                axis = ip.scan_image(obj, img)
                relative_dist = obj.relative_dist_arr[i].split(",")
                differ_axis(axis, relative_dist)
                if axis != None:
                    action.keypress(obj, axis, value, data)
            elif obj.action_arr[i] == 'IS_EQUAL_TO_IMAGE':
                is_true = ip.is_equal_to_image(obj, img, axis)
                if is_true:
                    next_step = int(ns[0])
                else:
                    next_step = int(ns[1])
def differ_axis(axis, relative_dist):
    axis[0] = str(int(axis[0]) - int(relative_dist[0]))
    axis[1] = str(int(axis[1]) - int(relative_dist[1]))
    