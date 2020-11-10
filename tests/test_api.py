import unittest
import api


class TestApi(unittest.TestCase):
    def test_api_post(self):
        result = api.api_post()
        self.assertEqual(406, result)

    def test_api_get(self):
        result = api.api_get()
        self.assertEqual(406, result)
