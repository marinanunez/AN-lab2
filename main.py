import numpy as np
from math import pi,sin
import matplotlib.pyplot as plt
from ejercicio1 import ivander, ilagrange

def main():
    #Genera las listas
    x = np.linspace(0, 2*np.pi, 55)
    y = [np.sin(p) for p in x]
    z = np.linspace(0, 2*np.pi, 100)

    lagrange_z = ilagrange(x, y, z)
    ivander_z = ivander(x, y, z)

    # Configuracion de los graficos
    figure, (axis1, axis2) = plt.subplots(1, 2)
    axis1.plot(x, y, '*')
    axis1.plot(z, lagrange_z)
    axis1.legend(['f(x)', 'lagrange'])

    axis2.plot(x, y, '*')
    axis2.plot(z, ivander_z)
    axis2.legend(['f(x)', 'ivander'])


    plt.show()
main()