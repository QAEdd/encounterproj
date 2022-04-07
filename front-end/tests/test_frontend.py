from flask import url_for
from flask_testing import TestCase
import pytest
import requests_mock
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app