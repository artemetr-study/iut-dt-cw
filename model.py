from collections.abc import Iterable

import numpy as np
import termtables as tt
from numpy import ndarray


class Model:
    def __init__(self, c: ndarray, a: ndarray, b: ndarray, f=0, maximization: bool = True, basis: ndarray = None):
        self.c = self.ndarray_to_longdouble(c)
        self.a = self.ndarray_to_longdouble(a)
        self.b = self.ndarray_to_longdouble(b)
        self.f = np.longdouble(f)
        self.maximization = maximization
        self.basis = np.array([None for _ in range(self.columns)]) if basis is None else basis

    @property
    def rows(self):
        return self.a.shape[0]

    @property
    def columns(self):
        return self.a.shape[1]

    def has_valid_basis(self):
        return not bool(sum([(i is None) or bool(sum(self.a[:, i]) != 1) for i in self.basis]))

    def has_basic_solution(self):
        return not bool(sum(self.b < 0))

    def to_m_task(self, sanction=10 ** 3, find_exists: bool = False):
        self.basis = np.array([None for _ in range(self.rows)])

        if find_exists:
            defined_basis_rows = [[column_number, column.tolist().index(1)] for column, column_number in
                                  zip(self.a.T, range(self.columns)) if
                                  (column == 1).sum() == 1 and (column == 0).sum() == column.size - 1 and self.c[
                                      column_number] == 0]
            for [column_number, row_number] in defined_basis_rows:
                if self.basis[row_number] is None:
                    self.basis[row_number] = column_number

        undefined_basis_rows = []
        for row_number in range(self.basis.size):
            basis_value = self.basis[row_number]
            if basis_value is None:
                self.basis[row_number] = self.columns + len(undefined_basis_rows)
                undefined_basis_rows.append(row_number)

        m_a = np.array([[1 if row_number == needed_row else 0 for row_number in range(self.rows)] for needed_row in
                        undefined_basis_rows]).T
        m_a = np.concatenate((self.a, m_a), axis=1)  # Складываем с единичной матрицей

        m_sum_a = sum(self.a) * sanction
        m_c = np.concatenate((self.c - m_sum_a if self.maximization else self.c + m_sum_a, np.zeros((len(undefined_basis_rows),))))

        m_sum_b = sum(self.b) * sanction
        m_f = self.f - m_sum_b if self.maximization else self.f + m_sum_b

        self.a = m_a
        self.c = m_c
        self.f = m_f

        return self

    @property
    def summary_table(self):
        return np.concatenate((np.concatenate((np.array([self.b]).T, self.a), axis=1),
                               np.array([np.concatenate((np.array([self.f]), self.c))])))

    def __repr__(self):
        t = tt.to_string(
            np.concatenate((np.array([[f'x_{i}'] if i != 'f' else [i] for i in self.basis.tolist() + ['f']]),
                            self.summary_table.round(decimals=2)), axis=1).tolist(),
            header=['Basis', 'b'] + [f'x_{i}' for i in range(self.columns)],
            style=tt.styles.ascii_thin_double
        )

        return t

    @classmethod
    def ndarray_to_longdouble(cls, subject: ndarray) -> ndarray:
        return np.array(
            [cls.ndarray_to_longdouble(i).tolist() if isinstance(i, Iterable) else np.longdouble(i) for i in subject])
