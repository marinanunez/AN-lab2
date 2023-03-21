import numpy as np
from aux import *

# Interpetacion del problema:
# En el sistema de ecuaciones propuesto para resolver el problema de
# los tres rersortes, primero igualo las derivadas a 0. Esto es:

# 0 = 2k * (x_2 - x_1) + m_1 * g -  k * x_1
# 0 = k * (x_3 - x_2) + m_2 * g - 2k * (x_2 - x_1)
# 0 = m_3 * g  - k * (x_3 - x_2)

# Planteo el sistema Kx=w con w=[g*m_1,g*m_2,g*m_3], g=9.8
# m_1=2, m_2=3, m_3=2.5, k=10

# Ahora despejo las componentes de w de la ecuacion anterior:
# m_1 * g = k * x_1 - 2k * (x_2 - x_1)
# m_2 * g = 2k * (x_2 - x_1) - k * (x_3 - x_2)
# m_3 * g = k * (x_3 - x_2)

# Ahora distribuyo y opero para obtener los coeficientes de las ecuaciones:
# m_1 * g =  3k x_1 - 2k x_2 + 0 x_3
# m_2 * g = -2k x_1 + 3k x_2 - k x_3
# m_3 * g =   0 x_1 -  k x_2 + k x_3


g = 9.8
k = 10.0
m_1 = 2.0
m_2 = 3.0
m_3 = 2.5

matriz_k = np.array([[3*k, -2*k, 0.0], [-2*k, 3*k, -k],[0.0, -k, k]])

matriz_w = np.array([m_1 * g, m_2 * g, m_3 * g])


# El problema a resolver entonces es Kx=w
# Voy a usar la forma de descomposicion PLU, K=PLU
P, L, U = lu(matriz_k)

e1 = np.array([1., 0., 0.])
D = soltrinf(L, e1)
firstColumn = soltrsup(U, D)

e2 = np.array([0., 1., 0.])
D = soltrinf(L, e2)
secondColumn = soltrsup(U, D)

e3 = np.array([0., 0., 1.])
D = soltrinf(L, e3)
thirdColumn = soltrsup(U, D)

# Main
print("La matriz K es:")
print(matriz_k)

# Muestro la inversa de K
print()
inverse_of_k = np.transpose(np.array([firstColumn, secondColumn, thirdColumn]))
print("La inversa de la matriz K es:")
print(inverse_of_k)

#planteo el sistema para encontrar los desplazamientos.


matriz_k = np.array([[3*k, -2*k, 0.0], [-2*k, 3*k, -k],[0.0, -k, k]])

matriz_w = np.array([m_1 * g, m_2 * g, m_3 * g])

solucion = sollu(matriz_k, matriz_w)
print("La solucion es:")
print(solucion)
