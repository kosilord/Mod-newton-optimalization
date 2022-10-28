from metoda_newtona import Newton
import sympy as sp

vektor_xk = []
vektor_tau = []
n = len(vektor_tau)
czy_min = False

# sprawdzane zmienne
# #funkcja Himmelblau'a
# epsilon = 10 ** (-3)
# tau = 9
# beta = 2 / 5
# pp = sp.Matrix([[10.3],[-21.1]])
# funkcja = "(x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2 - 200"
# nic = 0
# L = 100
# powod = 0
# wart = 0

# # funkcja testowa Geem'a
epsilon = 10 ** (-3)
tau = 9
beta = 2 / 5
pp = sp.Matrix([[9.4],[2.1]])
funkcja = "4*x1**2-2.1*x1**4+((x1**6)/3)+x1*x2-4*x2**2+4*x2**4"
nic = 0
L = 1000
powod = 0
wart = 0 

# # #funkcja eksponencjalna
# epsilon = 10 ** (-5)
# tau = 9
# beta = 2 / 5
# pp = sp.Matrix([[4.3],[-2.1]])
# funkcja = "sinx1*sinx2*e(-(x1**2+x2**2)"
# nic = 0
# L = 1000
# powod = 0



(vektor_xk, vektor_tau, czy_min, powod, wart) = Newton(pp, epsilon, L, beta, tau, funkcja, nic)

n = len(vektor_tau)
print('punkt: ' + str(vektor_xk[n]))
print('tau: ' + str(vektor_tau[n-1]))
print('ilość iteracji: ' + str(n))
print('czy min: ' + str(czy_min))
print('kryterium stop: ' + str(powod))
print('wartość kryterium stop: ' + str(wart))