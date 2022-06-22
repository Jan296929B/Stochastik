import math

import matplotlib.pyplot as plt
import numpy
import statistics
from math import comb

import numpy as np
from scipy import stats
from scipy.stats import poisson, hypergeom

# Quantitative Daten sind Zahlen und Merkmale, die objektiv gemessen werden können: Maße wie Höhe, Breite und Länge, Temperatur ect....
# Qualitative Daten beziehen sich auf Merkmale und Beschreibungen, die nicht gemessen, sondern nur subjektiv beobachtet werden können, z.B. Gerüche ect....

# Diskrete Daten sind Anzahlen, die nicht genauer gemacht werden könen. In der Regel handelt es sich um ganze Zahlen. z.B. Anzahl Kinder (2.5 Kinder geht nicht)
# Stetige Daten können hingegen immer feiner aufgeteilt bzw. präzisiert werden. So können Sie beispielsweise die Größe Ihrer Kinder auf immer genauere Skalen messen cm, mm....

# ordinale Daten haben eine natürliche Reihenfolge z.b. kurz, mittel oder lang
# nominale Daten sind nicht geordnet z.B. Farben anordnen

#absolute Häufigkeit

def empirischeStd(arr):
    mean = statistics.mean(arr)
    sum = 0
    for x in arr:
        sum += (x-mean)**2
    val = sum / (len(arr)-1)
    return math.sqrt(val)# Wurzel der empirischen Varianz = Emp. Std.


def stichprobe():
    arr3 = [3, 4, 5, 1, 5, 2, 1, 3, 1, 3]
    arr2 = [18,37,61,125,59]
    arr = [3, 4, 5, 1, 5, 2, 1, 3, 1, 3]
    print('Arithmetisches Mittel', np.mean(arr)) # arithmetisches Mittel
    print('Median:', statistics.median(arr)) # median
    print('Modalwert', statistics.mode(arr)) # Modalwert (mode of given data set)
    print('10% Quantil', np.quantile(arr, .10))  # 10% Quantil
    print('25% Quantil', np.quantile(arr, .25)) # 25% Quantil
    print('30% Quantil', np.quantile(arr, .30)) # 30% Quantil
    print('66% Quantil', np.quantile(arr, 0.66))# 66% Quantil
    print('75% Quantil', np.quantile(arr, 0.75))  # 75% Quantil
    print('90% Quantil', np.quantile(arr, 0.90))  # 90
    # % Quantil
    print('Varianz:', statistics.variance(arr)) # Varianz
    print('Standartabweichung:', statistics.pstdev(arr)) #Standartabweichung
    q3, q1 = np.percentile(arr, [75, 25])# Interquantilabstand ist immer zwischen x0.25 und x0.75 also zwischen erstes quantil und drittes quantil
    print('Interquartilabstand:', q3 - q1)
    print('Spannweite:', max(arr) - min(arr))# Spannweite max - min
    print('Empirische Standartabweichung', empirischeStd(arr))# Die Standardabweichung einer Stichprobe, also die empirische Standardabweichung 1/(n-1) anstatt nur n
    print('Empirischer Korrelationskoeffizient', np.corrcoef(arr,arr2))# Eintraege der Nebendiagonale verwaenden

if __name__ == '__main__':
    stichprobe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
