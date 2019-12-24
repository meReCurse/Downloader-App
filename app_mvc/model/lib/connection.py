import requests
from abc import ABCMeta, abstractmethod
from fake_useragent import UserAgent


class AbstractConnection(metaclass=ABCMeta):
    @abstractmethod
    def start_session(self):
        pass

    @abstractmethod
    def connect(self, url):
        pass

    @abstractmethod
    def download(self, url):
        pass


class Connection(AbstractConnection):
    __slots__ = '_proxy', '_headers', '_session'

    def __init__(self, proxy):
        self._proxy = proxy
        self._headers = self._make_headers()
        self._session = None

    def start_session(self):
        self._session = requests.session()
        self._set_session_proxy()
        return self._session

    def connect(self, url: str, stream=False):
        request = self._session.get(url, stream=stream, headers=self._headers)
        return request

    def download(self, params, flag=True):
        request = self.connect(params['url'], flag)
        self._set_download_request_params(request)
        params["request"] = request
        return params

    def _make_headers(self):
        return {'User-Agent': UserAgent().random}

    def _set_session_proxy(self) -> None:
        self._session.proxies = self._proxy

    def _set_download_request_params(self, request) -> None:
        request.raise_for_status()
        request.raw.decode_content = True


if __name__ == '__main__':
    con = Connection({
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
        }
    )
    con.start_session()
    con.connect('https://www.google.com/')
