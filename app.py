from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"🔥 App Running Successfully on EC2 via Docker 🔥")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), handler)
    print("Server started on port 5000...")
    server.serve_forever()
