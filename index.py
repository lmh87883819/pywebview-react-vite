import webview
import os
import requests


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    # On packaged app
    if exists('../Resources/gui/index.html'):  # frozen py2app
        return '../Resources/gui/index.html'

    # Using vite build
    if exists('./gui/index.html'):
        return './gui/index.html'

    # dev
    try:
        url = 'http://localhost:3000'
        get = requests.get(url)
        if get.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        raise Exception('No index.html found')


entry_point = get_entrypoint()

if __name__ == '__main__':
    window = webview.create_window(
        'pywebview-vue boilerplate', entry_point)

    webview.start(debug=True, http_server=True)
