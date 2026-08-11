import os
from wsgiref.simple_server import make_server

from legacy_api import create_application


if __name__ == "__main__":
    host = os.environ.get("SERVICE_HOST", "127.0.0.1")
    port = int(os.environ.get("SERVICE_PORT", "8080"))
    server = make_server(host, port, create_application())
    print("Legacy REST API listening on http://%s:%d" % (host, port))
    server.serve_forever()
