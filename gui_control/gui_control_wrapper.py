from pyautogui import press, typewrite, hotkey
import time

PRESS_SPEED_FACTOR = 0.1

def press_hanguel_key():
    time.sleep(PRESS_SPEED_FACTOR)
    press('hanguel')
    time.sleep(PRESS_SPEED_FACTOR)
    
def write_text(text):
    time.sleep(PRESS_SPEED_FACTOR)
    typewrite(text, interval=0.3)
    
def press_key(text):
    time.sleep(PRESS_SPEED_FACTOR)
    press(text)
    
def press_ctrl_a():
    time.sleep(PRESS_SPEED_FACTOR)
    hotkey('ctrl', 'a')
    time.sleep(PRESS_SPEED_FACTOR)

def press_ctrl_c():
    time.sleep(PRESS_SPEED_FACTOR)
    hotkey('ctrl', 'c')
    time.sleep(PRESS_SPEED_FACTOR)

def press_ctrl_v():
    time.sleep(PRESS_SPEED_FACTOR)
    hotkey('ctrl', 'v')
    time.sleep(PRESS_SPEED_FACTOR)

def press_del():
    time.sleep(PRESS_SPEED_FACTOR)
    press('del')
    time.sleep(PRESS_SPEED_FACTOR)

def press_home():
    time.sleep(PRESS_SPEED_FACTOR)
    press('home')
    time.sleep(PRESS_SPEED_FACTOR)

def press_end():
    time.sleep(PRESS_SPEED_FACTOR)
    press('end')
    time.sleep(PRESS_SPEED_FACTOR)

def press_enter():
    time.sleep(PRESS_SPEED_FACTOR)
    press('enter')
    time.sleep(PRESS_SPEED_FACTOR)

def press_backspace():
    time.sleep(PRESS_SPEED_FACTOR)
    press('backspace')
    time.sleep(PRESS_SPEED_FACTOR)
    
def press_tab():
    time.sleep(PRESS_SPEED_FACTOR)
    press('tab')
    time.sleep(PRESS_SPEED_FACTOR)

def press_shift():
    time.sleep(PRESS_SPEED_FACTOR)
    press('shift')
    time.sleep(PRESS_SPEED_FACTOR)

def press_altright():
    time.sleep(PRESS_SPEED_FACTOR)
    press('altright')
    time.sleep(PRESS_SPEED_FACTOR)    

def press_capslock():
    time.sleep(PRESS_SPEED_FACTOR)
    press('capslock')
    time.sleep(PRESS_SPEED_FACTOR)

def press_page_down():
    time.sleep(PRESS_SPEED_FACTOR)
    press('pagedown')
    time.sleep(PRESS_SPEED_FACTOR)

def press_down():
    time.sleep(PRESS_SPEED_FACTOR)
    press('down')
    time.sleep(PRESS_SPEED_FACTOR)
