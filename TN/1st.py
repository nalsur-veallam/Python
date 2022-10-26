import numpy as np
from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import pylab as plt

q = np.array([0, 1])

CNOT = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 0, 1],[0, 0, 1, 0]]).reshape(2, 2, 2, 2)

gamma = np.array([[0, -1.j], [1.j, 0]])
X = np.array([[0, 1], [1, 0]])
H = 1/np.sqrt(2)*np.array([[1, 1], [1, -1]])

q1 = np.einsum('i, ij->j', q, gamma)
q2 = np.einsum('i, ij->j', q, X)
q3 = np.einsum('i, ij->j', q, H)

q1_q2 = np.einsum('i, j, ijkl->kl', q1, q2, CNOT)

scalar = np.einsum('ij, k, i, j, k', q1_q2, q3, q, q, q)

print(np.tensordot(np.tensordot(q1, q2, axes=0), q3, axes=0))

circ = QuantumCircuit(3)
circ.y(qubit=0)
circ.x(qubit=1)
circ.h(qubit=2)
circ.cnot(control_qubit=0, target_qubit=1)
circ.draw('mpl')
plt.show()


state = Statevector.from_int(0, 2**3)
state = state.evolve(circ)
print(state)
