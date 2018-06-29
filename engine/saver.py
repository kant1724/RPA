import pickle
import easygui
import os

def save_file(obj):
    default_path = os.path.abspath("./files/save")
    path = easygui.filesavebox(default=default_path + "\*.dat")
    if path == None:
        return
    with open(path, 'wb') as f:
        data = {}
        data["action_arr"] = str(obj.action_arr)
        data["axis_arr"] = str(obj.axis_arr)
        data["class_arr"] = str(obj.class_arr)
        data["keypress_arr"] = str(obj.keypress_arr)
        data["interval_arr"] = str(obj.interval_arr)
        data["next_step_arr"] = str(obj.next_step_arr)
        data["image_arr"] = str(obj.image_arr)
        data["relative_dist_arr"] = str(obj.relative_dist_arr)
        data["excel_file_arr"] = str(obj.excel_file_arr)
        data["captured_image_arr"] = str(obj.captured_image_arr)
        data["image_portion_arr"] = str(obj.image_portion_arr)
        
        pickle.dump(data, f)

def save_register_file(obj):
    default_path = os.path.abspath("./files/save")
    path = easygui.filesavebox(default=default_path + "\*.txt")
    if path == None:
        return
    with open(path, 'w') as f:
        for data_file_path in obj.data_file_arr:
            f.write(data_file_path + "\n")
