"""Small WSGI JSON boundary shared by all endpoints."""
import json


STATUS_TEXT = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
}


def read_json(environ):
    try:
        length = int(environ.get("CONTENT_LENGTH") or 0)
        raw = environ["wsgi.input"].read(length)
        if not raw:
            raise ValueError("request body must contain JSON")
        if not isinstance(raw, str):
            raw = raw.decode("utf-8")
        return json.loads(raw)
    except (KeyError, TypeError, ValueError):
        raise ValueError("request body must contain valid JSON")


def json_response(start_response, status, payload=None):
    if status == 204:
        body = b""
    else:
        body = json.dumps(payload, sort_keys=True).encode("utf-8")
    headers = [("Content-Type", "application/json"), ("Content-Length", str(len(body)))]
    start_response("%d %s" % (status, STATUS_TEXT[status]), headers)
    return [body]


def error_response(start_response, status, message):
    return json_response(start_response, status, {"error": {"status": status, "message": message}})
