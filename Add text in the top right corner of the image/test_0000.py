# -*- coding : utf-8-*-

from PIL import Image,ImageFont,ImageDraw
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    width, height = img.size
    draw.text((width-30, 0), '1', font=myfont, fill=(255,0,0))
    img.save('image/result.jpg', 'jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('image/test0000.png')
    add_num(image)
