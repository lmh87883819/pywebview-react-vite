import webview
import os
import requests


class Api:
    def toogle_fullscreen(self):
        webview.windows[0].toggle_fullscreen()


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
    if exists('./gui/index.html'):  # frozen pyinstaller
        return './gui/index.html'

    if exists('../gui/index.html'):  # dev mode
        return '../gui/index.html'

    raise Exception('No entry point for front end found')


entry_point = get_entrypoint()

if __name__ == '__main__':
    api = Api()
    
    window = webview.create_window(
        'Pywebview React Vite', entry_point, js_api=api)

    # http server serve local file since edgeHTML doesn't allow local file
    webview.start(debug=True, http_server=True) 


print(__name__)
