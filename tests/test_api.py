import unittest
import api


@unittest.skip("test does not work")
class TestApi(unittest.TestCase):
    def test_api_post(self):
        result = api.api_post()
        self.assertEqual(200, result)

    def test_api_get(self):
        result = api.api_get()
        self.assertEqual(200, result)
