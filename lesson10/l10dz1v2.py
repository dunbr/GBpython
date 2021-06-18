# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        n = self.matrix
        x = str(n).replace('], [', '\n').lstrip('[').rstrip(']').replace(',', '')
        return x

    def __add__(self, other):
        x = self.matrix
        b = other.matrix
        v = [x[i][c] + b[i][c] for i in range(len(x)) for c in range(len(x[i]))]
        n = [[v[i + b] for b in range(len(x[0]))] for i in range(0, len(v), len(x[0]))]
        x = str(n).replace('], [', '\n').lstrip('[').rstrip(']').replace(',', '')
        return x


# matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
# matrix2 = Matrix([[9, 10], [11, 12], [13, 14]])
# matrix1 = Matrix([[1, 2, 3], [3, 4, 4], [5, 6, 4]])
# matrix2 = Matrix([[9, 10, 2], [11, 12, 1], [13, 14, 6]])
matrix1 = Matrix([[1, 2, 3, 7], [3, 4, 4, 7], [5, 6, 4, 6]])
matrix2 = Matrix([[9, 10, 2, 1], [11, 12, 1, 7], [13, 14, 6, 6]])
print(matrix1)
print('-'*20)
print(matrix2)
print('+'*20)
print(matrix1 + matrix2)
