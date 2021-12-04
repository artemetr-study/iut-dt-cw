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
        available_marks = available_columns * np.array([mark if self._model.maximization and mark < 0 or not self._model.maximization and mark > 0 else False for mark in self._model.c])
        needed_mark = available_marks.min() if self._model.maximization else available_marks.max()
        if not needed_mark:
            raise Exception('Undefined exception')

        needed_mark_index = np.where(available_marks == needed_mark)[0]
        if needed_mark_index.size:
            return int(needed_mark_index[0])

        raise Exception('Undefined exception')
    
    def _get_solved_row_number(self, column_number: int) -> int:
        max_longdouble = np.finfo(np.longdouble).max
        column = self._model.a[:,column_number]
        calculated_divs = np.array([b_value / row_value if row_value > 0 else max_longdouble for row_value, b_value in zip(column, self._model.b)])

        min_calculated_div = calculated_divs.min()
        if not min_calculated_div or min_calculated_div == max_longdouble:
            raise Exception('Undefined exception')

        min_row_index = np.where(calculated_divs == min_calculated_div)[0]
        if min_row_index.size:
            return int(min_row_index[0])

        raise Exception('Undefined exception')

    def _recalculate_with_new_basis(self, column_number: int, row_number: int):
        previous_solved_element = self._model.a[row_number][column_number].copy()
        previous_row = self._model.a[row_number].copy()
        previous_column = self._model.a[:,column_number].copy()
        previous_c = self._model.c[column_number].copy()
        previous_b = self._model.b[row_number].copy()

        self._model.a[row_number] = previous_row / previous_solved_element
        self._model.a[:,column_number] = Model.ndarray_to_longdouble(np.zeros((self._model.rows, )))
        self._model.a[row_number][column_number] = np.longdouble(1)
        self._model.basis[row_number] = column_number
        self._model.b[row_number] = previous_b / previous_solved_element
        self._model.c[column_number] = np.longdouble(0)

        # Пересчет a
        for row in range(self._model.rows):
            if row == row_number:
                continue
            for column in range(self._model.columns):
                if column == column_number:
                    continue
                self._model.a[row][column] = (self._model.a[row][column] * previous_solved_element - previous_row[column] * previous_column[row]) / previous_solved_element

        # Пересчет b
        for row in range(self._model.rows):
            if row == row_number:
                continue
            self._model.b[row] = (self._model.b[row] * previous_solved_element - previous_b * previous_column[row]) / previous_solved_element

        # Пересчет c
        for column in range(self._model.columns):
            if column == column_number:
                continue
            self._model.c[column] = (self._model.c[column] * previous_solved_element - previous_row[column] * previous_c) / previous_solved_element

        # Перерасчет f
        self._model.f = (self._model.f * previous_solved_element - previous_b * previous_c) / previous_solved_element

    def _solve(self) -> Model:
        if not self._model.has_valid_basis() or not self._model.has_basic_solution():
            print('Incorrect model form')

        # print(self._model)
        while not self._is_optimal_solution():
            column_number = self._get_new_basis_variable_number()
            row_number = self._get_solved_row_number(column_number)
            # print(column_number, row_number)
            self._recalculate_with_new_basis(column_number, row_number)
            # print(self._model)

        return self._model

    @classmethod
    def solve(cls, model: Model) -> Model:
        method = cls(model)
        return method._solve()
