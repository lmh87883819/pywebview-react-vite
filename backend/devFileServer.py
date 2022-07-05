from tkinter.tix import Tree
from flask import Flask
from flask import send_file, Response
from flask import request
import urllib.parse
import os
import mimetypes
from flask import request
import os
import signal
from flask_cors import CORS
import re

Flask.use_x_sendfile = True


class DevFileServer:
    def startDevFileServer(self):
        app = Flask(__name__)
        CORS(app, origins=["http://localhost:3000"])

        @app.route('/shutdown')
        def shutdown():
            os.kill(os.getpid(), signal.SIGINT)

        @app.after_request
        def after_request(response):
            response.headers.add('Accept-Ranges', 'bytes')
            return response

        @app.route('/file')
        def hello():
            raw_path = request.args.get('path')
            decoded_url = urllib.parse.unquote(raw_path)
            path = os.path.abspath(decoded_url)
            mime_type = mimetypes.guess_type(path)[0]
            
            # Code below is from https://blog.asgaard.co.uk/2012/08/03/http-206-partial-content-for-flask-python
            # Send partial
            range_header = request.headers.get('Range', None)
            if not range_header: return send_file(path_or_file=open(path, "rb"), mimetype=mime_type)
            
            size = os.path.getsize(path)    
            byte1, byte2 = 0, None
            
            m = re.search('(\d+)-(\d*)', range_header)
            g = m.groups()
            
            if g[0]: byte1 = int(g[0])
            if g[1]: byte2 = int(g[1])

            length = size - byte1
            if byte2 is not None:
                length = byte2 + 1 - byte1
            
            data = None
            with open(path, 'rb') as f:
                f.seek(byte1)
                data = f.read(length)

            rv = Response(data, 
                206,
                mimetype=mimetypes.guess_type(path)[0], 
                direct_passthrough=True)
            rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))

            return rv

        app.run(debug=True)


# Only run this file on development
# On production pywebview will use http_server to host local file on random port
devFileServer = DevFileServer()
devFileServer.startDevFileServer()
