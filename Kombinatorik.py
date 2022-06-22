import math
from math import factorial as fact

'''
Script zum Thema Kombinatorik.
Ermittelt das richtige Zählverfahren.

Author: Timothy Hale
Version: 10.11.2021
'''


def kombination():
    print("Bitte mit \"ja\", \"nein\", \"mit\" oder \"ohne\" antworten.")
    red = '\033[31m'
    orange = '\033[33m'
    gesamt = int(input("Geben Sie ihre Gesamtmenge ein: "))
    x = input("Werden alle Elemente geordnet? ")

    if x == "ja":
        print(orange+"Permutation ohne Wiederholung")
        print(red + str(fact(gesamt)))
        return

    auswahl = int(input("Geben Sie die Anzahl ihrer Auswahl ein: "))
    x = input("Ist die Reihenfolge wichtig? ")

    if x == "ja":
        x = input("mit oder ohne Wiederholung? ")
        if x == "mit":
            print(orange+"Variation mit Wiederholung")
            print(red + str(math.pow(gesamt, auswahl)))
            return
        if x == "ohne":
            print(orange+"Variation ohne Wiederholung")
            print(red + str(fact(gesamt) / fact(gesamt - auswahl)))
            return
    x = input("mit oder ohne Wiederholung? ")
    if x == "mit":
        print(orange+"Kombination mit Wiederholung")
        print(red + str(fact(gesamt + auswahl - 1) / (fact(gesamt - 1) * fact(auswahl))))
        return
    if x == "ohne":
        print(orange+"Kombination ohne Wiederholung")
        print(red + str((fact(gesamt) / (fact(gesamt - auswahl) * fact(auswahl)))))
        return


if __name__ == "__main__":
    kombination()