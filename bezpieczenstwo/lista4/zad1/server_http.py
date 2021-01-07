from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()


httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)


httpd.serve_forever()
