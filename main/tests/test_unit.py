import unittest
import requests
import pytest
import requests_mock

from flask import url_for
from flask_testing import TestCase

from app import app

from application.routes import index, date

class TestInit(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        print("-----------")

    def tearDown(self):
        print("--------")

class TestMain(TestInit):
    
    def test_response(self):
        
        response = self.client.get(url_for('index'))
        
        self.assertEqual(response.status_code, 200, msg='Equal')

        with requests_mock.mock() as m:
            m.post('http://converter:5001/date/1986/') #posts a response to the REST API

            response = self.client.get(
                ('http://main:5000/') #get hte data from session data via the url method
            )
            self.assertIn(b'Birth Year:', response.data) # refers to where in the html template the data is input

            #write tests for all urls

    def test_prime_response(self):
        
        response = self.client.get(url_for('index'))

        self.assertEqual(response.status_code, 200, msg='Equal')

        with requests_mock.mock() as m:
            m.post('http://prime:5002/date/444/')

            response = self.client.get(
                ('http://main:5000/') 
            )
            self.assertIn(b'Birth Year:', response.data)


