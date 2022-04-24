import unittest
import sys
from Check_If_Prime import check_prime


class TestPrime(unittest.TestCase):

	def test_prime(self):
		self.assertEqual(check_prime.check_prime(7), True)
		self.assertEqual(check_prime.check_prime(8), False)
		self.assertEqual(check_prime.check_prime(1), True)
		self.assertEqual(check_prime.check_prime(20), False)
		with self.assertRaises(ValueError):
			check_prime.check_prime(-9)

if __name__ == "__main__":
    unittest.main()