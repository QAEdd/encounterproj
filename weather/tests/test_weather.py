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
    @patch('application.routes.choice', return_value='Cloudy')
    def test_weather(self, mock_func):
        response = self.client.get(url_for('get_weather'))
        self.assert200(response)
        self.assertIn(b'Cloudy', response.data)
        