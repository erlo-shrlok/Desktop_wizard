# 桌面精灵1

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QPoint
from PIL import Image

input_image_path = "D:/Temp/test2.png"
output_image_path = "resized_image.png"
max_width = 200
max_height = 500

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

resize_image(input_image_path,output_image_path,max_width,max_height)

remove_white_background(output_image_path,output_image_path)

class DesktopSprite(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置卡通人物图片
        self.label = QLabel(self)
        pixmap = QPixmap(output_image_path)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(),pixmap.height())

        # 设置窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 调整窗口大小以适应图片
        self.resize(pixmap.width(),pixmap.height())

        # 设置窗口位置
        self.move(200,300)

        self.show()

        # 初始化鼠标拖动变量
        self.dragPosition = QPoint()

    # 重写鼠标按下事件
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    # 重写鼠标移动事件
    def mouseMoveEvent(self,event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sprite = DesktopSprite()
    sys.exit(app.exec_())
