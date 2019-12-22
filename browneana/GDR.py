# autor: Hugo de Jesús Valenzuela Chaparro
# Universidad de Sonora, octubre 2019
# Curso Desarrollo Experimental 2
#------------------------------------------------------------------
# SUBRUTINA PARA CALCULAR LA FUNCION DE DISTRIBUCION RADIAL
# A PARTIR DE LAS MATRICES DE CONFIGURACION CX, CY, CZ
# SISTEMA: BIDIMENSIONAL
# -----------------------------------------------------------------

# librerias requeridas para que funcione el programa
import numpy as np
# --------------------------------------------------

# X: posiciones en x
# Y: posiciones en y
# N: numero de particulas
# DENS: concentracion reducida
# KI2 aqui fue KI
# GDR for Brownian

def GDR(CX, CY, CZ, DENS, boxL, KI2, N, NN2, NN3):
    # declarar arreglos a utilizar
    #NHIST = np.zeros((int(NN3), 1))

    deltaR = 0.01e0
    MAXBIN = int(float(boxL)/2.0/deltaR)
    const_pi = (4.0e0)*np.arctan(1.0e0)

    # declarar arreglos a utilizar
    NHIST = np.zeros((int(MAXBIN), 1))

    for L in range(0, int(N)):
        for M in range(0, int(N)):
            if M == L:
                continue
            else:
                pass
            for J in range(0, KI2):
                XL0 = CX[L, J]
                XLT = CX[M, J]
                XL0T = XL0 - XLT

                YL0 = CY[L, J]
                YLT = CY[M, J]
                YL0T = YL0 - YLT

                ZL0 = CZ[L, J]
                ZLT = CZ[M, J]
                ZL0T = ZL0 - ZLT

                XL0T = XL0T - boxL*np.around(XL0T/boxL)
                YL0T = YL0T - boxL*np.around(YL0T/boxL)
                ZL0T = ZL0T - boxL*np.around(ZL0T/boxL)

                R0T = np.sqrt(XL0T**2 + YL0T**2 + ZL0T**2)

                NBIN = int(R0T/deltaR) + 1
                if NBIN <= MAXBIN:
                    NHIST[NBIN] = NHIST[NBIN] + 1
                else:
                    pass

    C1 = (4.0/3.0)*const_pi*DENS
    # arreglo para escribir datos
    gr2D = np.zeros((int(MAXBIN), 2))

    for NBIN in range(0, MAXBIN):
        RL = float(NBIN)*deltaR
        RU = RL + deltaR
        RT = RL + deltaR/2.0
        C2 = C1*(RU**3 - RL**3)
        GDRTA = float(NHIST[NBIN])/float(KI2)/float(N)/C2
        gr2D[NBIN, 0] = RT
        gr2D[NBIN, 1] = GDRTA
    return gr2D
