import unittest
import mock
from service import Service

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()

    def test_bad_random(self):
        pass

    def test_divide(self):
        pass

    def test_abs_plus(self):
        # Negative
        self.assertEqual(self.service.abs_plus(-1), 2)

        # 0
        self.assertEqual(self.service.abs_plus(0), 1)

        # Positive
        self.assertEqual(self.service.abs_plus(1), 2)

        # Non-integer
        with self.assertRaises(TypeError):
            self.service.abs_plus('a')

        # No argument
        with self.assertRaises(TypeError):
            self.service.abs_plus()
        

    def test_complicated_function(self):
        pass

if __name__ == "__main__":
    unittest.main()
