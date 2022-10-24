import numpy as np

data = np.loadtxt("al.txt")

pb_data = np.loadtxt("data.txt")

new_data = data.copy()

new_data[:,0] = pb_data[:,1]
new_data[:,1] = pb_data[:,0]

np.savetxt('pb.txt', new_data)
