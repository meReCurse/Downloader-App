from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHeaderView,
    QTableView,)
from .area import Area


class DatabaseArea(Area):
    color = "white"

    def __init__(self):
        super().__init__(self.color)
        self.table = QTableView()
        self.model = QStandardItemModel()
        self.headers = ['title', 'author']
        self.initUI()

    def initUI(self):
        super().initUI()
        WidgetLayout(self, self.table, self.model)
        self.model.setHorizontalHeaderLabels(self.headers)

    def refresh(self, data):
        self.model.clear()
        attrs = self.headers
        for el in data:
            li = []
            for attr in attrs:
                item = QStandardItem(str(getattr(el, attr)))
                li.append(item)
            self.model.appendRow(li)


class WidgetLayout(QVBoxLayout):
    def __init__(self, parent, table, model):
        super().__init__(parent)
        self.initUI(table, model)

    def initUI(self, table, model):
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(model)
        self.addWidget(table)
