import numpy as np

mat = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

print(np.all(mat >= 0))
print(np.linalg.eig(mat).eigenvectors[:, 1])