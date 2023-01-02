import numpy as np


def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

    print(np.array(matrix))


if __name__ == '__main__':
    rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
