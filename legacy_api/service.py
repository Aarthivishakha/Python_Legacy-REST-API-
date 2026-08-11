"""Item use cases."""


class ItemNotFound(Exception):
    pass


class ItemService(object):
    def __init__(self, store):
        self.store = store

    def list_all(self):
        return self.store.list_all()

    def create(self, payload):
        return self.store.create(payload)

    def get(self, item_id):
        item = self.store.get(item_id)
        if item is None:
            raise ItemNotFound("item %d was not found" % item_id)
        return item

    def update(self, item_id, payload):
        item = self.store.update(item_id, payload)
        if item is None:
            raise ItemNotFound("item %d was not found" % item_id)
        return item

    def delete(self, item_id):
        if not self.store.delete(item_id):
            raise ItemNotFound("item %d was not found" % item_id)
