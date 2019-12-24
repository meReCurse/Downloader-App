

from PyQt5.QtWidgets import QMainWindow
from utility.observer import Observer
from utility.meta import ViewQtObserverMeta
from .ui.window import Window


class View(QMainWindow, Observer, metaclass=ViewQtObserverMeta):
    def __init__(self, controller, model, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.controller = controller
        self.model = model
        self.ui = Window()
        self.model.add_observer(self)
        self.initActions()

    def initActions(self):
        self.ui.widget\
            .search_widget\
            .search\
            .returnPressed.connect(self.controller.run_parser)
        self.ui.widget\
            .search_widget\
            .search_button\
            .clicked.connect(self.controller.run_parser)
        self.ui.widget\
            .search_widget\
            .download_button\
            .clicked.connect(self.controller.download_file)
        self.ui.widget\
            .search_widget\
            .table.selectionModel()\
            .selectionChanged.connect(self.controller.selection_changed)

    def model_is_changed(self):
        data = self.model.identity_map.get_books()
        self.ui.widget.db_widget.refresh(data)

    def show(self):
        self.ui.show()

    def show_search_result(self, result):
        self.ui.widget.search_widget.refresh(result)

    def get_selected_data(self):
        return self.ui.widget.search_widget.get_data_from_selected()

    def get_text(self):
        return self.ui.widget.search_widget.search.text()

    def disable_search(self):
        self.ui.widget.search_widget.disable_search()

    def is_row_selected(self):
        return bool(self.ui.widget.search_widget.get_selected_rows())

    def enable_download(self):
        self.ui.widget.search_widget.enable_download()

    def disable_download(self):
        self.ui.widget.search_widget.disable_download()
