import sys
import keyboard
from PyQt5.QtWidgets import QSizeGrip, QVBoxLayout, QWidget, QApplication, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMainWindow
from PyQt5.QtCore import Qt, QSettings
from gui_control import control
from component import component_manager as cm
from engine import event_processor as ep
from engine import execution

class captured_image_class(QMainWindow):
    def __init__(self, parent=None):
        super(captured_image_class, self).__init__(parent)
        self.setGeometry(630, 150, 300, 200)
        self.label = QLabel(self)  
        self.label.setGeometry(10, 10, 250, 180)
        
class layout(QMainWindow):
    c = control.Mouse()
    set_axis_toggle = False
    set_image_toggle = False
    set_relative_dist_toggle = False
    default_interval = 2
    action_arr, axis_arr, class_arr, image_arr, keypress_arr, interval_arr, next_step_arr, excel_file_arr, relative_dist_arr, captured_image_arr = [], [], [], [], [], [], [], [], [], []
    image_portion_arr = []
    temp_image_axis = ''
    first_list_currow, second_list_currow, third_list_currow, fourth_list_currow, fifth_list_currow, sixth_list_currow = -1, -1, -1, -1, -1, -1
    excel_file_path = ''
    settings = QSettings("RPA", "RPA")

    def __init__(self):
        super().__init__()
        keyboard.on_press(self.add_keypress)
        self.dialog = captured_image_class(self)
        self.window()
        
    def on_click_add(self):
        ep.add_event(self)
    
    def on_click_insert(self):
        ep.insert_event(self)
        
    def on_click_delete(self):
        ep.delete_event(self)

    def on_click_axis(self):
        self.set_axis_toggle = True
        
    def on_click_execute(self):
        ep.execute_event(self)
    
    def on_click_keypress_apply(self):
        ep.keypress_apply_event(self)
    
    def on_click_interval_apply(self):
        ep.interval_apply_event(self)
    
    def on_click_next_step_apply(self):
        ep.next_step_apply_event(self)
        
    def window(self):
        cm.add_menu(self)
        self.add_btn = cm.add_button(self)
        self.insert_btn = cm.insert_button(self)
        self.delete_btn = cm.delete_button(self)
        self.first_list_label = cm.first_list_label(self)
        self.first_list = cm.first_list(self)
        self.second_list_label = cm.second_list_label(self)
        self.second_list = cm.second_list(self)
        self.third_list_label = cm.third_list_label(self)
        self.third_list = cm.third_list(self)
        self.fourth_list_label = cm.fourth_list_label(self)
        self.fourth_list = cm.fourth_list(self)
        self.fifth_list_label = cm.fifth_list_label(self)
        self.fifth_list = cm.fifth_list(self)
        self.sixth_list_label = cm.sixth_list_label(self)
        self.sixth_list = cm.sixth_list(self)
        self.point_axis = cm.point_axis(self)
        self.set_image = cm.set_image(self)
        self.set_relative_dist = cm.set_relative_dist(self)
        #self.set_excel_file = cm.set_excel_file(self)
        self.execute = cm.execute(self)
        self.save = cm.save(self)        
        self.keypress_text = cm.set_keypress(self)
        self.keypress_apply = cm.keypress_apply_button(self)
        self.interval_text = cm.set_interval(self)
        self.interval_apply = cm.interval_apply_button(self)
        self.next_step_text = cm.set_next_step(self)
        self.next_step_apply = cm.next_step_apply_button(self)
        self.captured_image_toggle = cm.captured_image_toggle(self)
        self.adjust_axis = cm.adjust_axis(self)
        self.setGeometry(300, 300, 1450, 450)
        self.show()
    
    def on_click_set_image(self):
        self.set_image_toggle = True
        
    def on_click_set_relative_dist(self):
        self.set_relative_dist_toggle = True
    
    def on_click_excel_file(self):
        ep.set_excel_file(self)
    
    def on_click_captured_image_toggle(self):
        ep.show_captured_image(self, self.dialog)
    
    def on_click_adjust_axis(self):
        ep.on_click_adjust_axis(self)
    
    def mousePressEvent(self, event):
        ep.mouse_press_event(self)
        
    def mouseReleaseEvent(self, QMouseEvent):
        ep.mouse_release_event(self)
    
    def add_keypress(self, e):
        key = e.name
        if key == 'esc':
            execution.stop_yn = True
      
    def on_click_save(self):
        ep.save_event(self)
    
    def on_click_second_list(self, event):
        ep.second_list_event(self, event)        
    
    def on_click_third_list(self, event):
        ep.third_list_event(self, event)
        
    def on_click_fourth_list(self, event):
        ep.fourth_list_event(self, event)
        
    def on_click_fifth_list(self, event):
        ep.fifth_list_event(self, event)
    
    def on_click_sixth_list(self, event):
        ep.sixth_list_event(self, event)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    l = layout()
    sys.exit(app.exec_())
    