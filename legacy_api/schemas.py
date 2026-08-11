"""Request validation."""

try:
    string_types = (basestring,)
except NameError:
    string_types = (str,)


def validate_item(payload):
    if not isinstance(payload, dict):
        raise ValueError("request body must be a JSON object")
    name = payload.get("name")
    description = payload.get("description", "")
    if not isinstance(name, string_types) or not name.strip():
        raise ValueError("name must be a non-empty string")
    if not isinstance(description, string_types):
        raise ValueError("description must be a string")
    return {"name": name.strip(), "description": description.strip()}
