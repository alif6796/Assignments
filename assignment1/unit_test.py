import unittest
from assignment1 import is_perfect_cube, print_cubes

class MyTest(unittest.TestCase):
    def test_cube(self):
        self.assertFalse(is_perfect_cube(3))
        self.assertTrue(is_perfect_cube(27))
    def test_range(self):
        self.assertEqual(print_cubes(1,1000), "1, 8, 27, 64, 125, 216, 343, 512, 729, 1000")
if __name__ == '__main__':
    unittest.main()

