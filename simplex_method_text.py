import unittest

import numpy as np

from model import Model
from simplex_method import SimplexMethod
from simplex_method_mocks import mock_models_1, mock_models_2, mock_models_3, mock_models_4

mock_optimal_max_mark_string = np.array([0, 1, 1, 2])
mock_not_optimal_max_mark_string = np.array([0, -1, 1, -2])

mock_optimal_min_mark_string = np.array([0, -1, -1, -2])
mock_not_optimal_min_mark_string = np.array([0, 1, -1, 2])

mock_not_optimal_columns = np.array([[0, -1, -1, 1], [0, 1, -1, 2], [-1, -1, -1, -2], [0, 3, 2, -1]]).T
mock_not_optimal_columns_with_one_available_column = np.array(
    [[0, -1, -1, 1], [0, 1, -1, 2], [-1, -1, -1, -2], [0, -3, -2, -1]]).T
mock_invalid_optimal_columns = np.array([[0, 1, 1, 1], [0, -1, -1, -1], [-1, -1, -1, -1], [0, -1, -1, -1]]).T

mock_solved_columns = Model.ndarray_to_longdouble(np.array(
    [[0, -1 / 3, -1 + 2 / 3, 1 - 1 / 3], [0, 1 / 3, -1 - 2 / 3, 2 + 1 / 3], [-1, -1 / 3, -1 + 2 / 3, -2 - 1 / 3],
     [0, 1, 0, 0]]).T)
mock_solved_b = Model.ndarray_to_longdouble(np.array([5, 4 / 3, 3 - 8 / 3, 2 + 4 / 3]))
mock_solved_marks = Model.ndarray_to_longdouble(np.array([-2 / 3, -1 + 2 / 3, 1 - 2 / 3, 0]))
mock_solved_basis = np.array([None, 3, None, None])
mock_solved_f = 8 / 3

mock_b = np.array([5, 4, 3, 2])


