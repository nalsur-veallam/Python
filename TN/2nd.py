import numpy as np
import pylab as plt

# O(d1^2 + d2^4)

d1 = 10
d2 = 8
A = np.zeros((d1,d1,d2,d2))
for i in range(d1):
    for j in range(d1):
        for k in range(d2):
            for l in range(d2):
                A[i, j, k, l] = np.sqrt((i + 1) + 2*(j + 1) + 3*(k + 1) + 4*(l + 1))
            
norm = np.sqrt(np.sum(np.abs(A.flatten())**2))
print("Frobenius norm of matrix is", norm)
A_ = A/norm

U, S, V = np.linalg.svd(A_.reshape(d1**2,d2**2))
norm_ = np.sqrt(np.sum(S**2))
print("Square root of the sum of the singular values squared is", norm_)

tol = 1e-4
eff_rank = np.sum(S > tol)
print("Effective rank (tol = 1e-4) is", eff_rank)

error = np.sqrt(np.sum((S[eff_rank : ])**2))
print("Truncation error is", error)

new_A = (U[:, : eff_rank] @ np.diag(S[: eff_rank]) @ V[: eff_rank, :]).reshape(d1,d1,d2,d2)
new_error = np.sqrt(np.sum(np.abs((A_ - new_A).flatten())**2))

print("New error is", new_error)

max_rank = len(S)

errors = []

for rank in range(1, max_rank):
    errors.append(np.sqrt(np.sum((S[rank : ])**2)))
    
plt.plot(np.arange(1, max_rank), errors, lw=3, c='r')
plt.xlabel('rank')
plt.ylabel('Truncation error')
plt.grid()
plt.show()

plt.plot(np.arange(2, 6), errors[1:5], lw=3, c='g')
plt.xlabel('rank')
plt.ylabel('Truncation error')
plt.grid()
plt.show()
    
