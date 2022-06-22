import numpy as np
from scipy.stats import binom, geom, poisson, hypergeom



if __name__ == '__main__':
    M = hypergeom(120, 20, 10) #20 Autos 10 davon Mercedes in Raum mit 5 Autos
    O = hypergeom(20, 5, 5)  # 20 Autos 5 davon Opel in Raum mit 5 Autos

    print(1-M.pmf(0)) # in Raum steht nur 1 Mercedes