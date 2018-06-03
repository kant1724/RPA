from PyQt5.QtWidgets import QAction, QSizeGrip, QVBoxLayout, QWidget, QApplication, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QFont
from engine import loader as l
from excel import excel_manager as em
from component import component_position as cp

def add_menu(obj):
    menubar = obj.menuBar()
    load_menu = menubar.addMenu('Load')
    load_action = QAction('&Load', obj)
    load_action.triggered.connect(lambda: l.load_file(obj))        
    load_menu.addAction(load_action)
    excel_menu = menubar.addMenu('Excel')
    excel_action = QAction('&Excel', obj)
    excel_action.triggered.connect(lambda: em.set_excel_file(obj))        
    excel_menu.addAction(excel_action)
    
def add_button(obj):
    btn = QPushButton(obj)
    btn.setText("add")
    btn.setGeometry(cp.ADD_BUTTON_X_START, cp.ADD_BUTTON_Y_START, cp.ADD_BUTTON_WIDTH, cp.ADD_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_add)
    return btn

def insert_button(obj):
    btn = QPushButton(obj)
    btn.setText("insert")
    btn.setGeometry(cp.INSERT_BUTTON_X_START, cp.INSERT_BUTTON_Y_START, cp.INSERT_BUTTON_WIDTH, cp.INSERT_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_insert)
    return btn

def delete_button(obj):
    btn = QPushButton(obj)
    btn.setText("delete")
    btn.setGeometry(cp.DELETE_BUTTON_X_START, cp.DELETE_BUTTON_Y_START, cp.DELETE_BUTTON_WIDTH, cp.DELETE_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_delete)
    return btn

def first_list_label(obj):
    label = QLabel("Selection", obj)
    font = QFont()
    font.setBold(True)
    label.setFont(font)
    label.setGeometry(cp.FIRST_LIST_X_START, cp.FIRST_LIST_Y_START - 25, cp.FIRST_LIST_WIDTH, 20)
    return 

def first_list(obj):
    ll = QListWidget(obj)
    ll.addItem('MOUSE_CLICK')
    ll.addItem('MOUSE_TP_CLICK')
    ll.addItem('KEYPRESS_ONLY')
    ll.addItem('KEYPRESS')
    ll.addItem('CLICK_BY_IMAGE')
    ll.addItem('KEYPRESS_BY_IMAGE')
    ll.addItem('IS_EQUAL_TO_IMAGE')
    ll.addItem("COPY_AND_PASTE")
    ll.addItem("GET_TEXT_VALUE")
    ll.addItem('GET_TEXT_AND_WRITE_TO_FILE')
    ll.setGeometry(cp.FIRST_LIST_X_START, cp.FIRST_LIST_Y_START, cp.FIRST_LIST_WIDTH, cp.FIRST_LIST_HEIGHT)    
    return ll

def second_list_label(obj):
    label = QLabel("Action", obj)
    font = QFont()
    font.setBold(True)
    label.setFont(font)
    label.setGeometry(cp.SECOND_LIST_X_START, cp.SECOND_LIST_Y_START - 25, cp.SECOND_LIST_WIDTH, 20)
    return

def second_list(obj):
    ll = QListWidget(obj)
    ll.setGeometry(cp.SECOND_LIST_X_START, cp.SECOND_LIST_Y_START, cp.SECOND_LIST_WIDTH, cp.SECOND_LIST_HEIGHT)
    ll.clicked.connect(obj.on_click_second_list)
    return ll

def third_list_label(obj):
    label = QLabel("Axis/Image", obj)
    font = QFont()
    font.setBold(True)
    label.setFont(font)
    label.setGeometry(cp.THIRD_LIST_X_START, cp.THIRD_LIST_Y_START - 25, cp.THIRD_LIST_WIDTH, 20)
    return

def third_list(obj):
    ll = QListWidget(obj)
    ll.setGeometry(cp.THIRD_LIST_X_START, cp.THIRD_LIST_Y_START, cp.THIRD_LIST_WIDTH, cp.THIRD_LIST_HEIGHT)
    ll.clicked.connect(obj.on_click_third_list)
    return ll
    
def fourth_list_label(obj):
    label = QLabel("Text", obj)
    font = QFont()
    font.setBold(True)
    label.setFont(font)
    label.setGeometry(cp.FOURTH_LIST_X_START, cp.FOURTH_LIST_Y_START - 25, cp.FOURTH_LIST_WIDTH, 20)
    return
    
