import http.server
import socketserver
import socket

PORT = 8000

class TestMe():
    def take_five(self):
        return 5
    def port(self):
        return PORT

if __name__ == '__main__':
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            hostname = socket.gethostname()
            self.wfile.write(f"Hello from CI/CD Lab 9! My pod is: {hostname}\n".encode())

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
