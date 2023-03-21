# NUÑEZ HEREDIA, MARINA ROCIO
# Analisis Numerico - Parcial 2
# Ejercicio 1


import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


#Funcion para el metodo de Vandermonde
def ivander(x,y,z):   	 

    if(len(y) != len(x)):
        print("Los arreglos son de distinto tamaño")
    return None
   	
    x = np.array(x)
    y = np.array(y)

    n = len(x)

    #Obtengo matriz 
    vader = np.zeros(shape=(n,n),dtype =float)
    for i in range(0,n):
        for j in range(0,n):
            potencia = (n-1)-j
            vander[i,j] = x[i]**potencia

    # Resuelvo sistema de ecuaciones
    coeficiente = np.linalg.solve(vander,y)

    # Evalúo los valores de z con el polinomio
    val_z = []
    vali_z = 0

    n = len(coeficiente)
    
    for zi in z:
        for i in range(0,n):
            potencia = (n-1)-i
            vali_z += coeficiente[i]*(zi**potencia)
        val_z.append(vali_z)
        vali_z = 0
    return val_z


# Funcion para el metodo de Lagrange
def ilagrange(x, y, z):

    if len(x) != len(y):
        print("Los arreglos son de distinto tamaño")
        return None

    n = len(x)
    w = []

    for z_i in z:
        # sumatoria de los polinomios base l_i por y_i
        w_i = 0.0
        for idx in range(n):
            # productoria para generar el polinomio base l_i evaluado en z_i
            l_i = 1.0
            for jdx in range(n):
                if jdx != idx:
                    l_i = l_i * (z_i - x[jdx]) / (x[idx] - x[jdx])

            w_i = w_i + y[idx] * l_i

        w.append(w_i)
    return w