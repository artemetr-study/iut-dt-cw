import numpy as np

from model import Model
from simplex_method_mocks import Models

mock_models_1 = Models(not_optimal=Model(
    c=np.array([2, -3, 6, 1, 0, 0]),
    a=np.array([[2, 1, -2, 1, 0, 0], [1, 2, 4, 0, 1, 0], [1, -1, 2, 0, 0, -1]]),
    b=np.array([24, 22, 10]),
    f=0,
    maximization=False
).to_m_task(), optimal=Model(
    c=np.array([0.0, -4.0, 0.0, 0.0, -0.0, 0.0, -1001.0, -1000.0, -1000.0, -7.0, -992.0]),
    a=np.array([[0.0, -3.0, 0.0, 1.0, -2.0, 0.0, 1.0, -2.0, 0.0, 10.0, -10.0],
                [0.0, 3.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, -1.0, -2.0, 2.0],
                [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, -1.0],
                [1.0, 2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, -4.0, 4.0]]),
    b=np.array([30, 2, 5, 2]),
    f=-64,
    basis=np.array([3, 5, 2, 0]),
    maximization=False
))

mock_models_2 = Models(not_optimal=Model(
    c=np.array([-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0]),
    a=np.array([[1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, -1, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, -1]]),
    b=np.array([4, 8, 10, 7, 12, 4]),
    f=0,
    maximization=False
).to_m_task(), optimal=Model(
    c=np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, -1.0, 0.0, -1.0, 0.0, -999.0, -1000.0, -999.0, -1000.0, -999.0,
                -1000.0]),
    a=np.array([[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0, 0.0, 1.0, -1.0, 1.0, -1.0, 0.0, 0.0, 0.0, 1.0, -1.0, 1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, -1.0],
                [0.0, 0.0, -1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0, -1.0, 1.0, 0.0, 0.0, 0.0, -1.0, 1.0, -1.0],
                [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]),
    b=np.array([4, 10, 6, 8, 1, 4]),
    f=26,
    basis=np.array([0, 1, 7, 3, 9, 4]),
    maximization=False
))

mock_models_3 = Models(
    not_optimal=Model(
        a=np.array([
            [np.longdouble(1) / np.longdouble(300), 0, 0, 0, np.longdouble(1) / np.longdouble(700), 0, 0, 0,
             np.longdouble(1) / np.longdouble(500), 0, 0, 0, np.longdouble(1) / np.longdouble(400), 0, 0, 0,
             np.longdouble(1) / np.longdouble(900), 0, 0, 0, 1, 0, 0, 0],
            [0, np.longdouble(1) / np.longdouble(700), 0, 0, 0, np.longdouble(1) / np.longdouble(800), 0, 0, 0,
             np.longdouble(1) / np.longdouble(400), 0, 0, 0, np.longdouble(1) / np.longdouble(500), 0, 0, 0,
             np.longdouble(1) / np.longdouble(900), 0, 0, 0, 1, 0, 0],
            [0, 0, np.longdouble(1) / np.longdouble(800), 0, 0, 0, np.longdouble(1) / np.longdouble(600), 0, 0, 0,
             np.longdouble(1) / np.longdouble(400), 0, 0, 0, np.longdouble(1) / np.longdouble(200), 0, 0, 0,
             np.longdouble(1) / np.longdouble(400), 0, 0, 0, 1, 0],
            [0, 0, 0, np.longdouble(1) / np.longdouble(500), 0, 0, 0, np.longdouble(1) / np.longdouble(700), 0, 0, 0,
             np.longdouble(1) / np.longdouble(500), 0, 0, 0, np.longdouble(1) / np.longdouble(500), 0, 0, 0,
             np.longdouble(1) / np.longdouble(600), 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, -4, -4, -4, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, -2, -2, -2, -2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, -5, -5, -5, -5, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
        ]),
        b=np.array([1, 1, 1, 1, 0, 0, 0, 0]),
        c=np.array([0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        f=0,
        maximization=True
    ).to_m_task()
)
