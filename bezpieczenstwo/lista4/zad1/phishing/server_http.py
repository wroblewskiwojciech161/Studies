from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b' halo halo tutaj server HTTP')


httpd = HTTPServer(('www.moj.serwer.pl', 5000), SimpleHTTPRequestHandler)


httpd.serve_forever()
