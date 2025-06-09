"""Basic MCP server example using Python.
See docs/architecture.md and docs/getting-started.md for protocol details.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        request = json.loads(self.rfile.read(length))
        method = request.get("method")
        if method == "sum":
            result = sum(request.get("params", []))
            response = {"jsonrpc": "2.0", "result": result, "id": request.get("id")}
        else:
            response = {
                "jsonrpc": "2.0",
                "error": {"code": -32601, "message": "Method not found"},
                "id": request.get("id"),
            }
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run():
    server = HTTPServer(("0.0.0.0", 8000), MCPHandler)
    print("Python MCP server running on http://0.0.0.0:8000")
    server.serve_forever()

if __name__ == "__main__":
    run()
