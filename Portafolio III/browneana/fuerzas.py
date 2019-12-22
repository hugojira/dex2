# ****
# **** CALCULO DE FUERZAS
# ****
# SUBROUTINE FRZAS(L)
# IMPLICIT DOUBLE PRECISION (A-H,O-Z)
# PARAMETER (NN1=810)
# COMMON /FUERZAS/ FX(NN1),FY(NN1),FZ(NN1)
# COMMON /POS1/ X(NN1),Y(NN1),Z(NN1)
# COMMON /VALORES/ DENS,RCUT,A,ZK,BOXL,NP,NS

# librerias necesarias para que funcione el programa
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------

def fuerzas(NP, BOXL, RCUT, ZK, A, X, Y, Z):

    ENPOT = 0.0 # calibrar energia potencial a cero

    # calibrar fuerzas a cero
    fx = np.zeros((int(NP), 1))
    fy = np.zeros((int(NP), 1))
    fz = np.zeros((int(NP), 1))

    for i in range(0, NP - 1):
        fxi = fx[i]
        fyi = fy[i]
        fzi = fz[i]
        for j in range(i + 1, NP):
            xij = X[i] - X[j]
            yij = Y[i] - Y[j]
            zij = Z[i] - Z[j]
            # convencion de imagen minima
            xij = xij - BOXL*np.around(xij/BOXL)
            yij = yij - BOXL*np.around(yij/BOXL)
            zij = zij - BOXL*np.around(zij/BOXL)

            rij = np.sqrt(xij**2 + yij**2 + zij**2)

            # verificando traslapes
            if rij <= 1.0:
                print("traslape en", i, " - ", j)
            else:
                pass

            # INICIA LA ESPECIFICACION DEL MODEL DE POTENCIAL DEL CUAL
            # SE DERIVDA LA FUERZA DE INTERACCION ENTRE LAS PARTICULAS
            if rij < RCUT:
                U = np.exp(-ZK*rij)
                U2 = A*U*(ZK*rij + 1.0)/(rij**3)
                ENPOT = (A*U)/rij + ENPOT

                fxij = (xij)*U2
                fyij = (yij)*U2
                fzij = (zij)*U2

                fxi = fxi + fxij
                fyi = fyi + fyij
                fzi = fzi + fzij

                fx[j] = fx[j] - fxij
                fy[j] = fy[j] - fyij
                fz[j] = fz[j] - fzij
            else:
                pass
            # 2  continue
        fx[i] = fxi
        fy[i] = fyi
        fz[i] = fzi
        # 3 continue
    # ESCRIBIR LA ENERGIA DE LA CONFIGURACION. IMPORTANTE PARA
    # VERIFICAR COMO TERMALIZA EL SISTEMA
    # write L, ENPOT/float(NP)
    #np.savetxt("ep.csv", np.c_[X,Y], delimiter=",")
    ENPOT = ENPOT/float(NP)
    return fx, fy, fz, ENPOT
