# 调整图片大小

from PIL import Image

input_image_path = "D:/Temp/app/dazai.png"
output_image_path = "D:/Temp/app/dazai.png"
max_width = 200
max_height = 500
scale_factor = 3

# 调整图片大小
def resize_image(input_image_path, output_image_path,max_width,max_height):
    original_image = Image.open(input_image_path)
    original_width, original_height = original_image.size
    aspect_ratio = float(original_width) / float(original_height)

    if original_width > original_height:
        new_width = min(max_width,original_width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(max_height,original_height)
        new_width = int(new_height * aspect_ratio)
    resized_image = original_image.resize((new_width, new_height),Image.ANTIALIAS)
    resized_image.save(output_image_path)

# 按比例缩小图片,缩小为原来的n倍
def resize_image2(input_image_path,output_image_path,scale_factor):
    original_image = Image.open(input_image_path)
    original_width,original_height = original_image.size

    new_width = int(original_width / scale_factor)
    new_height = int(original_height / scale_factor)

    resized_image = original_image.resize((new_width,new_height),Image.ANTIALIAS)
    resized_image.save(output_image_path)

resize_image2(input_image_path,output_image_path,scale_factor)