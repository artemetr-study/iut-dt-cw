from dataclasses import dataclass

import numpy as np

from model import Model


@dataclass
class Models:
    not_optimal: Model
    optimal: Model = None


mock_models_1 = Models(not_optimal=Model(c=Model.array([-9, -10, -16, 0, 0, 0]),
    a=Model.array([[18, 15, 12, 1, 0, 0], [6, 4, 8, 0, 1, 0], [5, 3, 3, 0, 0, 1]]), b=Model.array([360, 192, 180]), f=0,
    basis=np.array([3, 4, 5]), maximization=True), optimal=Model(c=Model.array([5, 0, 0, '2/9', '5/3', 0]),
    a=Model.array([[1, 1, 0, '1/9', '-1/6', 0], ['1/4', 0, 1, '-1/18', '5/24', 0], ['5/4', 0, 0, '-1/6', '-1/8', 1]]),
    b=Model.array([8, 20, 96]), f=400, basis=np.array([1, 2, 5]), maximization=True))

mock_models_2 = Models(
    not_optimal=Model(c=np.array([-3, -2, 5, 0, 0]), a=np.array([[4, -2, 2, 1, 0], [2, -1, 1, 0, 1]]),
        b=np.array([4, 1]), f=0, basis=np.array([3, 4]), maximization=False))

mock_models_3 = Models(not_optimal=Model(c=np.array([2, -3, 6, 1, 0, 0]),
    a=np.array([[2, 1, -2, 1, 0, 0], [1, 2, 4, 0, 1, 0], [1, -1, 2, 0, 0, -1]]), b=np.array([24, 22, 10]), f=0,
    maximization=True).to_m_task(), optimal=Model(c=np.array([0, 0, 0, '4/3', 0, '8/3', '3001/3', 1000, '2992/3']),
    a=np.array([[0, 1, 0, '1/12', '1/4', '5/12', '1/12', '1/4', '-5/12'],
                [0, 0, 1, '-1/8', '1/8', '-1/8', '-1/8', '1/8', '1/8'], [1, 0, 0, '1/3', 0, '-1/3', '1/3', 0, '1/3']]),
    b=np.array(['10/3', 1, '34/3']), f=Model.to_type('-56/3'), basis=np.array([1, 2, 0]), maximization=True))

mock_models_4 = Models(not_optimal=Model(c=np.array([2, -3, 6, 1, 0, 0]),
    a=np.array([[2, 1, -2, 1, 0, 0], [1, 2, 4, 0, 1, 0], [1, -1, 2, 0, 0, -1]]), b=np.array([24, 22, 10]), f=0,
    maximization=False).to_m_task(),
                       optimal=Model(c=np.array([-2.0, -8.0, 0.0, 0.0, -2.0, 0.0, -1001.0, -1002.0, -1000.0]),
                           a=np.array([[2.5, 2.0, 0.0, 1.0, 0.5, 0.0, 1.0, 0.5, 0.0],
                                       [-0.5, 2.0, 0.0, 0.0, 0.5, 1.0, 0.0, 0.5, -1.0],
                                       [0.25, 0.5, 1.0, 0.0, 0.25, 0.0, 0.0, 0.25, 0.0]]), b=np.array([35.0, 1, 5.5]),
                           f=-68, basis=np.array([3, 5, 2]), maximization=False))
