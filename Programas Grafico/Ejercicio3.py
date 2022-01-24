import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(-8,8)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.plot(7,4.5,'go',markersize=0)
plt.plot(-8,-3,'go',markersize=0)
plt.plot(-8,4.5,'go',markersize=0)

plt.fill([7,-8,-8],[4.5,-3,4.5],'y',alpha=0.75,label='Area Solucion')

y = (x+2)/2

plt.plot()

plt.plot(x,y,label='y > (x+2)/2')
plt.grid(True, which='both')
plt.legend()
plt.show()