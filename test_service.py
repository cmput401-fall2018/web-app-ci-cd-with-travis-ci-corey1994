import unittest
import mock
from service import Service

class TestService(unittest.TestCase):
    def test_bad_random(self):
        pass

    def test_divide(self):
        pass

    def test_abs_plus(self):
        service = Service()

        # Negative
        self.assertEqual(service.abs_plus(-1), 2)

        # 0
        self.assertEqual(service.abs_plus(0), 1)

        # Positive
        self.assertEqual(service.abs_plus(1), 2)

        # Non-integer
        with self.assertRaises(TypeError):
            service.abs_plus('a')
        

    def test_complicated_function(self):
        pass

if __name__ == "__main__":
    unittest.main()
