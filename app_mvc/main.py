import sys
import json
from PyQt5.QtWidgets import QApplication

from model.Model import Model
from controller.Controller import Controller


def read_settings():
    with open('conf.json', 'r') as conf:
        data = conf.read()
    return json.loads(data)


def main():
    settings = read_settings()
    app = QApplication(sys.argv)
    print(settings)
    model = Model(settings['proxy'], settings['database_file'])
    controller = Controller(model)
    app.exec_()


if __name__ == "__main__":
    sys.exit(main())
