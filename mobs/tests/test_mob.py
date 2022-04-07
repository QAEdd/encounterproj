from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='Dragon')
    def test_mob(self, mock_func):
        response = self.client.post(url_for('get_mob'), json={'location':'Tavern'})
        self.assert200(response)
        self.assertIn(b'Dragon',response.data)
