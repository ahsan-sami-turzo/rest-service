import http.server
import json
import socketserver

# List of cities in Sweden
cities = ["Stockholm", "Gothenburg", "Malmö", "Uppsala", "Västerås", "Örebro", "Linköping"]


class RESTRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(cities).encode())


# Set the server's port
port = 9091
httpd = socketserver.TCPServer(("", port), RESTRequestHandler)

print(f"REST Services running on port {port}")
httpd.serve_forever()
