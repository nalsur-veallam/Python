import numpy as np
from scipy.linalg import eigh
import pandas as pd

Y = 1
h = 1
r = 5

pauli_z = np.array([[1, 0],[0, -1]])
pauli_x = np.array([[0, 1],[1, 0]])

Id = np.array([[1, 0],[0, 1]])
null = np.array([[0,0],[0,0]])

psi = []
psi.append(np.random.rand(2, r))
psi.append(np.random.rand(r, 2, r))
psi.append(np.random.rand(r, 2))

H = []
H.append(np.array([h*pauli_x, Y*pauli_z, Id]))
H.append(np.array([[Id, null, null],
              [pauli_z, null, null],
              [h*pauli_x, Y*pauli_z, Id]]))
H.append(np.array([Id, pauli_z, h*pauli_x]))

vec = np.einsum('il,ljm,mk->ijk', psi[0], psi[1], psi[2])
norm = np.sqrt(np.einsum("ijk,ijk", vec, vec))**(1/3)

psi[0] = 1/norm*psi[0]
psi[1] = 1/norm*psi[1]
psi[2] = 1/norm*psi[2]

Ham = np.einsum('ijk,ilmn,lop->jmoknp', H[0], H[1], H[2]).reshape(8,8)

eigval, eigvec = np.linalg.eig(Ham)

for step in range(3):
    A = np.einsum('ijk,kl,sut,rspj,rml,opn,nm->ituo', psi[1], psi[2], H[0], H[1], H[2], psi[1], psi[2]).reshape((2*r,2*r))
    B = np.einsum('ijk,kl,njm,ml,op->iopn', psi[1], psi[2], psi[1], psi[2], Id).reshape((2*r,2*r))

    B = B + np.eye(2*r)

    eigvals, eigvecs = eigh(A, b = B, type=1)
    table = pd.DataFrame(columns=['val', 'vec'])
    table['val'] = eigvals
    table['vec'] = eigvecs
    table = table.sort_values(by=['val'], ascending=True)
    psi[0] = np.array(table['vec']).reshape((2, r))
    
    A = np.einsum('ij,lm,nio,npkr,pms,ou,ts->jklurt', psi[0], psi[2], H[0], H[1], H[2], psi[0], psi[2]).reshape((2*r**2,2*r**2))
    B = np.einsum('ij,lm,ik,nm,op->jolkpn', psi[0], psi[2], psi[0], psi[2], Id).reshape((2*r**2,2*r**2))

    B = B + 1e-5*np.eye(2*r**2)

    eigvals, eigvecs = eigh(A, b = B, type=1)
    table = pd.DataFrame(columns=['val', 'vec'])
    table['val'] = eigvals
    table['vec'] = eigvecs
    table = table.sort_values(by=['val'], ascending=True)
    psi[1] = np.array(table['vec']).reshape((r, 2, r))
    
    A = np.einsum('ijk,lk,sut,rspj,rml,opn,mn->ituo', psi[1], psi[0], H[0], H[1], H[2], psi[1], psi[0]).reshape((2*r,2*r))
    B = np.einsum('ijk,lk,njm,lm,op->iopn', psi[1], psi[0], psi[1], psi[0], Id).reshape((2*r,2*r))

    B = B + 1e2*np.eye(2*r)

    eigvals, eigvecs = eigh(A, b = B, type=1)
    table = pd.DataFrame(columns=['val', 'vec'])
    table['val'] = eigvals
    table['vec'] = eigvecs
    table = table.sort_values(by=['val'], ascending=True)
    psi[2] = np.array(table['vec']).reshape((r, 2))
    
    
err = (np.sqrt(np.sum(np.abs((eigvec).flatten())**2)) - np.sqrt(np.sum(np.abs((np.einsum('il,ljm,mk->ijk', psi[0], psi[1], psi[2])).flatten())**2)))/np.sqrt(np.sum(np.abs((eigvec).flatten())**2))

print(err)

