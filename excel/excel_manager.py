import easygui
import os
import pandas as pd

def set_excel_file(obj):
    default_path = os.path.abspath("./excel/files")
    obj.excel_file_path = easygui.fileopenbox(default=default_path + "\*.*")

def read_excel(obj):    
    if obj.excel_file_path == None or obj.excel_file_path == '':
        return ['']
    df = pd.read_excel(obj.excel_file_path, 'sheet', dtype=str)
    excel_data = {}
    excel_data_key = []
    for i in range(len(obj.keypress_arr)):
        text = obj.keypress_arr[i]
        if text[:1] == '$':
            val = df[df.columns[int(text[1:]) - 1]]
            excel_data[text] = val
            excel_data_key.append(text)
    max_len = 0
    for key in excel_data_key:
        max_len = max(max_len, len(excel_data[key]))
    res = []
    for i in range(max_len):
        data = {}
        for key in excel_data_key:
            if i >= len(excel_data[key]):
                data[key] = ''
            else:
                data[key] = excel_data[key][i]
        res.append(data)
    if len(res) == 0:
        for i in range(len(df)):
            res.append("")
    return res
