import graf
list = []
def beolvasas(lista):
    file = open("tablazat.csv", "r")
    file.readline()
    file.readline()
    for item in file:
        sor = item.strip().split(";")
        adat = {
            "ev": sor[0],
            "reszesedesszazalek": sor[1],
            "termelesertek": sor[2].replace(" ",""),
            "termelesindex": sor[3]
        }
        lista.append(adat)
    file.close()



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

def termelesNovekedes():
    for item in range(1,len(list)):
        print("Ev",list[item]["ev"],":",(int(list[item]["termelesertek"])-int(list[item-1]["termelesertek"])))

def lekerdezesek():
    a = input("Lekerdezesek\nMit szeretne: \n\t\"valtozasatlag\"\n\t...\n>").lower()
    tovabb = True
    while tovabb:
        if a == "valtozasatlag":
            valtozasAtlag()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Lekredezesek\nMit szeretne: \n\t\"valtozasatlag\"\n\t...\n>").lower()

def joslas():
    a = input("Joslas\nMit szeretne: \n\t\"varhatoMaxTermeles\"\n\t\"varhatoMinTermeles\"\n\t...\n>").lower()
    tovabb = True
    while tovabb:
        if a == "varhatomaxtermeles":
            varhatoMaxTermeles()
            tovabb = False
        elif a == "varhatomintermeles":
            varhatoMinTermeles()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Joslas\nMit szeretne: \n\t\"varhatoMaxTermeles\"\n\t\"varhatoMinTermeles\"\n\t...\n>").lower()
def valtozasAtlag():
    osszesAdatErtek = 0
    osszesAdatSzazalek = 0
    elozo = int(list[0]["termelesertek"])
    for item in list:
        osszesAdatErtek+= int(item["termelesertek"])-elozo
        osszesAdatSzazalek+= (int(item["termelesertek"]) - elozo) / int(item["termelesertek"]) * 100
        elozo = int(item["termelesertek"])
    print(f"Atlagos eves valtozas: {round(osszesAdatErtek  / len(list),2)}FT | {round(osszesAdatSzazalek / len(list),2)}%")

#Atgondolasra szorul
def varhatoMaxTermeles():
    maxNovekedesSzazalek = 0
    elozo = int(list[0]["termelesertek"])
    for item in list:
        szazalek = (int(item["termelesertek"]) - elozo) / int(item["termelesertek"])
        if maxNovekedesSzazalek < szazalek :
            maxNovekedesSzazalek = ((int(item["termelesertek"]) - elozo) / int(item["termelesertek"]))
            elozo = int(item["termelesertek"])
    print(f"Az adatok alapjan a kovetkezo evi maximum termelesi ertek: {round(float(list[-1]['termelesertek']) + float(list[-1]['termelesertek']) * maxNovekedesSzazalek)}FT")


#Javitasra szorul
def varhatoMinTermeles():
    minNovekedesSzazalek = 0
    elozo = int(list[0]["termelesertek"])
    for item in list:
        szazalek = (int(item["termelesertek"]) - elozo) / int(item["termelesertek"])
        if minNovekedesSzazalek > szazalek:
            minNovekedesSzazalek = ((int(item["termelesertek"]) - elozo) / int(item["termelesertek"]))
            elozo = int(item["termelesertek"])
    print(
        f"Az adatok alapjan a kovetkezo evi minimum termelesi ertek: {round(float(list[-1]['termelesertek']) + float(list[-1]['termelesertek']) * minNovekedesSzazalek)}FT")
def main():
    beolvasas(list)
    a = input("Programnev\nMit szeretne: \n\t\"adatbazis\"\n\t\"termelesnovekedes\"\n\t\"lekerdezesek\"\n\t\"joslas\"\n\t...\n>").lower()
    tovabb = True
    while tovabb:
        if a == "adatbazis":
            adatok()
            tovabb = False
        elif a == "termelesnovekedes":
            termelesNovekedes()
            tovabb = False
        elif a == "lekerdezesek":
            lekerdezesek()
            tovabb = False
        elif a == "linegraf":
            graf
            tovabb = False
        elif a == "plotdiagram":
            graf
            tovabb = False
        elif a == "joslas":
            joslas()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Programnev\nMit szeretne: \n\t\"adatbazis\"\n\t\"termelesnovekedes\"\n\t\"lekerdezesek\"\n\t...\n>").lower()
    input("\nNyomj Enter-t a tovabblepeshez...")
    a = input("Szeretne visszalepni a fooldalra (\"Igen\"):\n>").lower()
    if  a == "igen":
        main()


main()