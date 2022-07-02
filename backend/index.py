import webview
import os
import requests
from schema import *


class Api:
    def add_todo(self, title, content):
        print("Adding todo")
        Todo.create(title=title, content=content)

    def toogle_fullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def save_content(self):
        file_types = ('Image Files (*.bmp;*.jpg;*.gif)', 'All files (*.*)')
        results = webview.windows[0].create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        if not results:
            return

        return results

    def hello(self):
        a = webview.windows[0].original_url
        return a

    def hello_with_args(self, *args):
        return 'hello with args called, args:', args


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    # dev
    try:
        url = 'http://localhost:3000'
        get = requests.get(url)
        if get.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        print("Front end server is not running, trying front end build folder")

        # On packaged app
        if exists('../Resources/gui/index.html'):  # frozen py2app
            return '../Resources/gui/index.html'

        # Using vite build
        if exists('./gui/index.html'):  # pyinstaller
            return './gui/index.html'

        if exists('../gui/index.html'):  # dev mode
            return '../gui/index.html'

        raise Exception('No entry point for front end found')


entry_point = get_entrypoint()

if __name__ == '__main__':
    api = Api()

    # Sqlite database
    init_db()

    window = webview.create_window(
        'Pywebview React Vite', entry_point, js_api=api)

    # http server serve local file since edgeHTML doesn't allow local file
    webview.start(debug=True, http_server=True)
