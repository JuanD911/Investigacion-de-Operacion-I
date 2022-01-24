import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.ufunclike import fix 

x = np.arange(-8,16)

gx = (15-x)/5
tx = (15-5*x)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.plot(0,3,'go',markersize=8)
plt.plot(15,0,'go',markersize=8)
plt.plot(2.5,2.5,'ro',markersize=8, label = '(5/2,5/2) Punto de Maximizacion')
plt.plot(0,15,'go',markersize=8)
plt.plot(3,0,'go',markersize=8)

y3 = np.minimum(gx,tx)

plt.fill([15,0,2.5,15,0,0],[0,15,2.5,0,60,15],color='c',alpha=0.75,label='Area Solucion') 


plt.plot()

plt.plot(x,gx,label='$y \geq (15-x)/5$')
plt.plot(x,tx,label='$y \geq 15-5x$')
plt.axis(ymin=0)
plt.axis(xmin=0)
plt.grid(True, which='both')
plt.legend()
plt.show()