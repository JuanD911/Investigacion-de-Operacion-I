import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.ufunclike import fix 

x = np.arange(-8,8)

gx = (12-2*x)/6
tx = (7-x)/4

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.plot(0,2,'go',markersize=8)
plt.plot(6,0,'ro',markersize=8, label = '(6,0) Punto de Maximizacion')
plt.plot(0,1.75,'go',markersize=8)
plt.plot(7,0,'go',markersize=8)

y3 = np.minimum(gx,tx)

plt.fill_between(x,0,y3,color='c',alpha=0.75,label='Area Solucion') 


plt.plot()

plt.plot(x,gx,label='$y \leq (12-2x)/6$')
plt.plot(x,tx,label='$y \leq (7-x)/4$')
plt.axis(ymin=0)
plt.axis(xmin=0)
plt.grid(True, which='both')
plt.legend()
plt.show()