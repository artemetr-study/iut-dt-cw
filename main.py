from gomori_method_mocks import mock_models_3
from simplex_method import SimplexMethod

if __name__ == '__main__':
    print(SimplexMethod.solve(mock_models_3.not_optimal))
