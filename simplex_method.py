from fractions import Fraction
from math import inf

import numpy as np

from model import Model


class SimplexMethod:
    def __init__(self, model: Model):
        self._model = model

    def _is_optimal_solution(self) -> bool:
        for mark, column in zip(self._model.c, self._model.a.T):
            if self._model.maximization and mark < 0 or not self._model.maximization and mark > 0:
                if not bool(sum(column > 0)):
                    raise Exception(
                        f'Функция f не ограничена {"сверху" if self._model.maximization else "снизу"}, т.е. f→{"+" if self._model.maximization else "-"}∞')
                else:
                    return False

        return True

    def _get_new_basis_variable_number(self) -> int:
        available_columns = np.array([bool(sum(column > 0)) for column in self._model.a.T])
        available_marks = available_columns * np.array(
            [mark if self._model.maximization and mark < 0 or not self._model.maximization and mark > 0 else False for
             mark in self._model.c])
        needed_mark = available_marks.min() if self._model.maximization else available_marks.max()
        if not needed_mark:
            raise Exception('Undefined exception')

        needed_mark_index = np.where(available_marks == needed_mark)[0]
        if needed_mark_index.size:
            return int(needed_mark_index[0])

        raise Exception('Undefined exception')

    def _get_solved_row_number(self, column_number: int) -> int:
        column = self._model.a[:, column_number]
        calculated_divs = np.array(
            [b_value / row_value if row_value > 0 else inf for row_value, b_value in zip(column, self._model.b)])

        min_calculated_div = calculated_divs.min()
        if min_calculated_div == inf:
            raise Exception('Undefined exception')

        min_row_index = np.where(calculated_divs == min_calculated_div)[0]
        if min_row_index.size:
            return int(min_row_index[0])

        raise Exception('Undefined exception')

    def _recalculate_with_new_basis(self, column_number: int, row_number: int):
        previous_solved_element = self._model.a[row_number][column_number]
        previous_row = self._model.a[row_number].copy()
        previous_column = self._model.a[:, column_number].copy()
        previous_a = self._model.a.copy()
        previous_c = self._model.c.copy()
        previous_c_value = self._model.c[column_number]
        previous_b = self._model.b.copy()
        previous_b_value = self._model.b[row_number]
        previous_f = self._model.f

        self._model.a[row_number] = previous_row / previous_solved_element
        self._model.a[:, column_number] = Model.ndarray_to_type(np.zeros((self._model.rows,)))
        self._model.a[row_number][column_number] = Fraction(1)
        self._model.basis[row_number] = column_number
        self._model.b[row_number] = previous_b_value / previous_solved_element
        self._model.c[column_number] = Fraction(0)

        # Пересчет a
        for row in range(self._model.rows):
            if row == row_number:
                continue
            for column in range(self._model.columns):
                if column == column_number:
                    continue
                try:
                    self._model.a[row][column] = previous_a[row][column] - previous_row[column] * previous_column[
                        row] / previous_solved_element
                except:
                    self._model.a[row][column] = (previous_a[row][column] * previous_solved_element - previous_row[
                        column] * previous_column[row]) / previous_solved_element

        # Пересчет b
        for row in range(self._model.rows):
            if row == row_number:
                continue
            try:
                self._model.b[row] = previous_b[row] - previous_b_value * previous_column[row] / previous_solved_element
            except:
                self._model.b[row] = (previous_b[row] * previous_solved_element - previous_b_value * previous_column[
                    row]) / previous_solved_element

        # Пересчет c
        for column in range(self._model.columns):
            if column == column_number:
                continue
            try:
                self._model.c[column] = previous_c[column] - previous_row[
                    column] * previous_c_value / previous_solved_element
            except:
                self._model.c[column] = (previous_c[column] * previous_solved_element - previous_row[
                    column] * previous_c_value) / previous_solved_element

        # Перерасчет f

        try:
            self._model.f = previous_f - previous_b_value * previous_c_value / previous_solved_element
        except:
            self._model.f = (
                                    previous_f * previous_solved_element - previous_b_value * previous_c_value) / previous_solved_element

    def _solve(self) -> Model:
        if not self._model.has_valid_basis() or not self._model.has_basic_solution():
            print('Incorrect model form')

        # print(self._model)
        while not self._is_optimal_solution():
            column_number = self._get_new_basis_variable_number()
            row_number = self._get_solved_row_number(column_number)
            # print(column_number, row_number)
            self._recalculate_with_new_basis(column_number, row_number)
            # if not self._model.conditions_are_met():
            #     print(self._model)

        # print(self._model)

        return self._model

    @classmethod
    def solve(cls, model: Model) -> Model:
        method = cls(model)
        return method._solve()
