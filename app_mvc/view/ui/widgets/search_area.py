from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QTableView,
    QHeaderView)
from .area import Area


class SearchArea(Area):
    color = "white"

    def __init__(self):
        super().__init__(self.color)
        self.search = QLineEdit()
        self.search_button = QPushButton("Search")
        self.download_button = QPushButton("Download")
        self.table = QTableView()
        self.model = QStandardItemModel()
        self.initUI()

    def initUI(self):
        super().initUI()
        WidgetLayout(
            self,
            self.search,
            self.search_button,
            self.download_button,
            self.table,
            self.model)

    def clear_model(self):
        self.model.clear()

    def enable_search(self):
        self.search_button.setEnabled(True)
        self.search.setEnabled(True)

    def disable_search(self):
        self.search_button.setDisabled(True)
        self.search.setDisabled(True)

    def enable_download(self):
        self.download_button.setEnabled(True)

    def disable_download(self):
        self.download_button.setDisabled(True)

    def get_selected_rows(self):
        return self.table.selectionModel().selectedRows()

    def get_data_from_selected(self):
        selected = self.get_selected_rows()
        li = []
        for index in sorted(selected):
            row = index.row()
            href = self.model.data(self.model.index(row, 0))
            name = self.model.data(self.model.index(row, 1))
            author = self.model.data(self.model.index(row, 2))
            li.append({"url": href, "name": name, "author": author})
        return li

    def refresh(self, data):
        self.model.clear()
        i = 0
        for el in data:
            j = 0
            for value in el.values():
                item = QStandardItem(value)
                self.model.setItem(i, j, item)
                j += 1
            i += 1
        self.enable_search()


class WidgetLayout(QVBoxLayout):
    def __init__(self, parent, search, search_button, download_button, table, model):
        super().__init__(parent)
        self.initUI(search, search_button, download_button, table, model)

    def initUI(self, search, search_button, download_button, table, model):
        search_area = SearchAreaLayout(search, search_button)
        self.addLayout(search_area)
        table_area = TableAreaLayout(table, model, download_button)
        self.addLayout(table_area)


class SearchAreaLayout(QHBoxLayout):
    def __init__(self, search, search_button):
        super().__init__()
        self.initUI(search, search_button)

    def initUI(self, search, search_button):
        self.addWidget(search)
        self.addWidget(search_button)


class TableAreaLayout(QVBoxLayout):
    def __init__(self, table, model, download_button):
        super().__init__()
        self.initUI(table, model, download_button)

    def initUI(self, table, model, download_button):
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(model)
        self.addWidget(table)
        self.addWidget(download_button)
