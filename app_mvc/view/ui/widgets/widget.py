from PyQt5.QtWidgets import QWidget, QHBoxLayout
from .search_area import SearchArea
from .database_area import DatabaseArea


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.search_widget = SearchArea()
        self.db_widget = DatabaseArea()
        self.initUI()

    def initUI(self):
        self.layout = MainWidgetLayout(
            self,
            self.search_widget,
            self.db_widget)


class MainWidgetLayout(QHBoxLayout):
    def __init__(self, parent, search_widget, db_widget):
        super().__init__(parent)
        self.initUI(search_widget, db_widget)

    def initUI(self, search_widget, db_widget):
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.addWidget(search_widget, 2)
        self.addWidget(db_widget, 1)
