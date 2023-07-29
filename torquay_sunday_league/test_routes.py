import unittest
from torquay_sunday_league import routes
from flask import session
from flask import Flask
from myapp import app


class TestHome(unittest.TestCase):

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        session["user"]
        routes.home()
        self.assertTrue(user == "None")

# This is when I was trying to produce unittests.
