import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

# =====================================================
# INGRESO DE FUNCION
# =====================================================

x = sp.Symbol('x')

funcion_str = input("Ingrese f(x): ")

f_sym = sp.sympify(funcion_str)
f = sp.lambdify(x, f_sym, "numpy")

a = float(input("Límite inferior: "))
b = float(input("Límite superior: "))

N = 12

# =====================================================
# VALOR EXACTO
# =====================================================

integral_exacta = float(sp.N(sp.integrate(f_sym, (x, a, b))))

# =====================================================
# TRAPECIO COMPUESTO
# =====================================================

def trapecio_compuesto(f, a, b, N):

    h = (b-a)/N

    suma = f(a) + f(b)

    for i in range(1, N):
        suma += 2*f(a+i*h)

    return h*suma/2


# =====================================================
# SIMPSON 1/3 COMPUESTO
# =====================================================

def simpson13_compuesto(f,a,b,N):

    h=(b-a)/N

    suma=f(a)+f(b)

    for i in range(1,N):

        if i%2==0:
            suma += 2*f(a+i*h)
        else:
            suma += 4*f(a+i*h)

    return h*suma/3


# =====================================================
# SIMPSON 3/8 COMPUESTO
# =====================================================

def simpson38_compuesto(f,a,b,N):

    h=(b-a)/N

    suma=f(a)+f(b)

    for i in range(1,N):

        if i%3==0:
            suma += 2*f(a+i*h)
        else:
            suma += 3*f(a+i*h)

    return 3*h*suma/8


# =====================================================
# DETECTAR POLINOMIO
# =====================================================

def grado_polinomio(expr):

    if expr.is_polynomial():

        return sp.Poly(expr,x).degree()

    return None


# =====================================================
# GAUSS LEGENDRE
# =====================================================

def gauss_legendre(f,a,b,n):

    puntos,pesos = leggauss(n)

    xp = (b-a)/2*puntos + (a+b)/2

    return (b-a)/2*np.sum(
        pesos*f(xp)
    )


# =====================================================
# ELECCION AUTOMATICA DE n
# =====================================================

grado = grado_polinomio(f_sym)

if grado is not None:

    n_optimo = int(np.ceil((grado+1)/2))

else:

    n_optimo = 5


# =====================================================
# CALCULOS
# =====================================================

trap = trapecio_compuesto(f,a,b,N)

simp13 = simpson13_compuesto(f,a,b,N)

simp38 = simpson38_compuesto(f,a,b,N)

gauss = gauss_legendre(f,a,b,n_optimo)

# =====================================================
# ERRORES
# =====================================================

err_trap = abs(integral_exacta-trap)

err_s13 = abs(integral_exacta-simp13)

err_s38 = abs(integral_exacta-simp38)

err_gauss = abs(integral_exacta-gauss)

# =====================================================
# TABLA
# =====================================================

print("\nValor exacto =", integral_exacta)

print("\nMétodo\t\t\tAprox.\t\tError")

print("-"*60)

print(f"Trapecio\t\t{trap:.10f}\t{err_trap:.10e}")

print(f"Simpson 1/3\t\t{simp13:.10f}\t{err_s13:.10e}")

print(f"Simpson 3/8\t\t{simp38:.10f}\t{err_s38:.10e}")

print(f"Gauss-Legendre n={n_optimo}\t{gauss:.10f}\t{err_gauss:.10e}")
