from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from engine import loader as l
from engine import saver
from engine import execution
from engine import axis_adjustment
from engine import image_processor as ip
from excel import excel_manager as em
import time

def add_event(obj):
    cur_item = obj.first_list.currentItem()
    if cur_item != None:
        text = cur_item.text()
        obj.second_list.addItem(text)
        obj.action_arr.append(text)
        obj.third_list.addItem('0,0')
        obj.axis_arr.append('0,0')
        obj.class_arr.append('')
        obj.image_arr.append('')
        obj.relative_dist_arr.append('0,0')
        obj.keypress_arr.append('')
        obj.interval_arr.append(str(obj.default_interval))
        obj.next_step_arr.append(str(len(obj.next_step_arr) + 2) + "," + str(len(obj.next_step_arr) + 1))
        obj.excel_file_arr.append('')
        obj.captured_image_arr.append('')
        obj.image_portion_arr.append('')
        
def insert_event(obj):
    cur_item = obj.first_list.currentItem()
    if cur_item != None:
        nRow = obj.second_list_currow
        if nRow == -1:
            nRow = 0
        text = cur_item.text()
        obj.second_list.insertItem(nRow, text)
        obj.third_list.insertItem(nRow, '0,0')
        obj.action_arr.insert(nRow, text)
        obj.axis_arr.insert(nRow, '0,0')
        obj.class_arr.insert(nRow, '')
        obj.image_arr.insert(nRow, '')
        obj.relative_dist_arr.insert(nRow, '0,0')
        obj.keypress_arr.insert(nRow, '')
        obj.interval_arr.insert(nRow, str(obj.default_interval))
        obj.next_step_arr.insert(nRow, str(nRow + 2) + "," + str(len(obj.next_step_arr) + 1))
        obj.excel_file_arr.insert(nRow, '')
        obj.captured_image_arr.insert(nRow, '')
        obj.image_portion_arr.insert(nRow, '')
        for i in range(len(obj.next_step_arr)):
            if i > nRow:
                ns = obj.next_step_arr[i].split(",")
                for j in range(len(ns)):
                    ns[j] = str(int(ns[j]) + 1)
                obj.next_step_arr[i] = str(",".join(ns))
        obj.second_list.setCurrentRow(nRow)
        second_list_event(obj, '')
        
def delete_event(obj):
    if obj.second_list_currow < 0:
        return
    last = False
    if obj.second_list_currow == len(obj.action_arr) - 1:
        last = True
    obj.second_list.takeItem(obj.second_list_currow)
    obj.third_list.takeItem(obj.second_list_currow)
    obj.action_arr.pop(obj.second_list_currow)
    obj.axis_arr.pop(obj.second_list_currow)
    obj.class_arr.pop(obj.second_list_currow)
    obj.image_arr.pop(obj.second_list_currow)
    obj.relative_dist_arr.pop(obj.second_list_currow)
    obj.keypress_arr.pop(obj.second_list_currow)
    obj.interval_arr.pop(obj.second_list_currow)
    obj.next_step_arr.pop(obj.second_list_currow)
    obj.excel_file_arr.pop(obj.second_list_currow)
    obj.captured_image_arr.pop(obj.second_list_currow)
    obj.image_portion_arr.pop(obj.second_list_currow)
    obj.fourth_list.clear()
    obj.fifth_list.clear()
    obj.sixth_list.clear()
    if last == True:
        obj.second_list_currow = obj.second_list_currow - 1
        obj.third_list_currow = obj.third_list_currow - 1    
    if last == False:    
        for i in range(len(obj.next_step_arr)):        
            if i >= obj.second_list_currow:                
                ns = obj.next_step_arr[i].split(",")
                for j in range(len(ns)):
                    ns[j] = str(int(ns[j]) - 1)
                obj.next_step_arr[i] = str(",".join(ns))
    obj.second_list.setCurrentRow(obj.second_list_currow)
    second_list_event(obj, '')
    
def execute_event(obj):
    execution.execute(obj, 'N')

