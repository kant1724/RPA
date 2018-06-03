import keyboard
from gui_control import control
from engine import loader as l
from engine import execution
import sys

class scheduler():
    c = control.Mouse()
    action_arr, axis_arr, class_arr, image_arr, keypress_arr, interval_arr, next_step_arr, excel_file_arr, relative_dist_arr = [], [], [], [], [], [], [], [], []
    excel_file_path =''
    default_interval = 3
    
    def go(self):
        file_name = sys.argv[1]
        keyboard.on_press(self.add_keypress)
        with open('./save/' + file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                l.load_file_in_scheduler(self, line.replace("\n", ''))
                execution.execute(self)
    
    def add_keypress(self, e):
        key = e.name
        if key == 'esc':
            execution.stop_yn = True
    
if __name__ == '__main__':
    s = scheduler()
    s.go()
