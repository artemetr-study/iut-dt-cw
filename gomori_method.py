from model import Model
from simplex_method import SimplexMethod


class GomoriMethod(SimplexMethod):
    @staticmethod
    def _is_integer(value):
        return not (round(value, ndigits=13) % 1)

    def _is_integer_optimal_solution(self):
        if self._is_integer(self._model.f):
            return True

        if [True for row_number in range(self._model.rows) if
            not self._is_integer(self._model.b[row_number]) and len(
                    [True for i in self._model.a[row_number] if self._is_integer(i)]) == self._model.a[
                row_number].size]:
            raise Exception('Задача неразрешима т.к. в строке для дробной переменной все коэффициенты целые')

        return False

    @classmethod
    def solve(cls, model: Model) -> Model:
        model = super().solve(model)

        method = cls(model)
        return method._solve()
