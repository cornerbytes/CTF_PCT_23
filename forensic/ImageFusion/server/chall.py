#!/usr/bin/env python3

from PIL import Image, ImageFont
from io import BytesIO

def pad_binary_data(binary_data, target_length):
    padding = target_length - len(binary_data)
    return binary_data + bytes([0] * padding)

f = open('flag.txt','r')
flag = f.read().strip()
f.close()

font_size = 36
font_filepath = "consola.ttf"
color = (12, 102, 158, 155)

font = ImageFont.truetype(font_filepath, size=font_size)

mask_image1 = font.getmask(flag[:(len(flag)//2)], "L")
mask_image2 = font.getmask(flag[(len(flag)//2):], "L")

img1 = Image.new("RGBA", mask_image1.size)
img1.im.paste(color, (0, 0) + mask_image1.size, mask_image1)

img2 = Image.new("RGBA", mask_image2.size)
img2.im.paste(color, (0, 0) + mask_image2.size, mask_image2)

img_bin1 = BytesIO()
img_bin2 = BytesIO()

img1.save(img_bin1, format='PNG')
img2.save(img_bin2, format='PNG')

img_bin1.seek(0)
img_bin2.seek(0)

img_bin1 = img_bin1.read()
img_bin2 = img_bin2.read()
max_length = max(len(img_bin1),len(img_bin2))
if len(img_bin1) < len(img_bin2):
    img_bin1 = pad_binary_data(img_bin1, max_length)
else:
    img_bin2 = pad_binary_data(img_bin2, max_length)

with open('stacked.png', 'wb') as chall:
    chall.write(img_bin1 + img_bin2)
chall.close()
