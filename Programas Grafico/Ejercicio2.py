import numpy as np 
import matplotlib.pyplot as plt  

plt.plot(-5,5,'go',markersize=10) 
plt.plot(5,5,'go',markersize=10) 
plt.plot(5,-10,'go',markersize=10) 
plt.plot(-5,-10,'go',markersize=10) 

# Grafica del área solución   
plt.fill([-5,5,5,-5,-5],[5,5,-10,-10,5],'y',alpha=0.75, label = 'Area solucion')  

# Grafica
plt.hlines(5,xmin = -5, xmax = 5,color = 'blue', label = '$y \leq 5$') 
plt.axhline(0, color="black")
plt.axvline(0, color="black") 

plt.grid(True, which='both')
plt.legend()  
plt.show()