def keypress_apply_event(obj):
    if obj.second_list_currow < 0:
        return
    if obj.fourth_list.currentItem() == None:
        return
    obj.keypress_arr[obj.second_list_currow] = obj.keypress_text.text()
    obj.fourth_list.currentItem().setText(obj.keypress_text.text())
    
def interval_apply_event(obj):
    if obj.second_list_currow < 0:
        return
    if obj.fifth_list.currentItem() == None:
        return
    obj.interval_arr[obj.second_list_currow] = obj.interval_text.text()
    obj.fifth_list.currentItem().setText(obj.interval_text.text())

def next_step_apply_event(obj):
    if obj.second_list_currow < 0:
        return
    if obj.sixth_list.currentItem() == None:
        return
    obj.next_step_arr[obj.second_list_currow] = obj.next_step_text.text()
    obj.sixth_list.currentItem().setText(obj.next_step_text.text())

def set_image_event(obj, p):
    if obj.second_list_currow < 0:
        return
    a = obj.class_arr[obj.third_list_currow].replace(":image_ok", "")
    a += ":image_ok"
    obj.class_arr[obj.third_list_currow] = a
    obj.image_arr[obj.third_list_currow] = ip.get_image(obj, p)
    return a
    
def set_excel_file(obj):
    excel_path = em.set_excel_file(obj)
    obj.excel_file_arr[obj.second_list_currow] = excel_path
    
def mouse_press_event(obj):
    if obj.set_axis_toggle == True:
        hide_window(obj)
        QApplication.setOverrideCursor(QCursor(Qt.PointingHandCursor))
    elif obj.set_image_toggle == True:
        hide_window(obj)
        QApplication.setOverrideCursor(QCursor(Qt.PointingHandCursor))
    elif obj.set_relative_dist_toggle == True:
        hide_window(obj)
        QApplication.setOverrideCursor(QCursor(Qt.PointingHandCursor))
        
def mouse_release_event(obj):
    if obj.set_axis_toggle == True:        
        pos = obj.c.get_position()
        text = obj.keypress_arr[obj.third_list_currow]
        captured, portion = ip.capture_image(obj, pos, text)
        show_window(obj)
        cur_item = obj.third_list.currentItem()
        if cur_item != None:            
            p = str(pos[0]) + ',' + str(pos[1])
            a = set_image_event(obj, p)
            cur_item.setText(p)
            obj.axis_arr[obj.third_list_currow] = p
            obj.captured_image_arr[obj.third_list_currow] = captured
            obj.image_portion_arr[obj.third_list_currow] = portion
            show_image_portion(obj, obj.dialog, portion)
            QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))
            obj.set_axis_toggle = False
    elif obj.set_image_toggle == True:
        pos = obj.c.get_position()
        captured, portion = ip.capture_image(obj, pos, "")
        show_window(obj)
        cur_item = obj.third_list.currentItem()
        if cur_item != None:
            obj.c.move_mouse((0, 0))
            p = str(pos[0]) + ',' + str(pos[1])                        
            obj.axis_arr[obj.third_list_currow] = p
            obj.temp_image_axis = p
            a = set_image_event(obj, p)
            cur_item.setText(a)
            obj.captured_image_arr[obj.third_list_currow] = captured
            obj.image_portion_arr[obj.third_list_currow] = portion
            show_image_portion(obj, obj.dialog, portion)
            QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))
            time.sleep(0.2)
            obj.c.move_mouse(pos)
            obj.set_image_toggle = False
    elif obj.set_relative_dist_toggle == True:
        show_window(obj)
        cur_item = obj.third_list.currentItem()
        if cur_item != None:
            if obj.temp_image_axis == '':
                obj.set_relative_dist_toggle = False
                return 
            pos = obj.c.get_position()
            image_pos = obj.temp_image_axis.split(",")
            p = str(int(image_pos[0]) - pos[0]) + ',' + str(int(image_pos[1]) - pos[1])
            obj.relative_dist_arr[obj.third_list_currow] = p
            QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))
            obj.set_relative_dist_toggle = False
            
