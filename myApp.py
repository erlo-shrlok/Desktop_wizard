# 加入GUI界面

import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QFileDialog
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.config_file = "config.txt"

        static_image_path = ""
        move_image_path = ""

        self.load_config()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('桌面精灵')

        btn = QPushButton('选择静态图片',self)
        btn.clicked.connect(self.openFileNameDialog)

        btn2 = QPushButton('选择GIF',self)
        btn2.clicked.connect(self.openFileNameDialog2)

        btn3 = QPushButton('开始', self)
        btn3.clicked.connect(self.start)

        layout = QVBoxLayout() # 创建一个垂直布局对象
        layout.addWidget(btn) # 将按钮添加到布局中
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout) # 将布局设置为主窗口的布局

        self.show() # 显示主窗口

    def openFileNameDialog(self):
        options = QFileDialog.Options() # 创建文件对话框的选择对象
        fileName,_ = QFileDialog.getOpenFileName(self,"选择静态图片","","All Files (*);;Python Files (*.py)",options=options)
        # 打开文件对话框，获取选择的文件名和过滤器，存储在变量 fileName 和 _ 中
        if fileName:
            self.static_image_path = fileName
            self.save_config()

    def openFileNameDialog2(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"选择GIF","","GIF Files (*.gif)",options=options)
        if fileName:
            self.move_image_path = fileName
            self.save_config()

    def start(self):
        if self.static_image_path and self.move_image_path:
            # 设置 startupinfo
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen(['moveit.exe',self.static_image_path,self.move_image_path],startupinfo=startupinfo)
            QCoreApplication.instance().quit()

    def save_config(self):
        with open(self.config_file,'w') as f:
            f.write(self.static_image_path + '\n')
            f.write(self.move_image_path + '\n')

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file,'r') as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    self.static_image_path = lines[0].strip()
                    self.move_image_path = lines[1].strip()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 创建应用程序对象
    ex = MyApp() # 创建自定义的窗口对象
    sys.exit(app.exec_()) # 运行应用程序的事件循环，直到退出程序