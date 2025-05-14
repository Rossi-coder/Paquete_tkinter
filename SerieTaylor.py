import numpy as np
from math import *
import matplotlib.pyplot as plt
import sympy as sp
from sympy.plotting import plot

def PloliTaylor(a,n):
    x = sp.symbols('x')
    f = sp.cos(x)          #  Pueden poder la ecuacion que gusten 
    F = f
    T = f.subs(x,a)
    for i in range(1,n+1):
        dfi = sp.diff(f,x)
        T = T + dfi.subs(x,a)*((x-a)**(i))/factorial(i)
        f = dfi

    print(sp.expand(T))
    g = plot(F,T,(x,a-3,a+3), title='Polinomio de Taylor', show=False)
    g[0].line_color='g'
    g[1].line_color='b'
    g.show()

a = float(input('Digite al rededor de que punto desea que se analice el Polinomio de Taylor: '))
n = int(input('Digite el orden del polinomio de Taylor: '))

PloliTaylor(a,n)



