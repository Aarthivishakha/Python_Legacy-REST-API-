import io
import json
import unittest

from legacy_api import create_application


class LegacyApiTest(unittest.TestCase):
    def setUp(self):
        self.application = create_application()

    def request(self, method, path, payload=None):
        body = b"" if payload is None else json.dumps(payload).encode("utf-8")
        environ = {
            "REQUEST_METHOD": method,
            "PATH_INFO": path,
            "SERVER_NAME": "localhost",
            "SERVER_PORT": "80",
            "SERVER_PROTOCOL": "HTTP/1.1",
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            "wsgi.input": io.BytesIO(body),
            "wsgi.errors": io.StringIO(),
            "wsgi.multithread": False,
            "wsgi.multiprocess": False,
            "wsgi.run_once": False,
            "CONTENT_LENGTH": str(len(body)),
            "CONTENT_TYPE": "application/json",
        }
        result = {}

        def start_response(status, headers, exc_info=None):
            result["status"] = int(status.split()[0])
            result["headers"] = dict(headers)

        chunks = self.application(environ, start_response)
        raw = b"".join(chunks)
        payload = json.loads(raw.decode("utf-8")) if raw else None
        return result["status"], payload

    def test_health(self):
        status, payload = self.request("GET", "/health")
        self.assertEqual(200, status)
        self.assertEqual("ok", payload["status"])

    def test_crud_lifecycle(self):
        status, created = self.request("POST", "/api/v1/items", {"name": "legacy"})
        self.assertEqual(201, status)
        self.assertEqual(1, created["id"])
        status, fetched = self.request("GET", "/api/v1/items/1")
        self.assertEqual("legacy", fetched["name"])
        status, updated = self.request("PUT", "/api/v1/items/1", {"name": "modernized"})
        self.assertEqual(200, status)
        self.assertEqual("modernized", updated["name"])
        status, listed = self.request("GET", "/api/v1/items")
        self.assertEqual(1, len(listed["items"]))
        status, payload = self.request("DELETE", "/api/v1/items/1")
        self.assertEqual(204, status)
        self.assertEqual(None, payload)

    def test_validation_not_found_and_method_errors(self):
        status, payload = self.request("POST", "/api/v1/items", {"name": ""})
        self.assertEqual(400, status)
        status, payload = self.request("GET", "/api/v1/items/99")
        self.assertEqual(404, status)
        status, payload = self.request("PATCH", "/api/v1/items")
        self.assertEqual(405, status)


if __name__ == "__main__":
    unittest.main()