def fourth_list(obj):
    ll = QListWidget(obj)
    ll.setGeometry(cp.FOURTH_LIST_X_START, cp.FOURTH_LIST_Y_START, cp.FOURTH_LIST_WIDTH, cp.FOURTH_LIST_HEIGHT)
    ll.clicked.connect(obj.on_click_fourth_list)
    return ll

def fifth_list_label(obj):
    label = QLabel("Interval", obj)
    font = QFont()
    font.setBold(True)
    label.setFont(font)
    label.setGeometry(cp.FIFTH_LIST_X_START, cp.FIFTH_LIST_Y_START - 25, cp.FIFTH_LIST_WIDTH, 20)
    return

def fifth_list(obj):
    ll = QListWidget(obj)
    ll.setGeometry(cp.FIFTH_LIST_X_START, cp.FIFTH_LIST_Y_START, cp.FIFTH_LIST_WIDTH, cp.FIFTH_LIST_HEIGHT)
    ll.clicked.connect(obj.on_click_fifth_list)
    return ll

def sixth_list_label(obj):
    label = QLabel("Next step", obj)
    font = QFont()
    font.setBold(True)
    label.setFont(font)
    label.setGeometry(cp.SIXTH_LIST_X_START, cp.SIXTH_LIST_Y_START - 25, cp.SIXTH_LIST_WIDTH, 20)
    return

def sixth_list(obj):
    ll = QListWidget(obj)
    ll.setGeometry(cp.SIXTH_LIST_X_START, cp.SIXTH_LIST_Y_START, cp.SIXTH_LIST_WIDTH, cp.SIXTH_LIST_HEIGHT)
    ll.clicked.connect(obj.on_click_sixth_list)
    return ll

def point_axis(obj):
    btn = QPushButton(obj)
    btn.setText("set axis")
    btn.setGeometry(cp.POINT_AXIS_X_START, cp.POINT_AXIS_Y_START, cp.POINT_AXIS_WIDTH, cp.POINT_AXIS_HEIGHT)
    btn.clicked.connect(obj.on_click_axis)
    return btn

def set_image(obj):
    btn = QPushButton(obj)
    btn.setText("set image axis")
    btn.setGeometry(cp.SET_IMAGE_X_START, cp.SET_IMAGE_Y_START, cp.SET_IMAGE_WIDTH, cp.SET_IMAGE_HEIGHT)
    btn.clicked.connect(obj.on_click_set_image)
    return btn

def set_relative_dist(obj):
    btn = QPushButton(obj)
    btn.setText("set pos from image axis")
    btn.setGeometry(cp.SET_RELATIVE_DIST_X_START, cp.SET_RELATIVE_DIST_Y_START, cp.SET_RELATIVE_DIST_WIDTH, cp.SET_RELATIVE_DIST_HEIGHT)
    btn.clicked.connect(obj.on_click_set_relative_dist)
    return btn

def set_excel_file(obj):
    btn = QPushButton(obj)
    btn.setText("excel")
    btn.setGeometry(cp.SET_EXCEL_FILE_X_START, cp.SET_EXCEL_FILE_Y_START, cp.SET_EXCEL_FILE_WIDTH, cp.SET_EXCEL_FILE_HEIGHT)
    btn.clicked.connect(obj.on_click_excel_file)
    return btn

def set_keypress(obj):
    textbox = QLineEdit(obj)    
    textbox.setGeometry(cp.SET_KEYPRESS_X_START, cp.SET_KEYPRESS_Y_START, cp.SET_KEYPRESS_WIDTH, cp.SET_KEYPRESS_HEIGHT)
    return textbox

def keypress_apply_button(obj):
    btn = QPushButton(obj)
    btn.setText("apply")
    btn.setGeometry(cp.KEYPRESS_APPLY_BUTTON_X_START, cp.KEYPRESS_APPLY_BUTTON_Y_START, cp.KEYPRESS_APPLY_BUTTON_WIDTH, cp.KEYPRESS_APPLY_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_keypress_apply)
    return btn

def set_interval(obj):
    textbox = QLineEdit(obj)    
    textbox.setGeometry(cp.SET_INTERVAL_X_START, cp.SET_INTERVAL_Y_START, cp.SET_INTERVAL_WIDTH, cp.SET_INTERVAL_HEIGHT)
    return textbox

