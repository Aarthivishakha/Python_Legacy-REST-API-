from wsgiref.simple_server import make_server

from legacy_api import create_application


if __name__ == "__main__":
    server = make_server("127.0.0.1", 8080, create_application())
    print("Legacy REST API listening on http://127.0.0.1:8080")
    server.serve_forever()
