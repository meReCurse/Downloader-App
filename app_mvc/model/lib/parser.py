import re
from bs4 import BeautifulSoup as BS
from abc import ABCMeta, abstractmethod


class AbstractParser(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, content):
        pass


class Parser(AbstractParser):
    __slots__ = '_type', '_url'

    def __init__(self, connection):
        self._type = 'html.parser'
        self._con = connection
        self._url = 'http://xfmro77i3lixucja.onion'

    def parse(self, search):
        self._con.start_session()
        response = self._con.connect(f'{self._url}/search/?q={search}&num=1')
        content = BS(response.content, self._type)
        quantity = self._get_books_quantity(content)
        if quantity:
            response = self._con.connect(f'{self._url}/search/?q={search}&num={quantity}')
            content = BS(response.content, self._type)
            return self._get_actual_data(content, quantity)

    def _get_books_quantity(self, content):
        data = content.find("ul", {"class": "pager"}).get_text()
        try:
            quantity = int(re.search(r'\S\d+\S', data).group(0))
            return quantity
        except AttributeError:
            pass

    def _get_actual_data(self, content, quantity) -> list:
        result = []
        for x in range(quantity):
            if x == 0:
                data = content.find("div", class_="row")
            else:
                data = data.find_next_sibling("div")

            file = data.find("a", class_="btn-inverse").get("href")
            url = f"http://xfmro77i3lixucja.onion/{file}"

            title = data.find("strong").get_text()
            autor_raw = str(data.find("br").next_element)
            autor = re.search(r"\S.*\S", autor_raw).group(0)

            result.append({"url": url, "title": title, "autor": autor})
        return result


URL_PARSERS_DICT = {
    'http://xfmro77i3lixucja.onion': Parser
}


if __name__ == "__main__":
    from connection import Connection
    con = Connection({
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
        }
    )

    parser = Parser(con)
    print(parser.parse("python"))
