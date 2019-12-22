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
# Z: posiciones en z
# N: numero de particulas
# DENS: concentracion reducida

def energia_configuracion(X, Y, Z, N, boxL, Rcut):



# calibrar energia inicial a 0
    V = 0.0
    # loops para calcular las energias
    for i in range(0, int(N - 1)):
        #print("La i es:", i)
        rxi = X[i]
        ryi = Y[i]
        rzi = Z[i]
        for j in range(i + 1, int(N)):
            #print("La j es:", j)
            rxij = rxi - X[j]
            ryij = ryi - Y[j]
            rzij = rzi - Z[j]
            # ** condicion de imagen minima **
            rxij = rxij - boxL*np.around(rxij/boxL)
            ryij = ryij - boxL*np.around(ryij/boxL)
            rzij = rzij - boxL*np.around(rzij/boxL)

            # ***** MODELO DE POTENCIAL DE INTERACCION *****
            # ***** Esferas Duras (HS) *****
            rijSQ = np.sqrt(rxij*rxij + ryij*ryij + rzij*rzij)
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
