from http.server import HTTPServer,SimpleHTTPRequestHandler
from socketserver import BaseServer
import ssl

httpd = HTTPServer(('localhost', 4443),SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='../serverCreds/server-public-key.pem',keyfile='../serverCreds/server-private-key.pem',server_side=True)
httpd.serve_forever()
