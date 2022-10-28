import sympy as sp
from krok_goldstein import goldstein

pp = sp.Matrix([[0],[0]])
d = sp.Matrix([[1],[0]])
beta = 2/5
Tr = 9
epsilon = 10**(-5)
funkcja = 'x1**2+2*x2**2-6*x1**1+x1*x2**1'

# funkcja = 'x1**3+x1*x2**3'
nic = 0

# tau = goldstein(pp, d, beta, Tr, epsilon, funkcja, nic)
tau = goldstein(funkcja, pp, d, beta, Tr, epsilon, nic)

print(tau)
