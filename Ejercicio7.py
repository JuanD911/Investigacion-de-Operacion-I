#Importación de la libreria scipy
from scipy.optimize import  linprog
import math

#Declara la funcion objetivo
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [-200,-100] # P = 200x + 100y

#restricciones


"""
Se declara el lado izquierdo de las restricciones
"""

left_side_restrictions = [
    [5,3],# 5x + 3y
    [2,4],# 2x + 4y
]

"""
Se declara el lado derecho o el elemento independiente de las restricciones
"""

right_side_restrictions = [105,70]

"""
Se usa el modulo linprog que lo que hace es que toma como argumentos la funcion obejtivo, las restricciones y el lado derecho
de las restricciones para luego aplicar el metodo simplex, integrado en la libreria
"""

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("------"+"Metodo Simplex"+"------")
print("Funcion Objetivo: p = 200x + 100y")
print("\nRestricciones:\n")
print("5x + 3y <= 105")
print("2x + 4y <= 70")
print("")

"""
Se imprimen los valores del que la funcion linprog calcula anteriormente, y se guardan en una variable solution, para luego mostrar
los valores, tanto de las variables, como el valor de maximizacion o minimizacion
"""

print("Valor de Optimizacion (Maximizar): "+str(int(math.fabs(solution.fun))))
print("")
print("Valor de las Variables")
print(solution.x)