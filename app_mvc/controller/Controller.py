from view.View import View
from .lib.thread import Thread


class Controller:
    def __init__(self, model):
        self.model = model
        self.view = View(self, model)
        self.view.show()
        self._threads = []
        self.read_database()

    def read_database(self):
        self.model.read_database()

    def _start_thread(self, method, data, signal):
        thread = Thread(method, data)
        self._threads.append(thread)
        thread.downloaded.connect(signal, thread.connection)
        thread.start()

    def run_parser(self):
        text = self.view.get_text()
        self.view.disable_search()
        self._start_thread(self.model.parser.parse, text, self._searched)

    def download_file(self):
        data = self.view.get_selected_data()
        for el in data:
            self._start_thread(
                self.model.connection.download, el, self._downloaded)

    def selection_changed(self):
        if self.view.is_row_selected():
            return self.view.enable_download()
        return self.view.disable_download()

    def _searched(self, results):
        self.view.show_search_result(results)

    def _downloaded(self, result):
        if result:
            self._start_thread(
                self.model.file_writer.write, result, self._writed)

    def _writed(self, result):
        title = result["name"]
        author = result["author"]
        url = result["url"]
        book = self.model.entity(self.model.counter, title, author, url)
        self.model.mapper.insert(book)
        self.model.identity_map.add_book(book)
        self.model.notify_observers()
        self.model.increment_counter()
