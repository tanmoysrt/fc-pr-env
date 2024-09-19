import http.server
import socketserver
import json
import os
import signal
import sys
from urllib.parse import urlparse, parse_qs, unquote

PORT = 3000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Print request details
        print(f"Received GET request:")
        print(f"Path: {self.path}")
        print(f"Headers: {self.headers}")
        print(f"Client Address: {self.client_address}")
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("hello world", "utf-8"))

    def do_POST(self):
        # Print request details
        print(f"Received POST request:")
        print(f"Path: {self.path}")
        print(f"Headers: {self.headers}")
        print(f"Client Address: {self.client_address}")
        
        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode('utf-8')
        print(f"Post Data: {post_data}")
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("hello world", "utf-8"))

if __name__ == "__main__":    
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()