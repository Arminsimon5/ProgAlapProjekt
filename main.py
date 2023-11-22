# Kulon fajlban levo script beimportalasa
import graf
from graf import *
# lista letrehozasa "list" neven
list = []
#fajl beolvasasa
def beolvasas(lista):
    #fajl megnyitasa
    file = open("tablazat.csv", "r")
    #felesleges szovegek atugrasa
    file.readline()
    file.readline()
    #ciklus, amely dictionary-ben tarolja a sorokat, majd hozzaadja a listahoz
    for item in file:
        sor = item.strip().split(";")
        adat = {
            "ev": sor[0],
            "reszesedesszazalek": sor[1],
            "termelesertek": sor[2].replace(" ",""),
            "termelesindex": sor[3]
        }
        lista.append(adat)
    #fajl bezarasa
    file.close()


#Mentett adatok kiiratasa valaszthato lehetosegek kozul
def adatok():
    a = input("Adatbazis\n-------------------------------------------------\n\tO) A teljes allomany adatai rendszerezve\n\tR) A Az építõipar részesedése éves leosztásban\n\tE) Az építõipari termelés értéke éves leosztásban\n\tV) Az építõipari termelés volumenindexe\n\tv) Vissza\nValasszon opciot>")
    tovabb = True
    while tovabb:
        if a.lower() == "r":
            for item in list:
                print("Ev "+item["ev"]+": "+item["reszesedesszazalek"])
            tovabb = False
        elif a.lower() == "e":
            for item in list:
                print("Ev "+item["ev"]+": "+item["termelesertek"]+"FT")
            tovabb = False
        elif a.lower() == "v":
            for item in list:
                print("Ev " + item["ev"] + ": " + item["termelesindex"]+"%")
            tovabb = False
        elif a.lower() == "o":
            for item in list:
                print("Ev ",item["ev"],": ","\t| Reszesedes Szazalek: ",item["reszesedesszazalek"],"%\t| Termeles ertek: ",item["termelesertek"],"FT\t| Termeles index: ",item["termelesindex"])
            tovabb = False
        elif a == "v":
            tovabb = False
            main()
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input(
                "Adatbazis\n-------------------------------------------------\n\tO) A teljes allomany adatai rendszerezve\n\tR) A Az építõipar részesedése éves leosztásban\n\tE) Az építõipari termelés értéke éves leosztásban\n\tV) Az építõipari termelés volumenindexe\n\tv) Vissza\nValasszon opciot>")
    input("\nNyomj Enter-t a tovabblepeshez...")
    a = input("Szeretne visszalepni az adatokhoz (Igen):\n>").lower()
    if a == "igen":
        adatok()
#elozo evhez kepesti termeles novekedes vagy csokkenes
def termelesNovekedes():
    for item in range(1,len(list)):
        print("Ev",list[item]["ev"],":",(int(list[item]["termelesertek"])-int(list[item-1]["termelesertek"])),"FT")

#valaszthato lehetosegek
def lekerdezesek():
    a = input("Lekerdezesek\n-------------------------------------------------\n\tA) a termeles atlagos eves valtozasa\n\tT) Elozo evhez kepesti termeles novekedes vagy csokkenes\n\tMIN) Varhato maximum termeles a kovetkezo evben\n\tMAX) Varhato maximum termeles a kovetkezo evben\n\tv) Vissza\nValasszon opciot>").lower()
    tovabb = True
    while tovabb:
        if a == "a":
            valtozasAtlag()
            tovabb = False
        elif a == "t":
            termelesNovekedes()
            tovabb = False
        elif a == "max":
            varhatoMaxTermeles()
            tovabb = False
        elif a == "min":
            varhatoMinTermeles()
            tovabb = False
        elif a == "v":
            tovabb = False
            main()
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Lekerdezesek\n-------------------------------------------------\n\tA) a termeles atlagos eves valtozasa\n\tT) Elozo evhez kepesti termeles novekedes vagy csokkenes\n\tMIN) Varhato maximum termeles a kovetkezo evben\n\tMAX) Varhato maximum termeles a kovetkezo evben \n\tv) Vissza\nValasszon opciot>").lower()
        input("\nNyomj Enter-t a tovabblepeshez...")
        a = input("Szeretne visszalepni a lekerdezesekhez (Igen):\n>").lower()
        if a == "igen":
            lekerdezesek()

