
# extract a tar.gz file with the tarfile module
import tarfile
 
import os
import sys
import uuid
import shutil
from pyramid.response import Response
import argparse

target = None

def upload_and_extract(request):
    tfile = tarfile.open(fileobj=request.POST['file'].file, mode='r:gz')
    tfile.extractall(target)
    return Response('OK')

from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--port', metavar='N', type=int,
                        help='port to listen on')
    parser.add_argument('--target', dest='target',
                   help='target')

    args = parser.parse_args()
    target = args.target

    config = Configurator()
    config.add_route('up', '/')
    config.add_view(upload_and_extract, route_name='up')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', args.port, app)
    server.serve_forever()
   
