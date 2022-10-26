import numpy as np

def TT_decomp(A, r):
    TT = []
    n = A.shape[0]
    A_ = (A.copy()).reshape(n, -1)
    
    T, S, V = np.linalg.svd(A_)
    TT.append(T[:, :r])
    A_ = np.diag(S[:r])@V[:r, :]
    A_ = A_.reshape(n*r, -1)
    
    for i in range(2, len(A.shape)):

        T, S, V = np.linalg.svd(A_)
        TT.append(T[:, :r].reshape(r, n, r))
        A_ = np.diag(S[:r])@V[:r, :]
        A_ = A_.reshape(n*r, -1)
        
    TT.append(A_.reshape(r, n))
    return TT

n = 10
r = 2

A = np.zeros((n, n, n, n))
i, j, k, l = np.indices(A.shape)

A[i, j, k, l] = np.sin(i + j + k + l)

TT = TT_decomp(A, r)

print("Error for rank = 2 and n = 10 is", np.sqrt(np.sum(np.abs((A - np.einsum('ij,jkl,lmn,no->ikmo', TT[0], TT[1], TT[2], TT[3]) ).flatten())**2)))

r = 1
TT = TT_decomp(A, r)

print("Error for rank = 1 and n = 10 is", np.sqrt(np.sum(np.abs((A - np.einsum('ij,jkl,lmn,no->ikmo', TT[0], TT[1], TT[2], TT[3]) ).flatten())**2)))

n = 15
r = 2
A = np.zeros((n, n, n, n))
i, j, k, l = np.indices(A.shape)

A[i, j, k, l] = np.sin(i + j + k + l)
TT = TT_decomp(A, r)

print("Error for rank = 2 and n = 15 is", np.sqrt(np.sum(np.abs((A - np.einsum('ij,jkl,lmn,no->ikmo', TT[0], TT[1], TT[2], TT[3]) ).flatten())**2)))

r = 1
TT = TT_decomp(A, r)

print("Error for rank = 1 and n = 15 is", np.sqrt(np.sum(np.abs((A - np.einsum('ij,jkl,lmn,no->ikmo', TT[0], TT[1], TT[2], TT[3]) ).flatten())**2)))

n = 20
r = 2
A = np.zeros((n, n, n, n))
i, j, k, l = np.indices(A.shape)

A[i, j, k, l] = np.sin(i + j + k + l)
TT = TT_decomp(A, r)

print("Error for rank = 2 and n = 20 is", np.sqrt(np.sum(np.abs((A - np.einsum('ij,jkl,lmn,no->ikmo', TT[0], TT[1], TT[2], TT[3]) ).flatten())**2)))

r = 1
TT = TT_decomp(A, r)

print("Error for rank = 1 and n = 20 is", np.sqrt(np.sum(np.abs((A - np.einsum('ij,jkl,lmn,no->ikmo', TT[0], TT[1], TT[2], TT[3]) ).flatten())**2)))
