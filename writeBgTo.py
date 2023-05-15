# 设置白色图片背景为透明，并图片大小

from PIL import Image

input_image_path = "chuyetalk_2.png"
output_image_path = "chuyetalk.png"

# 设置图像白色背景为透明
def remove_white_background(input_image_path, output_image_path):
    original_image = Image.open(input_image_path)
    image_with_transparency = original_image.convert("RGBA")
    data = image_with_transparency.getdata()

    new_data = []
    for item in data:
        if item[0] == 255 and item[1] == 255 and item[2] ==255:
            new_data.append((255,255,255,0))
        else:
            new_data.append(item)
    image_with_transparency.putdata(new_data)
    image_with_transparency.save(output_image_path,"PNG")


remove_white_background(output_image_path,output_image_path)