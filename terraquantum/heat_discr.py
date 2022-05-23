import numpy as np
import tt
import time
from tt.amen import amen_solve

def initial_cond(T0, dx):
    t0 = T0*tt.ones(2, 3*dx)
    
    t0 = t0.round(1e-14)

    return t0

def vector(dx, dt, tau, I0, r02, k_sc, k_abs, rho, Cv, T0):
    nx = 2 ** dx # number of points in space
    nt = 2 ** dt # number of points in time
    
    bx = 1 # [0, b] - interval
    hx = bx / (nx - 1) # step 
    bt = 1 # [0, b] - interval
    ht = bt / (nt - 1) # step 
    
    
    x = hx * tt.xfun(2, dx) # coordinates generation
    ex = tt.ones(2, dx)
    t = ht * tt.xfun(2, dt) # coordinates generation
    et = tt.ones(2, dt)

    t0 = (T0 - 1)*tt.delta(2, dx, center = 0) # initial conditions for spatial
    t0 = tt.mkron(ex, ex, ex, et) + tt.mkron(t0, t0, t0, et)
    
    X = tt.mkron(x, ex, ex, et)
    Y = tt.mkron(ex, x, ex, et)
    Z = tt.mkron(ex, ex, x, et)
    T = tt.mkron(ex, ex, ex, t)
    
    Qs = tt.multifuncrs([X, Y, Z, T], lambda arg: I0 * (arg[:, 3]/tau *np.exp(-arg[:, 3]/tau)) * 
                        (np.exp( -(arg[:,1]**2 - arg[:,2]**2) / r02*np.exp(k_sc*arg[:,0]) ) * 
                         np.exp(-(k_sc + k_abs) * arg[:, 0]))  , 1e-14, verb = True)
    Qs = Qs + t0
    Qs = Qs.round(1e-14)
    
    return 1/(rho*Cv) * Qs

def matrix(dx, rho, Cv, k_t):
    Idx = tt.eye(2, 3*dx) # identity tensor
    
    delta = tt.qlaplace_dd([dx, dx, dx]) # laplasian
    
    return - k_t/(rho*Cv) * delta

def full_matrix(A, Qs, t0, pt, dt):
    support =  -tt.delta(2, pt, center = 1) + tt.delta(2, pt, center = 0)
    G_t = tt.Toeplitz(support,kind='L').T
    G_t = G_t.round(1e-14)
    
    support =  tt.delta(2, pt, center = 1) + tt.delta(2, pt, center = 0)
    M_t = tt.Toeplitz(support,kind='L').T
    M_t = M_t.round(1e-14)
    
    px = A.n.shape[0]
    Id = tt.eye(2, px)
    
    A_full = tt.kron(Id, G_t) - 0.5 * dt * tt.kron(A, M_t)

    A_full = A_full.round(1e-14) # collected full matrix A
    
    e1 = tt.delta(2, pt, center = 0)

    left = t0 + 0.5* dt * tt.matvec(A, t0)
    left = left.round(1e-14)
    left = tt.kron(left, e1)
    left = left.round(1e-14)
    
    right = dt * Qs

    Qs_full = left + right

    Qs_full = Qs_full.round(1e-14)

    return A_full, Qs_full

#consts
I0 = 1
rho = 1
tau = 1
r02 = 1
k_sc = 1
k_abs = 1
k_t = 1
Cv = 1
T0 = 1

#tensor dim
dx = 50
pt = 50
dt = 1e-10

#initialisation'
t1 = time.time()
A = matrix(dx, rho, Cv, k_t)
Qs = vector(dx, pt, tau, I0, r02, k_sc, k_abs, rho, Cv, T0)
t0 = initial_cond(T0, dx)
A, Qs = full_matrix(A, Qs, t0, pt, dt)

y = amen_solve(A, Qs, Qs, 1e-14)
t2 = time.time()
print('error:', (tt.matvec(A, y) - Qs).norm() / Qs.norm())
print('time:', (t2-t1))
    
    
