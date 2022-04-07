from application import app
from flask_testing import TestCase
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_mob(self):
        response = self.client.post(url_for('get-mobs'), json={'location':'Tavern'})
        self.assert200(response)
        self.assertIn(b'Dragon',response.data)