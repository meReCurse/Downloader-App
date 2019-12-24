import sys
import os
import re

sys.path.append(os.path.join(os.getcwd(), '..', '..'))


class FileWriter:
    __slot__ = 'path'

    def __init__(self):
        self.path = os.path.join(os.getcwd(), "downloads")

    def write(self, data):
        response = data["request"]
        ext = re.search(r"\w+$", data['url']).group(0)
        path = os.path.join(self.path, f"{data['name']}.{ext}")
        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return data
