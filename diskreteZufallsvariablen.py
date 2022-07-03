import math

import matplotlib.pyplot as plt
import numpy
import statistics
from math import comb

import numpy as np
from scipy.stats import describe
from scipy import stats
from scipy.stats import poisson, hypergeom


def alleDaten():
    arr = [0.1, 0.1, 0.1, 0.2, 0.2, 0.3]
    arr1 = [1,2,3,4,3,2,1]
    print('Erwartungswert:', statistics.mean(arr)) #Erwartungswert
    print('Varianz:', statistics.pvariance(arr)) #Varianz pvariance wenn man alle daten hat
    print('Standartabweichung:', statistics.pstdev(arr)) #Standartabweichung ist die Wurzel der Varianz pstdev verwendet von allen daten (nicht empirisch)
    # Korrelationskoeffizient is Cov(X1, X2)/X1STd*X2Std # Je weiter der Korrelationskoeffizient von Null netfernt ist desto staerker ist die Beziehung



if __name__ == '__main__':
    alleDaten()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
