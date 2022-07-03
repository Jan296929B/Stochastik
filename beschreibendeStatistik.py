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
    arr1 = [3, 7, 12, 18, 19, 20, 25, 25, 27, 28, 29, 31, 32, 34, 37, 38, 40, 41, 45, 47]
    arr2 = [3,2,10,7,0,3,5,0,6,1]
    arr = [24,27,14,15,30,26,15,33,18,30]
    print('Arithmetisches Mittel', np.mean(arr)) # arithmetisches Mittel
    print('Median:', statistics.median(arr)) # median 2 Quartil
    print('Modalwert(ACHTUNG! es koennten mehr geben)', statistics.mode(arr)) # Modalwert (mode of given data set)
    print('10% Quantil', np.quantile(arr, .10, interpolation="midpoint"))  # 10% Quantil
    print('25% Quantil', np.quantile(arr, .25, interpolation="midpoint")) # 25% Quantil 1 Quartil
    print('30% Quantil', np.quantile(arr, .30, interpolation="midpoint")) # 30% Quantil
    print('66% Quantil', np.quantile(arr, 0.66, interpolation="midpoint")) # 66% Quantil
    print('75% Quantil', np.quantile(arr, 0.75, interpolation="midpoint"))  # 75% Quantil 3 Quartil
    print('90% Quantil', np.quantile(arr, 0.90, interpolation="midpoint"))  # 90
    # % Quantil
    print('Varianz:', statistics.variance(arr)) # Varianz
    print('Standardabweichung:', statistics.stdev(arr)) #Standartabweichung
    q3, q1 = np.percentile(arr, [75, 25])# Interquantilabstand ist immer zwischen x0.25 und x0.75 also zwischen erstes quantil und drittes quantil
    print('Interquartilabstand:', q3 - q1)
    print('Spannweite:', max(arr) - min(arr))# Spannweite max - min
    print('Empirische Standartabweichung', empirischeStd(arr))# Die Standardabweichung einer Stichprobe, also die empirische Standardabweichung 1/(n-1) anstatt nur n
    print('Empirischer Korrelationskoeffizient', np.corrcoef(arr,arr2))# Eintraege der Nebendiagonale verwaenden

if __name__ == '__main__':
    stichprobe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
