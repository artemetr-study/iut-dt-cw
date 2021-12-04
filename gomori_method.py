import numpy as np

from model import Model
from simplex_method import SimplexMethod


class GomoriMethod(SimplexMethod):
    @staticmethod
    def _get_floating_part(value):
        return round(value, ndigits=13) % 1

    @classmethod
    def _is_integer(cls, value):
        return not cls._get_floating_part(value)

    def _is_integer_optimal_solution(self):
        if self._is_integer(self._model.f) and np.array([self._is_integer(i) for i in self._model.b]).prod():
            return True

        if [True for row_number in range(self._model.rows) if
            not self._is_integer(self._model.b[row_number]) and len(
                    [True for i in self._model.a[row_number] if self._is_integer(i)]) == self._model.a[
                row_number].size]:
            raise Exception('Задача неразрешима т.к. в строке для дробной переменной все коэффициенты целые')

        return False

    def _get_column_number_with_max_floating_part(self):
        floating_parts = [self._get_floating_part(b) for b in self._model.b]
        max_floating_part = max(floating_parts)

        if not max_floating_part:
            raise Exception('Undefined exception')

        return self._model.basis[floating_parts.index(max_floating_part)]

    def _add_condition(self, column_number):
        row_number = self._model.basis.tolist().index(column_number)
        self._model.a = Model.ndarray_to_longdouble(np.array(np.concatenate((self._model.a, np.zeros((self._model.rows, 1))), axis=1).tolist() + [[self._get_floating_part(i) for i in self._model.a.tolist()[row_number]] + [-1]]))
        self._model.b = Model.ndarray_to_longdouble(np.array(self._model.b.tolist() + [self._get_floating_part(self._model.b[row_number])]))
        self._model.basis = np.array(self._model.basis.tolist() + [None])
        self._model.c = Model.ndarray_to_longdouble(np.array(self._model.c.tolist() + [1]))

        self._model.to_m_task(find_exists=True)

    def _solve(self) -> Model:
        self._model = super()._solve()
        while not self._is_integer_optimal_solution():
            condition_column_number = self._get_column_number_with_max_floating_part()
            self._add_condition(condition_column_number)
            self._model = super()._solve()

        return self._model
