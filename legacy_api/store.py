"""Thread-safe in-memory persistence."""
import threading


class ItemStore(object):
    def __init__(self):
        self._items = {}
        self._next_id = 1
        self._lock = threading.RLock()

    def list_all(self):
        with self._lock:
            return [dict(self._items[key]) for key in sorted(self._items)]

    def create(self, payload):
        with self._lock:
            item = dict(payload)
            item["id"] = self._next_id
            self._items[self._next_id] = item
            self._next_id += 1
            return dict(item)

    def get(self, item_id):
        with self._lock:
            item = self._items.get(item_id)
            return dict(item) if item is not None else None

    def update(self, item_id, payload):
        with self._lock:
            if item_id not in self._items:
                return None
            item = dict(payload)
            item["id"] = item_id
            self._items[item_id] = item
            return dict(item)

    def delete(self, item_id):
        with self._lock:
            if item_id not in self._items:
                return False
            del self._items[item_id]
            return True
