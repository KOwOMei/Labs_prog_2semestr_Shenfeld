import os
from PIL import Image, ImageFilter

filename = input("Введите имя файла: ")
im_1 = Image.open(filename)

im_1.show()

width, height = im_1.size
format = im_1.format
mode = im_1.mode

print(f"Ширина: {width}\nВысота: {height}\nФормат: {format}\nЦветовая модель: {mode}")

thumbnail_size = (int(im_1.width / 3), int(im_1.height / 3))
thumbnail_im = im_1.copy()
thumbnail_im.thumbnail(thumbnail_size)

horizontal_flip_im = im_1.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
vertical_flip_im = im_1.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)

thumbnail_im.save('thumbnail_' + filename)
horizontal_flip_im.save('horizontal_flip_' + filename)
vertical_flip_im.save('vertical_flip_' + filename)

folder_path = input("Введите путь к папке: ")

files = [f for f in os.listdir(folder_path) if f.endswith('.jpeg')]

if not os.path.exists('output'):
    os.makedirs('output')

for file in files:
    original_im = Image.open(os.path.join(folder_path, file))
    filtered_im = original_im.filter(ImageFilter.MinFilter)
    filtered_im.save(os.path.join('output', file))


parent_image_filename = input("Введите имя файла, на который нужно наложить водяной знак: ")
watermark_filename = input("Введите имя файла с водяным знаком: ")

parent_image = Image.open(parent_image_filename)
watermark = Image.open(watermark_filename)

watermark_size = (int(parent_image.width / 3), int(parent_image.height / 3))
watermark.thumbnail(watermark_size)

x = parent_image.width - watermark.width
y = parent_image.height - watermark.height

parent_image.paste(watermark, (x,y), watermark)
parent_image.save('watermarked_' + parent_image_filename)