#Atlagos valtozas az osszes adat alapjan szazalekban es ertekben
def valtozasAtlag():
    osszesAdatErtek = 0
    osszesAdatSzazalek = 0
    elozo = int(list[0]["termelesertek"])
    for item in list:
        osszesAdatErtek+= int(item["termelesertek"])-elozo
        osszesAdatSzazalek+= (int(item["termelesertek"]) / elozo)
        elozo = int(item["termelesertek"])
    print(f"Atlagos eves valtozas: {round(osszesAdatErtek  / len(list),2)}FT | {round(osszesAdatSzazalek / len(list),2)}%")

#Varhato max termeles
def varhatoMaxTermeles():
    maxNovekedesSzazalek = 0
    elozo = int(list[0]["termelesertek"])
    for item in list:
        if maxNovekedesSzazalek < ((int(item["termelesertek"]) - elozo) / int(item["termelesertek"])):
            maxNovekedesSzazalek = ((int(item["termelesertek"]) - elozo) / int(item["termelesertek"]))
        elozo = int(item["termelesertek"])
    print(f"Az adatok alapjan a kovetkezo evi maximum termelesi ertek: {round(float(list[-1]['termelesertek']) + float(list[-1]['termelesertek']) * maxNovekedesSzazalek)}FT")


#Varhato min termeles
def varhatoMinTermeles():
    minNovekedesSzazalek = 1
    elozo = int(list[0]["termelesertek"])
    for item in list:
        if minNovekedesSzazalek > ((int(item["termelesertek"]) - elozo) / int(item["termelesertek"])):
            minNovekedesSzazalek = ((int(item["termelesertek"]) - elozo) / int(item["termelesertek"]))
        elozo = int(item["termelesertek"])
    print(f"Az adatok alapjan a kovetkezo evi minimum termelesi ertek: {round(float(list[-1]['termelesertek']) + float(list[-1]['termelesertek']) * minNovekedesSzazalek)}FT")

def grafikonok():
    a = input("Grafikonok\n-------------------------------------------------\n\tL) Line grafikon\n\tP) Plot diagram\n\tR) Linear Regression\n\tv) Vissza\nValasszon opciot>").lower()
    tovabb = True
    while tovabb:
        if a == "l":
            graf.lineGraph()
            tovabb = False
        elif a == "p":
            graf.plotDiagram()
            tovabb = False
        elif a == "r":
            graf.LinearRegression()
            tovabb = False
        elif a == "v":
            tovabb = False
            main()
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Grafikonok\n-------------------------------------------------\n\tL) Line grafikon\n\tP) Plot diagram\n\tR) Linear Regression\n\tv) Vissza\nValasszon opciot>").lower()
    input("\nNyomj Enter-t a tovabblepeshez...")
    a = input("Szeretne visszalepni a grafikonokhoz (Igen):\n>").lower()
    if a == "igen":
        grafikonok()

#A program fo futasi resze
def main():
    beolvasas(list)
    a = input("Az építőipar összefoglaló adatai\n-------------------------------------------------\n\tA) adatbazis adatainak megtekintese\n\tL) lekerdezesek az adatbazisbol\n\tG) grafikonok az adatbazisbol\nValasszon opciot>").lower()
    tovabb = True
    while tovabb:
        if a == "a":
            adatok()
            tovabb = False
        elif a == "l":
            lekerdezesek()
            tovabb = False
        elif a == "g":
            grafikonok()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Az építőipar összefoglaló adatai\n-------------------------------------------------\n\tA) adatbazis adatainak megtekintese\n\tL) lekerdezesek az adatbazisbol\n\tG) grafikonok az adatbazisbol\nValasszon opciot>").lower()
    input("\nNyomj Enter-t a tovabblepeshez...")
    a = input("Szeretne visszalepni a fooldalra (Igen):\n>").lower()
    if a == "igen":
        main()

main()

