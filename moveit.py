import sys
import time
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt, QPoint

# 静态图片
static_image_path = "chuyetalk.png" if len(sys.argv) < 2 else sys.argv[1]

# 动态图片
move_image_path = "chuyetalk.gif" if len(sys.argv) < 3 else sys.argv[2]

class DesktopSprite(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置卡通人物图片
        self.label = QLabel(self)
        self.pixmap = QPixmap(static_image_path)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        # 设置动画
        self.movie = QMovie(move_image_path)
        self.movie.setScaledSize(self.label.size())
        self.movie.finished.connect(self.restore_pixmap)  # 连接 finished 信号到插槽

        # 设置窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 调整窗口大小以适应图片
        self.resize(self.pixmap.width(), self.pixmap.height())

        # 设置窗口位置
        self.move(200, 300)

        self.show()

        # 初始化点击时间和点击计数器
        self.last_click_time_left = 0
        self.last_click_time_right = 0

        # 初始化鼠标拖动变量
        self.dragPosition = None

    # 重写鼠标按下事件
    def mousePressEvent(self, event):
        current_time = time.time()

        if event.button() == Qt.LeftButton:  # 左键双击播放动画
            if current_time - self.last_click_time_left < 0.2:
                self.label.setMovie(self.movie)
                self.movie.start()
            self.last_click_time_left = current_time
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()

        elif event.button() == Qt.RightButton:  # 右键双击关闭窗口
            if current_time - self.last_click_time_right < 0.2:
                QApplication.quit()
            self.last_click_time_right = current_time

    # 重写鼠标移动事件
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.dragPosition is not None:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 插槽：恢复静态图片
    def restore_pixmap(self):
        self.label.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sprite = DesktopSprite()
    sys.exit(app.exec_())
