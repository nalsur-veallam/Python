import numpy as np


n = 50

A = np.zeros((n, n, n, n))
i, j, k, l = np.indices(A.shape)

A[i, j, k, l] = np.sin(i + j + k + l)
