"""Legacy route matching and endpoint controller."""
import re

from legacy_api.http import error_response, json_response, read_json
from legacy_api.schemas import validate_item
from legacy_api.service import ItemNotFound


ITEM_PATH = re.compile(r"^/api/v1/items/(\d+)$")


def dispatch(environ, start_response, service):
    method = environ.get("REQUEST_METHOD", "GET").upper()
    path = environ.get("PATH_INFO", "/")
    match = ITEM_PATH.match(path)
    try:
        if method == "GET" and path == "/health":
            return json_response(start_response, 200, {"status": "ok", "service": "legacy-rest-api", "python": "3.16"})
        if path == "/api/v1/items" and method == "GET":
            return json_response(start_response, 200, {"items": service.list_all()})
        if path == "/api/v1/items" and method == "POST":
            return json_response(start_response, 201, service.create(validate_item(read_json(environ))))
        if match and method == "GET":
            return json_response(start_response, 200, service.get(int(match.group(1))))
        if match and method == "PUT":
            payload = validate_item(read_json(environ))
            return json_response(start_response, 200, service.update(int(match.group(1)), payload))
        if match and method == "DELETE":
            service.delete(int(match.group(1)))
            return json_response(start_response, 204)
        if path == "/api/v1/items" or match:
            return error_response(start_response, 405, "method not allowed")
        return error_response(start_response, 404, "route not found")
    except ValueError as error:
        return error_response(start_response, 400, str(error))
    except ItemNotFound as error:
        return error_response(start_response, 404, str(error))