def second_list_event(obj, event):
    obj.fourth_list.clear()
    obj.fifth_list.clear()
    obj.sixth_list.clear()
    if len(obj.second_list.selectedIndexes()) > 0:
        obj.second_list_currow = obj.third_list_currow = obj.second_list.selectedIndexes()[0].row()
        show_image_portion(obj, obj.dialog, obj.image_portion_arr[obj.second_list_currow])
    else:
        obj.second_list_currow = -1
    if obj.second_list_currow >= 0:
        obj.third_list.setCurrentRow(obj.second_list_currow)
        fourth_list_when = ['KEYPRESS_BY_IMAGE', 'KEYPRESS_ONLY', 'KEYPRESS', 'COPY_AND_PASTE', 'GET_TEXT_VALUE', 'IE_GO_TO_SITE']
        if obj.action_arr[obj.third_list_currow] in fourth_list_when:
            obj.fourth_list.addItem(obj.keypress_arr[obj.second_list_currow])
            obj.fourth_list.setCurrentRow(0)
        obj.fifth_list.addItem(str(obj.interval_arr[obj.second_list_currow]))
        obj.sixth_list.addItem(obj.next_step_arr[obj.second_list_currow])
        obj.fifth_list.setCurrentRow(0)
        obj.sixth_list.setCurrentRow(0)    

def third_list_event(obj, event):
    obj.fourth_list.clear()
    obj.fifth_list.clear()
    obj.sixth_list.clear()
    obj.third_list_currow = obj.second_list_currow = obj.third_list.selectedIndexes()[0].row()
    obj.second_list.setCurrentRow(obj.third_list_currow)
    fourth_list_when = ['KEYPRESS_BY_IMAGE', 'KEYPRESS_ONLY', 'KEYPRESS', 'COPY_AND_PASTE', 'GET_TEXT_VALUE', 'IE_GO_TO_SITE']
    if obj.action_arr[obj.third_list_currow] in fourth_list_when:
        obj.fourth_list.addItem(obj.keypress_arr[obj.second_list_currow])
        obj.fourth_list.setCurrentRow(0)
    obj.fifth_list.addItem(str(obj.interval_arr[obj.second_list_currow]))
    obj.fifth_list.setCurrentRow(0)
    obj.sixth_list.addItem(str(obj.next_step_arr[obj.second_list_currow]))
    obj.sixth_list.setCurrentRow(0)
        
def fourth_list_event(obj, event):
    obj.fourth_list_currow = obj.fourth_list.selectedIndexes()[0].row()

def fifth_list_event(obj, event):
    obj.fifth_list_currow = obj.fifth_list.selectedIndexes()[0].row()

def sixth_list_event(obj, event):
    obj.sixth_list_currow = obj.sixth_list.selectedIndexes()[0].row()
    
def save_event(obj):
    saver.save_file(obj)
    
def register_add(obj):
    l.load_file_in_register(obj)
    
def register_delete(obj):
    obj.register_list.takeItem(obj.register_list_currow)
    obj.data_file_arr.pop(obj.register_list_currow)
    
def register_save(obj):
    saver.save_register_file(obj)
    
def register_list_event(obj, event):
    obj.register_list_currow = obj.register_list.selectedIndexes()[0].row()

def show_captured_image(obj, child):
    captured = obj.captured_image_arr[obj.third_list_currow]
    ip.save_image(captured)     

def show_image_portion(obj, child, img):    
    if img == '':
        pixmap = QPixmap()
        child.label.setPixmap(pixmap)
        return
    pixmap = QPixmap(img)
    child.show()
    child.label.setPixmap(pixmap)

def on_click_adjust_axis(obj):
    execution.execute(obj, 'Y')

def hide_window(obj):
    obj.settings.setValue("main", obj.saveGeometry())
    obj.settings.setValue("img", obj.dialog.saveGeometry())
    obj.setGeometry(-30, -30, 1, 1)
    obj.dialog.setGeometry(-30, -30, 1, 1)
    
def show_window(obj):
    obj.restoreGeometry(obj.settings.value("main"))
    obj.dialog.restoreGeometry(obj.settings.value("img"))
    