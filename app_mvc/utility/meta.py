from PyQt5.QtCore import QObject
from abc import ABCMeta

pyqtWrapperType = type(QObject)


class ViewQtObserverMeta(pyqtWrapperType, ABCMeta):
    pass
