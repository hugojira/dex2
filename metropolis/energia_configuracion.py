# autor: Hugo de Jesus Valenzuela Chaparro
# Universidad de Sonora, septiembre 2019
# Curso Desarrollo Experimental 2
# ************** energia configuracion inicial: ******************
# Este codigo es una funcion que sirve como subrutina  para calcular
#
# SISTEMA: bidimensional de particulas discos
# UNIDADES REDUCIDAS: sigma-beta

# librerias requeridas para que funcione el programa
import numpy as np
# --------------------------------------------------

# X: posiciones en x
# Y: posiciones en y
# N: numero de particulas
# DENS: concentracion reducida

def energia_configuracion(X, Y, N, DENS):


# ------------------- calculos preliminares ------------------------
# lado reducido de la celda
    boxL = ((1.0*float(N))/float(DENS))**(1.0/2.0)
# fraccion en area phit = pi*DENS/4
    phit = (float(DENS)*np.pi)/4.0
# distancia a partir de la cual ya es sumamente despreciable el potencial
    Rcut = boxL/2.0
# el diametro de las particulas
    sigma = 1.0
# --------------------------------------------------------------------

# calibrar energia inicial a 0
    V = 0.0
    # loops para calcular las energias
    for i in range(0, int(N - 1)):
        #print("La i es:", i)
        rxi = X[i]
        ryi = Y[i]
        for j in range(i + 1, int(N)):
            #print("La j es:", j)
            rxij = rxi - X[j]
            ryij = ryi - Y[j]
            # ** condicion de imagen minima **
            rxij = rxij - boxL*np.around(rxij/boxL)
            ryij = ryij - boxL*np.around(ryij/boxL)

            # ***** MODELO DE POTENCIAL DE INTERACCION *****
            # ***** Discos Duros (HD) *****
            rijSQ = np.sqrt(rxij*rxij + ryij*ryij)
            if rijSQ < Rcut:
                if rijSQ <= 1.0:
                    Vij = 1.0e10
                else:
                    Vij = 0.0
                V = V + Vij
            else:
                pass

# dar resultados (la energia)
    return V
