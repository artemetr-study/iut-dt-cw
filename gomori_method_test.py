import unittest

import numpy as np

from gomori_method import GomoriMethod
from model import Model

mock_a = np.array([[1, 1], [1 / 2, 1]])
mock_basis = np.array([0, 1])
mock_b = np.array([1, 1 / 18])
mock_b_invalid = np.array([1 / 16, 1 / 18])

mock_f_int = 1
mock_f_double = np.longdouble(1 / 9)


class GomoriMethodTestCase(unittest.TestCase):
    def test__is_integer_optimal_solution_true(self):
        self.assertEqual(True, GomoriMethod(
            Model(c=np.array([]), a=mock_a, b=mock_b, f=mock_f_int, basis=mock_basis))._is_integer_optimal_solution())

    def test__is_integer_optimal_solution_false(self):
        self.assertEqual(False, GomoriMethod(Model(c=np.array([]), a=mock_a, b=mock_b, f=mock_f_double,
                                                   basis=mock_basis))._is_integer_optimal_solution())

    def test__is_integer_optimal_solution_invalid(self):
        self.assertRaises(Exception, GomoriMethod(Model(c=np.array([]), a=mock_a, b=mock_b_invalid, f=mock_f_double,
                                                        basis=mock_basis))._is_integer_optimal_solution)


if __name__ == '__main__':
    unittest.main()
