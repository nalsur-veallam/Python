import numpy as np

d = 50
n = 2
r = 5
index = 6

TT1 = []

TT1.append(np.random.rand(n, r))
for i in range(2,d):
    TT1.append(np.random.rand(r, n, r))
    
TT1.append(np.random.rand(r, n))


TT2 = []

TT2.append(np.random.rand(n, r))
for i in range(2,d):
    TT2.append(np.random.rand(r, n, r))
    
TT2.append(np.random.rand(r, n))

scalar = np.einsum("ij,ik->jk", TT1[0], TT2[0])
for i in range(2,d):
    scalar = np.einsum("jk,kon->jon", scalar, TT2[i-1])
    scalar = np.einsum("jon,jop->pn", scalar, TT1[i-1])
    
scalar = np.einsum("jk,ki->ji", scalar, TT2[-1])
scalar = np.einsum("ji,ji", scalar, TT1[-1])

print("Scalar product is", scalar)

elem = str(bin(index - 1))[2:]
for i in range(d-len(elem)):
    elem = "0" + elem

ind0 = np.array([1.0,0.0])
ind1 = np.array([0.0,1.0])
IND = []
for char in elem:
    if char == "0":
        IND.append(ind0)
    else:
        IND.append(ind1)
        
TT = []
TT.append(np.einsum("i,ij->j",IND[0],TT1[0]))

for i in range(2, d):
    TT.append(np.einsum("i,jik->jk",IND[i-1], TT1[i-1]))

TT.append(np.einsum("i,ji->j",IND[-1],TT1[-1]))

T = TT[0]
for i in range(2, d):
    T = np.einsum("i,ij->j", T, TT[i-1])

print("The element of the first vector at index", index-1, "is", np.einsum("i,i", T, TT[-1]))


#psi = []
#psi.append(np.random.rand(2, r))
#psi.append(np.random.rand(r, 2, r))
#psi.append(np.random.rand(r, 2))

#psi_s = np.einsum('il,ljm,mk->ijk', psi[0], psi[1], psi[2])
#psi_2 = np.einsum("ijk,ijk", psi_s, psi_s)

#scalar = np.einsum("ij,ik->jk", psi[0], psi[0])
#scalar = np.einsum("jk,kon->jon", scalar, psi[1])
#scalar = np.einsum("jon,jop->pn", scalar, psi[1])
#scalar = np.einsum("jk,ki->ji", scalar, psi[-1])
#scalar = np.einsum("ji,ji", scalar, psi[-1])

#print(psi_2 - scalar)

#d = 3
#psi = []
#psi.append(np.random.rand(2, r))
#psi.append(np.random.rand(r, 2, r))
#psi.append(np.random.rand(r, 2))

#TT1 = psi

#psi = np.einsum("ij,jkl,ln->ikn", psi[0], psi[1], psi[2]).reshape(8)

#print(psi)

#elem = str(bin(index - 1))[2:]
#for i in range(d-len(elem)):
    #elem = "0" + elem

#ind0 = np.array([1, 0])
#ind1 = np.array([0, 1])
#IND = []
#for char in elem:
    #if char == "0":
        #IND.append(ind0)
    #else:
        #IND.append(ind1)
        
#TT = []
#TT.append(np.einsum("i,ij->j",IND[0],TT1[0]))

#for i in range(2, d):
    #TT.append(np.einsum("i,jik->jk",IND[i-1], TT1[i-1]))

#TT.append(np.einsum("i,ji->j",IND[-1],TT1[-1]))

#T = TT[0]
#for i in range(2, d):
    #T = np.einsum("i,ij->j", T, TT[i-1])

#print(np.einsum("i,i", T, TT[-1]))
