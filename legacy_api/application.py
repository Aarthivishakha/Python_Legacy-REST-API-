"""WSGI application factory."""

from legacy_api.http import error_response
from legacy_api.routes import dispatch
from legacy_api.service import ItemService
from legacy_api.store import ItemStore


class LegacyApplication(object):
    def __init__(self, service):
        self.service = service

    def __call__(self, environ, start_response):
        try:
            return dispatch(environ, start_response, self.service)
        except Exception:
            return error_response(start_response, 500, "internal server error")


def create_application(store=None):
    return LegacyApplication(ItemService(store or ItemStore()))
