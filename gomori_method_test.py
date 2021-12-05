import unittest
from fractions import Fraction

import numpy as np

from gomori_method import GomoriMethod
from gomori_method_mocks import mock_models_2, mock_models_1
from model import Model

mock_a = Model.array([[1, 1], ['1/2', 1]])
mock_basis = np.array([0, 1])
mock_b = Model.array([1, '1/18'])
mock_b_int = Model.array([1, 2])
mock_b_invalid = Model.array(['1/16', '1/18'])

mock_f_int = Fraction(1)
mock_f_rational = Fraction('1/9')


class GomoriMethodTestCase(unittest.TestCase):
    def test__is_integer_optimal_solution_true(self):
        self.assertEqual(True, GomoriMethod(Model(c=Model.array([]), a=mock_a, b=mock_b_int, f=mock_f_int,
                                                  basis=mock_basis))._is_integer_optimal_solution())

    def test__is_integer_optimal_solution_false(self):
        self.assertEqual(False, GomoriMethod(Model(c=Model.array([]), a=mock_a, b=mock_b, f=mock_f_rational,
                                                   basis=mock_basis))._is_integer_optimal_solution())

    def test__is_integer_optimal_solution_invalid(self):
        self.assertRaises(Exception, GomoriMethod(
            Model(c=Model.array([]), a=mock_a, b=mock_b_invalid, f=mock_f_rational,
                  basis=mock_basis))._is_integer_optimal_solution)

    def test__solve_1(self):
        self.assertEqual(mock_models_1.optimal.__repr__(), GomoriMethod.solve(mock_models_1.not_optimal).__repr__())

    def test__solve_2(self):
        self.assertEqual(mock_models_2.optimal.__repr__(), GomoriMethod.solve(mock_models_2.not_optimal).__repr__())


if __name__ == '__main__':
    unittest.main()
