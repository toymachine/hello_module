from bottle import route, run, static_file, abort, HTTPResponse

import sys
import os
import zipfile
import mimetypes

@route('/')
def index():
    return open('index.html')

@route('/favicon.ico')
def favicon():
    return static_file("favicon.ico", ".")

@route('/scripts/<filepath:path>')
def statics(filepath):
    for pkg in os.listdir('./pkgs'):
        pkg_path = os.path.join('pkgs', pkg)
        if os.path.isdir(pkg_path):
            response = static_file(filepath, root = pkg_path)
            if response.status in [200, 304]:
                return response
        elif os.path.isfile(pkg_path) and pkg_path.endswith('.zip'):
            zf = zipfile.ZipFile(pkg_path)
            try:
                content = zf.read(filepath)
                mimetype, _ = mimetypes.guess_type(filepath)
                return HTTPResponse(content, header = {'Content-Type': mimetype})
            except KeyError:          
                pass #file not found in this zip
            
    abort(404, "Not found")

run(host='localhost', port=8080)
