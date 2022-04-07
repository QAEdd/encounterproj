from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_location(TestBase):
    @patch('application.routes.choice', return_value='Tavern')
    def test_loc(self, mock_func):
        response = self.client.get(url_for('get_location'))
        self.assert200(response)
        self.assertIn(b'Tavern', response.data)
        