class SimplexMethodTest(unittest.TestCase):
    def test__is_optimal_solution_max_optimal(self):
        self.assertEqual(True,
                         SimplexMethod(Model(mock_optimal_max_mark_string, mock_not_optimal_columns, np.array([]), 0,
                                             True))._is_optimal_solution())

    def test__is_optimal_solution_max_not_optimal(self):
        self.assertEqual(False,
                         SimplexMethod(
                             Model(mock_not_optimal_max_mark_string, mock_not_optimal_columns, np.array([]), 0,
                                   True))._is_optimal_solution())

    def test__is_optimal_solution_max_invalid_optimal(self):
        method = SimplexMethod(
            Model(mock_not_optimal_max_mark_string, mock_invalid_optimal_columns, np.array([]), 0, True))
        self.assertRaises(Exception, method._is_optimal_solution)

    def test__is_optimal_solution_min_optimal(self):
        self.assertEqual(True,
                         SimplexMethod(Model(mock_optimal_min_mark_string, mock_not_optimal_columns, np.array([]), 0,
                                             False))._is_optimal_solution())

    def test__is_optimal_solution_min_not_optimal(self):
        self.assertEqual(False,
                         SimplexMethod(
                             Model(mock_not_optimal_min_mark_string, mock_not_optimal_columns, np.array([]), 0,
                                   False))._is_optimal_solution())

    def test__is_optimal_solution_min_invalid_optimal(self):
        method = SimplexMethod(
            Model(mock_not_optimal_min_mark_string, mock_invalid_optimal_columns, np.array([]), 0, False))
        self.assertRaises(Exception, method._is_optimal_solution)

    def test__get_new_basis_variable_number_max_found(self):
        self.assertEqual(3,
                         SimplexMethod(
                             Model(mock_not_optimal_max_mark_string, mock_not_optimal_columns, np.array([]), 0,
                                   True))._get_new_basis_variable_number())

    def test__get_new_basis_variable_number_max_found_with_one_available_column(self):
        self.assertEqual(1,
                         SimplexMethod(
                             Model(mock_not_optimal_max_mark_string, mock_not_optimal_columns_with_one_available_column,
                                   np.array([]), 0,
                                   True))._get_new_basis_variable_number())

    def test__get_new_basis_variable_number_max_not_found(self):
        method = SimplexMethod(Model(mock_optimal_max_mark_string, mock_not_optimal_columns, np.array([]), 0, True))
        self.assertRaises(Exception, method._get_new_basis_variable_number)

    def test__get_new_basis_variable_number_max_not_found_by_column(self):
        method = SimplexMethod(
            Model(mock_not_optimal_max_mark_string, mock_invalid_optimal_columns, np.array([]), 0, True))
        self.assertRaises(Exception, method._get_new_basis_variable_number)

    def test__get_new_basis_variable_number_min_found(self):
        self.assertEqual(3,
                         SimplexMethod(
                             Model(mock_not_optimal_min_mark_string, mock_not_optimal_columns, np.array([]), 0,
                                   False))._get_new_basis_variable_number())

    def test__get_new_basis_variable_number_min_found_with_one_available_column(self):
        self.assertEqual(1,
                         SimplexMethod(
                             Model(mock_not_optimal_min_mark_string, mock_not_optimal_columns_with_one_available_column,
                                   np.array([]), 0,
                                   False))._get_new_basis_variable_number())

    def test__get_new_basis_variable_number_min_not_found(self):
        method = SimplexMethod(Model(mock_optimal_min_mark_string, mock_not_optimal_columns, np.array([]), 0, False))
        self.assertRaises(Exception, method._get_new_basis_variable_number)

    def test__get_new_basis_variable_number_min_not_found_by_column(self):
        method = SimplexMethod(
            Model(mock_not_optimal_min_mark_string, mock_invalid_optimal_columns, np.array([]), 0, False))
        self.assertRaises(Exception, method._get_new_basis_variable_number)

    def test__get_solved_row_number_found(self):
        self.assertEqual(3, SimplexMethod(
            Model(np.array([]), mock_not_optimal_columns, mock_b, 0, True))._get_solved_row_number(1))
        self.assertEqual(1, SimplexMethod(
            Model(np.array([]), mock_not_optimal_columns, mock_b, 0, True))._get_solved_row_number(3))
        self.assertEqual(3, SimplexMethod(
            Model(np.array([]), mock_not_optimal_columns, mock_b, 0, False))._get_solved_row_number(1))
        self.assertEqual(1, SimplexMethod(
            Model(np.array([]), mock_not_optimal_columns, mock_b, 0, False))._get_solved_row_number(3))

    def test__get_solved_row_number_not_found(self):
        method = SimplexMethod(Model(np.array([]), mock_invalid_optimal_columns, mock_b, 0, True))
        self.assertRaises(Exception, method._get_solved_row_number, 1)
        self.assertRaises(Exception, method._get_solved_row_number, 3)

        method = SimplexMethod(Model(np.array([]), mock_invalid_optimal_columns, mock_b, 0, False))
        self.assertRaises(Exception, method._get_solved_row_number, 1)
        self.assertRaises(Exception, method._get_solved_row_number, 3)

    def test__recalculate_with_new_basis(self):
        method = SimplexMethod(Model(mock_not_optimal_max_mark_string, mock_not_optimal_columns, mock_b, 0, True))
        method._recalculate_with_new_basis(3, 1)
        np.testing.assert_array_equal(mock_solved_basis, method._model.basis)
        np.testing.assert_array_almost_equal(mock_solved_b, method._model.b, decimal=15)
        np.testing.assert_array_almost_equal(mock_solved_marks, method._model.c, decimal=15)
        np.testing.assert_array_almost_equal(mock_solved_columns, method._model.a, decimal=15)
        np.testing.assert_almost_equal(mock_solved_f, method._model.f, decimal=15)

    def test__solve_1(self):
        self.assertEqual(mock_models_1.optimal.__repr__(), SimplexMethod.solve(mock_models_1.not_optimal).__repr__())

    def test__solve_2(self):
        self.assertRaises(Exception, SimplexMethod.solve, mock_models_2.not_optimal)

    def test__solve_3(self):
        self.assertEqual(mock_models_3.optimal.__repr__(), SimplexMethod.solve(mock_models_3.not_optimal).__repr__())

    def test__solve_4(self):
        self.assertEqual(mock_models_4.optimal.__repr__(), SimplexMethod.solve(mock_models_4.not_optimal).__repr__())


if __name__ == '__main__':
    unittest.main()
