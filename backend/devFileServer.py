from flask import Flask
from flask import send_file
from flask import request
import urllib.parse
import os
import mimetypes
from flask import request
import os
import signal
from flask_cors import CORS


class DevFileServer:
    def startDevFileServer(self):
        app = Flask(__name__)
        CORS(app, origins=["http://localhost:3000"])

        @app.route('/shutdown')
        def shutdown():
            os.kill(os.getpid(), signal.SIGINT)

        @app.route('/file')
        def hello():
            raw_path = request.args.get('path')
            decoded_url = urllib.parse.unquote(raw_path)
            path = os.path.abspath(decoded_url)
            mime_type = mimetypes.guess_type(path)[0]

            return send_file(open(path, "rb"), mimetype=mime_type, conditional=True)

        app.run()


# Only run this file on development
# On production pywebview will use http_server to host local file on random port
devFileServer = DevFileServer()
devFileServer.startDevFileServer()


