import sys
from PyQt5.QtWidgets import QSizeGrip, QVBoxLayout, QWidget, QApplication, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMainWindow
from component import component_manager as cm
from engine import event_processor as ep

class layout(QMainWindow):
    data_file_arr = []
    
    def __init__(self):
        super().__init__()
        self.window()
        
    def window(self):
        self.register_add_btn = cm.register_add_button(self)
        self.register_delete_btn = cm.register_delete_button(self)
        self.register_list = cm.register_list(self)
        self.register_save = cm.register_save(self)        
        self.setGeometry(630, 150, 330, 320)
        self.show()
    
    def on_click_register_add(self):
        ep.register_add(self)
        
    def on_click_register_delete(self):
        ep.register_delete(self)
        
    def on_click_register_save(self):
        ep.register_save(self)
    
    def on_click_register_list(self, event):
        ep.register_list_event(self, event)        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    l = layout()
    sys.exit(app.exec_())
    