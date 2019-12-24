from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow
from .widgets.widget import Widget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self._title = 'tor_book_downloader v0.0.1'
        self._size = (640, 480)
        self._color = '#000000'
        self.widget = Widget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self._title)
        self.resize(*self._size)
        self._centrify()
        self._colorize()
        self.setCentralWidget(self.widget)
        self.showMaximized()
        self.widget.search_widget.disable_download()

    def _centrify(self):
        desktop = QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

    def _colorize(self):
        brush = QBrush(QColor(self._color), Qt.SolidPattern)
        pal = self.palette()
        pal.setBrush(
            QPalette.Normal,
            QPalette.Window,
            brush)
        pal.setBrush(
            QPalette.Inactive,
            QPalette.Window,
            brush)
        self.setPalette(pal)
