import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

# Inecuacion

def f1(x):
    return 5-(2*x)

# Variable independiente

x = Symbol('x')

# Puntos para graficar

x1, =  solve(f1(x))
x2 =  0
x3 =  0

y1 = f1(x1)
y2 = 0
y3 = f1(x3)

# Puntos interseccion

plt.plot(x1,y1,'go',markersize=10)
plt.plot(x2,y2,'go',markersize=10)
plt.plot(x3,y3,'go',markersize=10)

# Gráfica del área solución

plt.fill([x1,x2,x3,x1],[y1,y2,y3,y1],'y',alpha=0.75, label = 'Area Solucion')

xr = np.linspace(-1,4,100)
y1r = f1(xr)

# Grafica

plt.plot(xr,y1r, label = '$y \less 5 - 2x$')
plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid(True, which='both')
plt.legend()
plt.show()
