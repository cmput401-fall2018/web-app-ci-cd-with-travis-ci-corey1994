import unittest
from mock import patch
from service import Service

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service()

    @patch('service.Service.bad_random')
    def test_bad_random(self, mock_bad_random):
        mock_bad_random.return_value = 10

        self.assertEqual(self.service.bad_random(), 10)

    @patch('service.Service.bad_random')
    def test_divide(self, mock_bad_random):
        mock_bad_random.return_value = 10

        # Divisor and dividend are positive, whole result
        self.assertEqual(self.service.divide(5), 2)

        # Divisor and dividend are positive, fractional result
        self.assertEqual(self.service.divide(20), 0.5)

        # Divide by 0
        with self.assertRaises(ZeroDivisionError):
            self.service.divide(0)

        # Positive dividend and negative divisor
        self.assertEqual(self.service.divide(-5), -2)

        mock_bad_random.return_value = -10

        # Negative dividend and positive divisor
        self.assertEqual(self.service.divide(5), -2)

        # Missing argument
        with self.assertRaises(TypeError):
            self.service.divide()

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
        

    @patch('service.Service.divide')
    @patch('service.Service.bad_random')
    def test_complicated_function(self, mock_bad_random, mock_divide):
        mock_divide.return_value = 5

        # Sanity test, with even "random" number
        mock_bad_random.return_value = 20
        (a, b) = self.service.complicated_function(3)
        self.assertEqual(a, 5)
        self.assertEqual(b, 0)

        # Odd "random" number
        mock_bad_random.return_value = 19
        (a, b) = self.service.complicated_function(3)
        self.assertEqual(b, 1)

        # Negative even "random" number
        mock_bad_random.return_value = -20
        (a, b) = self.service.complicated_function(3)
        self.assertEqual(b, 0)

        # Negative odd "random" number
        mock_bad_random.return_value = -19
        (a, b) = self.service.complicated_function(3)
        self.assertEqual(b, 1)

        # No argument
        with self.assertRaises(TypeError):
            self.service.complicated_function()

if __name__ == "__main__":
    unittest.main()
