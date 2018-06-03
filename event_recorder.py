import keyboard
import mouse
import time
from gui_control import control
from engine import saver
from engine import image_processor as ip

class event_recorder():
    action_arr, axis_arr, class_arr, image_arr, keypress_arr, interval_arr, next_step_arr, excel_file_arr, relative_dist_arr = [], [], [], [], [], [], [], [], []
    timestamp = time.time()
    c = control.Mouse()
    image_mode = False
    previous_pos = (-1, -1)
    
    def add_row(self, action, axis, keypress, image, interval):
        self.action_arr.append(action)
        self.axis_arr.append(axis)
        self.class_arr.append('')
        self.image_arr.append(image)
        self.relative_dist_arr.append('0,0')
        self.keypress_arr.append(keypress)
        self.interval_arr.append(interval)
        self.next_step_arr.append(str(len(self.next_step_arr) + 2) + "," + str(len(self.next_step_arr) + 1))
        self.excel_file_arr.append('')
    
    def add_mouse_left_click(self):
        pos = self.c.get_position()
        axis = str(pos[0]) + ',' + str(pos[1])
        self.timestamp = time.time()
        if self.previous_pos == pos:
            self.add_row('MOUSE_ONLY_CLICK', '', '', '', 0.001)
        else:
            self.add_row('MOUSE_CLICK', axis, '', '', 1)
        self.previous_pos = pos
    
    def add_move_to_image(self):
        pos = self.c.get_position()
        axis = str(pos[0]) + ',' + str(pos[1])
        self.c.move_mouse((0, 0))
        time.sleep(0.2)
        self.add_row('MOVE_TO_IMAGE', axis, '', ip.get_image(self, axis), 1)
        self.c.move_mouse(pos)
        self.previous_pos = pos
        
    def add_wait_until_image_is_there(self):
        pos = self.c.get_position()
        axis = str(pos[0]) + ',' + str(pos[1])
        self.c.move_mouse((0, 0))
        time.sleep(0.2)
        self.add_row('IS_EQUAL_TO_IMAGE', axis, '', ip.get_image(self, axis), 1)
        self.c.move_mouse(pos)
        
    def add_keypress(self, e):
        key = e.name
        print(key)
        if key == 'f8':
            self.add_wait_until_image_is_there()
        elif key == 'f9':
            self.add_move_to_image()
        elif key != 'esc':
            self.timestamp = time.time()
            self.add_row('KEYPRESS_ONLY', '', key, '', 0.1)
        
    def start(self):
        keyboard.wait('esc')
        mouse.on_click(self.add_mouse_left_click)        
        keyboard.on_press(self.add_keypress)
        keyboard.wait('esc')
        mouse.unhook_all()
        keyboard.unhook_all()
        saver.save_file(self)    

if __name__ == '__main__':
    cls = event_recorder()
    cls.start()
