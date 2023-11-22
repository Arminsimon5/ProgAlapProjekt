import csv

"""
print("hello")

print("Elso feladat:") #irasd ki az egesz listat     
lista = 'tablazat.csv.csv'
with open(lista, 'r') as egeszlista:
    olvasas = csv.reader(egeszlista)
    for kiiras in olvasas:
        print(kiiras)

print("-------------------------------------------------------------------")

print("Masodik feladat:") #irasd ki hogy hany evszam van 
utvonal = 'tablazat.csv.csv'
szamok = 0
with open(utvonal, 'r') as lista:
    #skippeles a listara
    next(lista)

    for valami in lista:
        szamok += 1

print(f"Evszamok darabja: {szamok} db")

print("-------------------------------------------------------------------")

print("Harmadik feladat:") #osszegezd a harmadik oszlopban levo milliokat
utvonal = 'tablazat.csv.csv'
osszesmillio = 0

with open(utvonal, 'r') as lista:
    next(lista)
    for valami in lista:
        oszlopok = valami.strip().split(';')
        try:
            szamok = int(oszlopok[2].replace(' ', '').replace(',', '.'))
            osszesmillio += szamok
        except (ValueError, IndexError):
            print(".")


print(f"Az osszes millio forintba: {osszesmillio} forint")

print("-------------------------------------------------------------------")

print("Negyedik feladat:") #H�ny ".." jel�l�s talalhato a tablazatban? (Ures cella)

utvonal = 'tablazat.csv.csv'
pontok = 0
with open(utvonal, 'r') as lista:
    for valami in lista:
        pontok += valami.count('..')

print(f"Ures cellak a listaban darabszamra: {pontok} db")

print("-------------------------------------------------------------------")

print("Otodik feladat:") # a negyedik oszlop �tlaga

utvonal = 'tablazat.csv.csv'
osszesszam = 0
szam2 = 0

with open(utvonal, 'r') as lista:

    next(lista)

 #lista feldarabolas es a negyedik oszlop kivalasztasa es viszgalata
    for valami in lista:
        oszlopok = lista.strip().split(';')
        try:
            erteke = float(oszlopok[3].replace(' ', '').replace(',', '.'))
            osszesszam += erteke
            szam2 += 1
        except (ValueError, IndexError):
            print(".")

#atlag szamitas
if szam2 > 0:
    atlagosszam= osszesszam / szam2
    print(f"A negyedik oszlop szamok atlaga: {atlagosszam} ")  
"""
print("-------------------------------------------------------------------")
# grafikonok:
import matplotlib.pyplot as plt  # konyvtarak meghivasa amik kellenek/kellhetnek
import pandas as pd
import numpy as np

ev = []  # listak letrehozasa a kulon oszlopok adatainak
epitoipar_reszesedese = []
epitoipari_termeles_erteke = []
epitoipari_termeles_volumenindexe = []
# reading a csv file and splitting it into 4 lists:
with open('tablazat.csv', newline='\n') as csvfile:
    csvfile.readline()
    csvfile.readline()
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        ev.append(int(row[0]))
        epitoipar_reszesedese.append(row[1])
        epitoipari_termeles_erteke.append(int(row[2].replace(" ","")))
        epitoipari_termeles_volumenindexe.append(row[3])
# making a line graph and plot diagram from the above:
# line graph:
plt.plot(ev, epitoipari_termeles_erteke)
plt.title('Az építőipari termelés értéke(millió forint), évenkenti változása:')
plt.xlabel('év')
plt.ylabel('termelés értéke')
plt.show()
# plot diagram:
plt.plot(ev, epitoipari_termeles_volumenindexe, 'ro')
plt.title('Az építőipari termelés volumenindexének(előző év = 100,0%) évenkénti változása')
plt.xlabel('év')
plt.ylabel('építőipari termelés volumenindexe')
plt.show()
# making a linear regression graph from 2 lists(above):
# calculating the slope and intercept of the linear regression line:
slope, intercept = np.polyfit(ev, epitoipari_termeles_erteke, 1)
# creating the scatter plot:
plt.scatter(ev, epitoipari_termeles_erteke)
# adding the linear regression line to the scatter plot:
plt.plot(ev, slope * np.array(ev) + intercept, color='red')
# adding titles:
plt.title('Lineáris regresszió évek és az építőipari termelés értéke viszonylatába:')
plt.xlabel('év')
plt.ylabel('építőipari termelés értéke')
# showing the plot:
plt.show()