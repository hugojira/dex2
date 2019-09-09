np.random.seed(4958202) # semilla para poder hacer los numeros reproducibles
# generar posiciones
for i in range(0, int(N)):
    print("la iesima es", i)
    # numeros aleatorios para generar las posiciones
    deltax = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
    deltay = np.random.uniform(low = 0, high = 1, size = 1) - 0.5
    print("el deltax fue", deltax)
    print("el deltay fue", deltay)
    # posiciones
    X[i] = deltax*boxL
    Y[i] = deltay*boxL
    for j in range(0, i): # loop para impedir traslapes
        xij = X[i] - X[j]
        yij = Y[i] - Y[j]
        #print("la jota es", j)

        # distancia entre centros de particulas
        RO = xij**2 + yij**2
        if RO <= sigma:
            print("traslape en", i, j)
            print("se traslapo la delta x mi compa, y fue", deltax)
            print("se traslapo la delta y mi compa, y fue", deltay)
            break # salir de loop en j y regresar a loop en i
        else:
            pass

#print("las posiciones fueron", np.c_[X,Y])
