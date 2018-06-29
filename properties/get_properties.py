def get_image_range():
    with open('./files/properties/config.properties', 'r', encoding='utf8') as f:
        lines = f.readlines()
        LEFT_RANGE = int(lines[0].split("=")[1].replace("\n", ""))
        RIGHT_RANGE = int(lines[1].split("=")[1].replace("\n", ""))
        TOP_RANGE = int(lines[2].split("=")[1].replace("\n", ""))
        BOTTOM_RANGE = int(lines[3].split("=")[1].replace("\n", ""))
        
    return LEFT_RANGE, RIGHT_RANGE, TOP_RANGE, BOTTOM_RANGE
