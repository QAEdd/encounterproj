from flask import url_for
from flask_testing import TestCase
import pytest
import requests_mock
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFrontend(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as m:
            m.get('http://location:5000/get-location', json={'location':'Tavern'})
            m.get('http://weather:5000/get-weather', json={'weat':'Cloudy'})
            m.post('http://mobs:5000/get-mobs', json={'mob':'Dragon'})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'locatoin : Tavern', response.data)
            self.assertIn(b'weat : Cloudy', response.data)
            self.assertIn(b'mob : Dragon', response.data)