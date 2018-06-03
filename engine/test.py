import PIL.Image

img = PIL.Image.open('../save/image/20180522141710.jpg')
width, height = img.size
pix = img.load()
for i in range(width):
    for j in range(height):
        if i < 200 and j < 200:
            pix[i, j] = (255, 255, 255)

img.save('../save/image/new.jpg')