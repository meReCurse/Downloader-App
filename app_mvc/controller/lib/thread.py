from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread, pyqtSignal


class Thread(QThread):
    downloaded = pyqtSignal(object)

    def __init__(self, method, req, parent=None):
        self.method = method
        self.req = req
        self.connection = Qt.QueuedConnection
        super().__init__(parent)

    def run(self):
        result = self.method(self.req)
        self.downloaded.emit(result)
