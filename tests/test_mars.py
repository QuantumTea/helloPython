import unittest
import mars


# tests for an API GET request

class TestMars(unittest.TestCase):
    def test_response_code(self):
        result = mars.get_latest_response_code()
        self.assertEqual(200, result)

    def test_response_json(self):
        result = mars.get_latest_json()
        # print(result)
        self.assertIn('local_uv_irradiance_index', result)

    def test_given_sol(self):
        result = mars.get_specific_sol(42)
        self.assertIn('2012-09-18T00:00:00.000Z', result)
