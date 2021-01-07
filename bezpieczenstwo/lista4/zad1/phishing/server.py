from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b' halo halo tutaj server HTTPS')


httpd = HTTPServer(('www.moj.serwer.pl', 5000), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="privkeyA.pem",
                               certfile='certA.crt', server_side=True)

httpd.serve_forever()
