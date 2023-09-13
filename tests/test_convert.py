import unittest

from diffeq_pybamm import add_one


class TestConvert(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)


if __name__ == '__main__':
    unittest.main()