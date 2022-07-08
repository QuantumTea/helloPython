import unittest
import api


class TestApi(unittest.TestCase):
    @unittest.skip("test does not work")
    def test_api_post(self):
        result = api.api_post()
        self.assertEqual(200, result)

    def test_api_get(self):
        result = api.api_get_status_code()
        self.assertEqual(200, result)
