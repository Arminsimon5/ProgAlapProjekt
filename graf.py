import csv
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