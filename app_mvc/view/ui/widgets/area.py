from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSizePolicy


class Area(QWidget):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def initUI(self):
        self.set_background_color()
        self.stretch()

    def set_background_color(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), getattr(Qt, self.color))
        self.setPalette(p)

    def stretch(self):
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding)
