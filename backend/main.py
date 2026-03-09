from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from db.database import get_latest_momentum_scores


class SimpleAPI(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"status": "ok"}
            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/api/top":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            top_coins = get_latest_momentum_scores()
            response = {"top_coins": top_coins}
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"error": "not found"}
            self.wfile.write(json.dumps(response).encode())


def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPI)

    print("Server running on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
