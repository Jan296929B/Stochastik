# -*- coding: utf-8 -*-
"""
KAP3_STETIGEVERTEILUNGEN

"""

import numpy as np
from scipy.stats import uniform, expon, norm

# not necessary helper function for displaying results a bit nicer

def stetigeVerteilung():
    print('Beispiele aus Kaptitel 3 "Stetige Verteilungen"')


    # Gleichverteilung
    # Eve hat liest Meldungen in ihrer Twitter-Timeline.
    # Die Zeit, die sie für das Lesen eines Beitrags braucht
    # wird durch die Zufallsvariable X ∼ U(5, 300) für die Lesezeit in Sekunden
    # beschrieben

    l = 50
    s = 180-l
    X = uniform(loc=l,scale=s)

    print(' ')
    print('Twitterlesezeiten von Eve (gleichverteilt)')
    print(' ')


    print("Gleichverteiltung Kleiner gleich:", X.cdf(500))
    print("Gleichverteiltung Mehr als:", X.sf(100))
    print("Gleichverteilung zwischen:", X.cdf(300)-X.cdf(200))

    E_X = X.mean()
    print('Gleichverteilung Erwartungswert: ' + myprint(E_X))

    print('Gleichverteilung Varianz', X.var())
    std_X = X.std()
    print('Gleichverteilung Standartabweichung σ: ' + myprint(std_X))

    print(' ')


    # Exponentialverteilung
    # Ein Paar Laufschuhe hält im Mittel 18 Monate, falls diese täglich
    # benutzt werden. Die Zeit, die Laufschuhe nutzbar sind, bevor sie
    # kaputt gehen, ist also Y~expon(1/18)

    lamb = 1/7
    Y = expon(loc=0,scale=lamb)


    print(' ')
    print('Nutzungsdauer von Laufschuhen (exponentialverteilt)')
    print(' ')
    print("Exponentialverteilung Kleiner gleich:", Y.cdf(2/7))
    print("Exponentialverteilung Mehr als:", Y.sf(1000)) #bsp. mehr als eine halbe minute = Y.sf(0.5)
    print("Exponentialverteilung zwischen:", Y.cdf(10) - Y.cdf(5))

    E_Y = Y.mean()
    print('Exponentialverteilung Erwartungswert: ' + myprint(E_Y))

    print('Exponentialverteilung Varianz', Y.var())
    print('Exponentialverteilung Median:', Y.ppf(0.5))
    std_Y = Y.std()
    print('Exponentialverteilung Standartabweichung σ: ' + myprint(std_Y))
    Quant_Y75 = Y.ppf(0.75)
    print('Exponentialverteilung: Quant_Y75 = ' + myprint(Quant_Y75)) #75% der faelle nicht ueberschritten

    Quant_Y90 = Y.ppf(0.90)
    print('Exponentialverteilung: Quant_Y90 = ' + myprint(Quant_Y90))  # 90% der faelle nicht ueberschritten

    print(' ')



    # Normalverteilung
    # Die Größe eines zufällig ausgewählten deutschen Mannes ist eine
    # Zufallsvariable X ∼ N(180.3, 7.17).
    print(' ')
    print('Körpergröße von Männern (normalverteilt)')
    print(' ')

    mu = 13 #Erwartungswert
    sig = 1 #Standartabweichung
    Z = norm(loc=mu,scale=sig) #N(mu, sig)

    print("Normalvertielt-kleinerGleich:", Z.cdf(12))
    print("Normalvertielt-größerGleich:", Z.sf(120))
    print("Normalvertielt-genau: immer 0  (wie bei jeder stetigen Zufallsvariable)")
    print("Normalvertielt-zwischen:", Z.cdf(15) - Z.cdf(11))


    Quant_Z95 = Z.ppf(0.95)
    print('Normalvertielt: Quant_Z95 = ' + myprint(Quant_Z95))

    Quant_Z90 = Z.ppf(0.90)
    print('Normalvertielt: Quant_Z90 = ' + myprint(Quant_Z90))#Wert über dem 10% der IQ-Werte liegen, also der Wert unter dem 90% der IQ-Werte liegen, also das 90%-Quantil.
    Quant_Z10 = Z.ppf(0.10)
    print('Normalvertielt: Quant_Z10 = ' + myprint(Quant_Z10))
    Quant_Z01 = Z.ppf(0.01)
    print('Normalvertielt: Quant_Z01 = ' + myprint(Quant_Z01))

    E_Z = Z.mean()
    print('Normalvertielt Erwartungswert: ' + myprint(E_Z))

    std_Z = Z.std()
    print('Normalvertielt Standartabweichung: ' + myprint(std_Z))

    print('Bonus: In welchen Bereich fallen 90% der Körpergrößen aller Männer?')
    print('[0.05-Quantil, 0.95-Quantil] = [' + myprint(Z.ppf(0.05)) + ', '
          + myprint(Z.ppf(0.95)) + ']')

    print(' ')

def myprint(x):
    x = str(np.round(x,3))
    return x

if __name__ == '__main__':
    stetigeVerteilung()


