import PIL.ImageGrab
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import datetime
import unicodedata
from properties import get_properties

LEFT_RANGE, RIGHT_RANGE, TOP_RANGE, BOTTOM_RANGE = get_properties.get_image_range() 

def save_image(image_path):
    im = PIL.Image.open(image_path)
    im.show()

def capture_image(obj, pos, text):
    now = datetime.datetime.now()
    file_name = now.strftime("%Y%m%d%H%M%S") + '.jpg'
    image_path = './files/save/image/' + file_name
    img = PIL.ImageGrab.grab()
    width, height = img.size
    if text != None and text != '':
        draw = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype("./files/fonts/ARIALUNI.TTF", 30)
        draw.text((pos[0] + 10, pos[1] + 10), unicodedata.normalize("NFC", text), (255,0,0), font=font)    
    pix = img.load()
    for i in range(width):
        for j in range(height):
            if i < pos[0] + 10 and i > pos[0] - 10:
                if j < pos[1] + 10 and j > pos[1] - 10:
                    if i < pos[0] + 7 and i > pos[0] - 7 and j < pos[1] + 7 and j > pos[1] - 7:
                        continue                
                    pix[i, j] = (255, 0, 0)
    img2 = img.crop((pos[0] - 120, pos[1] - 60, pos[0] + 120, pos[1] + 60))
    image_portion_path = './files/save/image/p_' + file_name
    img.save(image_path)
    img2.save(image_portion_path)
    return image_path, image_portion_path

def get_image(obj, p):
    rgb = PIL.ImageGrab.grab().load()
    size = PIL.ImageGrab.grab().size
    width = LEFT_RANGE + RIGHT_RANGE + 1
    height = TOP_RANGE + BOTTOM_RANGE + 1
    img_arr = []
    for j in range(height):
        x_arr = []
        for i in range(width):
            x_arr.append(rgb[0, 0])
        img_arr.append(x_arr)
    axis_x = int(p.split(",")[0])
    axis_y = int(p.split(",")[1])
    frm_x = axis_x - LEFT_RANGE
    to_x = axis_x + RIGHT_RANGE
    frm_y = axis_y - TOP_RANGE
    to_y = axis_y + BOTTOM_RANGE
    x = 0
    y = 0
    for jj in range(size[1]):
        updated = False
        if jj < frm_y or jj > to_y:
            continue
        for ii in range(size[0]):
            if ii < frm_x or ii > to_x:
                continue
            img_arr[x][y] = rgb[ii, jj]
            x += 1
            updated = True
        if updated == True:
            y += 1
            x = 0
    return img_arr

def compare_image(rgb, img, ii, jj, width, height):
    i = ii
    j = jj
    x = 0
    y = 0
    while j < jj + height:
        while i < ii + width:
            a = rgb[i, j]
            b = img[x][y]
            if abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) > 10:
                return False
            x += 1
            i += 1
        y += 1
        j += 1
        x = 0
        i = ii
    return True

def scan_image(obj, img):
    rgb = PIL.ImageGrab.grab().load()
    size = PIL.ImageGrab.grab().size
    width = LEFT_RANGE + RIGHT_RANGE + 1
    height = TOP_RANGE + BOTTOM_RANGE + 1
    for jj in range(size[1]):
        if jj > size[1] - height:
            continue
        for ii in range(size[0]):
            if ii > size[0] - width:
                continue
            if compare_image(rgb, img, ii, jj, width, height):
                return [ii + LEFT_RANGE, jj + TOP_RANGE]    
    return None

def is_equal_to_image(obj, img, axis):
    rgb = PIL.ImageGrab.grab().load()
    width = LEFT_RANGE + RIGHT_RANGE + 1
    height = TOP_RANGE + BOTTOM_RANGE + 1
    if compare_image(rgb, img, int(axis[0]) - LEFT_RANGE, int(axis[1]) - TOP_RANGE, width, height):
        return True
    else:
        return False
