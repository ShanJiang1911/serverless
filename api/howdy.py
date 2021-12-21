from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "test/plain")
        self.end_headers()
        message = "Howdy"
        self.wfile.write(message.encode())
        return