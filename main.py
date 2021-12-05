import numpy as np

from gomori_method import GomoriMethod
from model import Model
from model_parser import parse

if __name__ == '__main__':
    # print(GomoriMethod.solve(mock_models_1.not_optimal))

    asd = Model(
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

    print(asd)
    print(GomoriMethod.solve(asd))
    # maximum, model_ = parse('model.txt')
    # model_ = np.array(model_)
    # A_ = model_[0:model_.shape[0] - 1, 1:model_.shape[1]]
    # c_ = model_[-1, 1:model_.shape[1]]
    # b_ = model_[0:model_.shape[0] - 1, 0]
    #
    # mdl = Model(c_, A_, b_, 0, maximum)
    # print(mdl.has_valid_basis())
    # mdl.to_m_task()
    # print(mdl.has_valid_basis())
    # print(mdl)
    # SimplexMethod.solve(mdl)
    # exit()
    #
    # # print(maximum, model)
    # # for m in model:
    # #     print(m)
    # m_method = MMethod(model_, [None for i in range(len(model_) - 1)], maximum)
    # m_method.m_task()
    # print('\n')
    # for m in m_method.Table:
    #     print(m)
    # exit()
    # gomori_method = GomoriMethod(m_method.Table, m_method.basis, maximum)
    # gomori_method.solve_gomori()
    # for m in model:
    #     print(m)
