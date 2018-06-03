import pickle
import easygui
import os

def set_arr_from_data(obj, data):
    obj.action_arr = eval(data['action_arr'])
    obj.axis_arr = eval(data['axis_arr'])
    obj.class_arr = eval(data['class_arr'])
    obj.image_arr = eval(data['image_arr'])
    obj.relative_dist_arr = eval(data['relative_dist_arr'])
    obj.keypress_arr = eval(data['keypress_arr'])
    obj.interval_arr = eval(data['interval_arr'])
    obj.next_step_arr = eval(data['next_step_arr'])
    obj.excel_file_arr = eval(data['excel_file_arr'])
    obj.captured_image_arr = eval(data["captured_image_arr"])
    obj.image_portion_arr = eval(data["image_portion_arr"])

def load_file(obj):
    default_path = os.path.abspath("./save")
    path = easygui.fileopenbox(default=default_path + "\*.*")
    if path == None:
        return
    with open(path, 'rb') as f:
        data = pickle.load(f)
        set_arr_from_data(obj, data)
        obj.second_list.clear()
        obj.third_list.clear()
        obj.fourth_list.clear()
        obj.fifth_list.clear()
        obj.sixth_list.clear()
        for i in range(len(obj.axis_arr)):
            if obj.class_arr[i] != '':
                obj.third_list.addItem(obj.class_arr[i])
            else:
                obj.third_list.addItem(obj.axis_arr[i])
        for action in obj.action_arr:
            obj.second_list.addItem(action)

def load_file_in_register(obj):
    default_path = os.path.abspath("./save")
    path = easygui.fileopenbox(default=default_path + "\*.*")
    if path == None:
        return
    obj.data_file_arr.append(path)
    path_arr = path.split('\\')
    obj.register_list.addItem(path_arr[len(path_arr) - 1])

def load_file_in_scheduler(obj, path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
        set_arr_from_data(obj, data)
