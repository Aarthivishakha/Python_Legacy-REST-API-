# Legacy REST API / Microservice (Python 3.6)

A framework-free JSON microservice built on the Python 3.6 WSGI standard
library. It demonstrates how a legacy service can retain clear HTTP, routing,
validation, service, and persistence boundaries while remaining analyzable by
current tooling.

```bash
python setup.py test
python run.py
```

The development server listens at `http://127.0.0.1:8080`.

## API

| Method | Path | Behavior |
|---|---|---|
| GET | `/health` | Health, service, and Python version |
| GET | `/api/v1/items` | List items |
| POST | `/api/v1/items` | Validate and create an item |
| GET | `/api/v1/items/<id>` | Fetch an item |
| PUT | `/api/v1/items/<id>` | Validate and replace an item |
| DELETE | `/api/v1/items/<id>` | Delete an item |

Item JSON requires a non-empty string `name`; `description` is optional. Errors
use `{"error": {"status": ..., "message": ...}}` consistently.

## Architecture

- `legacy_api/application.py`: WSGI application and request dispatch.
- `legacy_api/http.py`: JSON request/response boundary.
- `legacy_api/routes.py`: URL matching and endpoint controller.
- `legacy_api/schemas.py`: input validation.
- `legacy_api/service.py`: use cases and not-found behavior.
- `legacy_api/store.py`: thread-safe in-memory persistence.
- `tests/test_api.py`: WSGI-level health, CRUD, validation, and error tests.
- `tool-triggers/`: 14 tools wired to real project files.

Current analyzers run separately under Python 3.10+; application source remains
compatible with Python 3.6.
