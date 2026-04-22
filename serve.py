import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "/Users/amirosai/.openclaw/workspace/aia-card-generator"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print("Open this link in your browser to generate your AIA 2026 card.")
    httpd.serve_forever()
