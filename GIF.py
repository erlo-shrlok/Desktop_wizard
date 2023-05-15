# 将黑底GIF转换为透明底GIF

from PIL import Image, ImageSequence

# 加载GIF动画
gif = Image.open('chuye2.gif')

# 创建一个空列表来保存处理过的帧
frames = []

# 遍历每一帧
for frame in ImageSequence.Iterator(gif):
    # 将帧转换为RGBA格式
    frame_rgba = frame.convert('RGBA')

    # 创建一个新的帧来保存处理过的数据
    new_frame = Image.new('RGBA', frame_rgba.size)

    # 遍历帧中的每一个像素
    for x in range(frame_rgba.width):
        for y in range(frame_rgba.height):
            # 获取当前像素的颜色
            r, g, b, a = frame_rgba.getpixel((x, y))

            # 如果当前像素是黑色，则将其透明度设置为0
            if r == 0 and g == 0 and b == 0:
                new_frame.putpixel((x, y), (r, g, b, 0))
            else:
                new_frame.putpixel((x, y), (r, g, b, a))

    # 将处理过的帧添加到列表中
    frames.append(new_frame)

# 将处理过的帧重新组合成GIF动画并保存
frames[0].save('chuye22.gif', save_all=True, append_images=frames[1:], loop=0, disposal=2)