def interval_apply_button(obj):
    btn = QPushButton(obj)
    btn.setText("apply")
    btn.setGeometry(cp.INTERVAL_APPLY_BUTTON_X_START, cp.INTERVAL_APPLY_BUTTON_Y_START, cp.INTERVAL_APPLY_BUTTON_WIDTH, cp.INTERVAL_APPLY_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_interval_apply)
    return btn

def set_next_step(obj):
    textbox = QLineEdit(obj)    
    textbox.setGeometry(cp.SET_NEXT_STEP_X_START, cp.SET_NEXT_STEP_Y_START, cp.SET_NEXT_STEP_WIDTH, cp.SET_NEXT_STEP_HEIGHT)
    return textbox

def next_step_apply_button(obj):
    btn = QPushButton(obj)
    btn.setText("apply")
    btn.setGeometry(cp.NEXT_STEP_APPLY_BUTTON_X_START, cp.NEXT_STEP_APPLY_BUTTON_Y_START, cp.NEXT_STEP_APPLY_BUTTON_WIDTH, cp.NEXT_STEP_APPLY_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_next_step_apply)
    return btn
    
def execute(obj):
    btn = QPushButton(obj)
    btn.setText("execute")
    btn.clicked.connect(obj.on_click_execute)
    btn.setGeometry(cp.EXECUTE_X_START, cp.EXECUTE_Y_START, cp.EXECUTE_WIDTH, cp.EXECUTE_HEIGHT)
    return btn

def save(obj):
    btn = QPushButton(obj)
    btn.setText("save")
    btn.clicked.connect(obj.on_click_save)
    btn.setGeometry(cp.SAVE_X_START, cp.SAVE_Y_START, cp.SAVE_WIDTH, cp.SAVE_HEIGHT)
    return btn

def register_add_button(obj):
    btn = QPushButton(obj)
    btn.setText("register")
    btn.setGeometry(cp.REGISTER_ADD_BUTTON_X_START, cp.REGISTER_ADD_BUTTON_Y_START, cp.REGISTER_ADD_BUTTON_WIDTH, cp.REGISTER_ADD_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_register_add)
    return btn

def register_delete_button(obj):
    btn = QPushButton(obj)
    btn.setText("delete")
    btn.setGeometry(cp.REGISTER_DELETE_BUTTON_X_START, cp.REGISTER_DELETE_BUTTON_Y_START, cp.REGISTER_DELETE_BUTTON_WIDTH, cp.REGISTER_DELETE_BUTTON_HEIGHT)
    btn.clicked.connect(obj.on_click_register_delete)
    return btn

def register_list(obj):
    ll = QListWidget(obj)
    ll.setGeometry(cp.REGISTER_LIST_X_START, cp.REGISTER_LIST_Y_START, cp.REGISTER_LIST_WIDTH, cp.REGISTER_LIST_HEIGHT)
    ll.clicked.connect(obj.on_click_register_list)
    return ll

def register_save(obj):
    btn = QPushButton(obj)
    btn.setText("save")
    btn.clicked.connect(obj.on_click_register_save)
    btn.setGeometry(cp.REGISTER_SAVE_X_START, cp.REGISTER_SAVE_Y_START, cp.REGISTER_SAVE_WIDTH, cp.REGISTER_SAVE_HEIGHT)
    return btn

def captured_image_toggle(obj):
    btn = QPushButton(obj)
    btn.setText("captured image")
    btn.clicked.connect(obj.on_click_captured_image_toggle)
    btn.setGeometry(cp.CAPTURED_IMAGE_TOGGLE_X_START, cp.CAPTURED_IMAGE_TOGGLE_Y_START, cp.CAPTURED_IMAGE_TOGGLE_WIDTH, cp.CAPTURED_IMAGE_TOGGLE_HEIGHT)
    return btn

def adjust_axis(obj):
    btn = QPushButton(obj)
    btn.setText("adjust")
    btn.clicked.connect(obj.on_click_adjust_axis)
    btn.setGeometry(cp.ADJUST_AXIS_X_START, cp.ADJUST_AXIS_Y_START, cp.ADJUST_AXIS_WIDTH, cp.ADJUST_AXIS_HEIGHT)
    return btn
