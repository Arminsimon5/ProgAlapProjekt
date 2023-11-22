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
    a = input("Adatbazis\nValasszon a lehetosegek kozul.\n\t\"Osszesadat\"\n\t\"Reszesedesszazalek\"\n\t\"Termelesertek\"\n\t\"termelesindex\"\n>")
    tovabb = True
    while tovabb:
        if a.lower() == "reszesedesszazalek" or a.lower() == "termelesertek" or a.lower() == "termelesindex":
            for item in list:
                print("Ev "+item["ev"]+": "+item[a.lower()])
            tovabb = False
        elif a.lower() == "osszesadat":
            for item in list:
                print("Ev ",item["ev"],": ","\t| Reszesedes Szazalek: ",item["reszesedesszazalek"],"\t| Termeles ertek: ",item["termelesertek"],"\t| Termeles index: ",item["termelesindex"])
                tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Adatbazis\nValasszon a lehetosegek kozul.\n\t\"Osszesadat\"\n\t\"Reszesedesszazalek\"\n\t\"Termelesertek\"\n\t\"termelesindex\"\n>")
            input("\nNyomj Enter-t a tovabblepeshez...")
            a = input("Szeretne visszalepni az adatokhoz (\"Igen\"):\n>").lower()
            if a == "igen":
                adatok()
#elozo evhez kepesti termeles novekedes vagy csokkenes
def termelesNovekedes():
    for item in range(1,len(list)):
        print("Ev",list[item]["ev"],":",(int(list[item]["termelesertek"])-int(list[item-1]["termelesertek"])))

#valaszthato lehetosegek
def lekerdezesek():
    a = input("Lekerdezesek\nMit szeretne: \n\t\"valtozasatlag\"\n\t\"termelesnovekedes\"\n\t\"varhatoMaxTermeles\"\n\t\"varhatoMinTermeles\"\n\t...\n>").lower()
    tovabb = True
    while tovabb:
        if a == "valtozasatlag":
            valtozasAtlag()
            tovabb = False
        elif a == "termelesnovekedes":
            termelesNovekedes()
            tovabb = False
        elif a == "varhatomaxtermeles":
            varhatoMaxTermeles()
            tovabb = False
        elif a == "varhatomintermeles":
            varhatoMinTermeles()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Lekredezesek\nMit szeretne: \n\t\"valtozasatlag\"\n\t\"termelesnovekedes\"\n\t\"varhatoMaxTermeles\"\n\t\"varhatoMinTermeles\"\n\t...\n>").lower()
        input("\nNyomj Enter-t a tovabblepeshez...")
        a = input("Szeretne visszalepni a lekerdezesekhez (\"Igen\"):\n>").lower()
        if a == "igen":
            lekerdezesek()

#Atlagos valtozas az osszes adat alapjan szazalekban es ertekben
def valtozasAtlag():
    osszesAdatErtek = 0
    osszesAdatSzazalek = 0
    elozo = int(list[0]["termelesertek"])
    for item in list:
        osszesAdatErtek+= int(item["termelesertek"])-elozo
        osszesAdatSzazalek+= (int(item["termelesertek"]) - elozo) / int(item["termelesertek"]) * 100
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
    a = input("Grafikonok\nMit szeretne: \n\t\"Line\"\n\t\"Plot\"\n\t\"Vlm\"\n\t...\n>").lower()
    tovabb = True
    while tovabb:
        if a == "line":
            graf.line()
            tovabb = False
        elif a == "plot":
            graf.plot()
            tovabb = False
        elif a == "vlm":
            graf.vlm()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Grafikonok\nMit szeretne: \n\t\"Line\"\n\t\"Plot\"\n\t\"Vlm\"\n\t...\n>").lower()
        input("\nNyomj Enter-t a tovabblepeshez...")
        a = input("Szeretne visszalepni a grafikonokhoz (\"Igen\"):\n>").lower()
        if a == "igen":
            grafikonok()

#A program fo futasi resze
def main():
    beolvasas(list)
    a = input("Programnev\nMit szeretne: \n\t\"adatbazis\"\n\t\"lekerdezesek\"\n\t\"grafikonok\"\n\t...\n>").lower()
    tovabb = True
    while tovabb:
        if a == "adatbazis":
            adatok()
            tovabb = False
        elif a == "lekerdezesek":
            lekerdezesek()
            tovabb = False
        elif a == "grafikonok":
            grafikonok()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Programnev\nMit szeretne: \n\t\"adatbazis\"\n\t\"lekerdezesek\"\n\t\"grafikonok\"\n\t...\n>").lower()
    input("\nNyomj Enter-t a tovabblepeshez...")
    a = input("Szeretne visszalepni a fooldalra (\"Igen\"):\n>").lower()
    if  a == "igen":
        main()

main()

