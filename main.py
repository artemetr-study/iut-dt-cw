import numpy as np

from model import Model
from model_parser import parse
from gomori_method import GomoriMethod
from simplex_method import SimplexMethod
from gomori_method_mocks import mock_models_1

if __name__ == '__main__':
    print(GomoriMethod.solve(mock_models_1.not_optimal))

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
