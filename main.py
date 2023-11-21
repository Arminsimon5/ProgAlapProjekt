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
    a = input("Valasszon a lehetosegek kozul.\n\t\"Osszesadat\"\n\t\"Reszesedesszazalek\"\n\t\"Termelesertek\"\n\t\"termelesindex\"\n>")
    tovabb = True
    while tovabb:
        if a.lower() == "reszesedesszazalek" or a.lower() == "termelesertek" or a.lower() == "termeleseindex":
            for item in list:
                print("Ev "+item["ev"]+": "+item[a.lower()])
            tovabb = False
        elif a.lower() == "osszesadat":
            for item in list:
                print("Ev ",item["ev"],": ","\t| Reszesedes Szazalek: ",item["reszesedesszazalek"],"\t| Termeles ertek: ",item["termelesertek"],"\t| Termeles index: ",item["termelesindex"])
                tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Valasszon a lehetosegek kozul.\n\t\"Ev\"\n\t\"Reszesedesszazalek\"\n\t\"Termelesertek\"\n\t\"termelesindex\"\n>")

def termelesNovekedes():
    for item in range(1,len(list)):
        print("Ev",list[item]["ev"],":",(int(list[item]["termelesertek"])-int(list[item-1]["termelesertek"])))

def lekerdezesek():
    a = input("Lekredezesek\nMit szeretne: \n\t\"valtozasatlag\"\n\t...\n>").lower()
    tovabb = True
    while tovabb:
        if a == "valtozasatlag":
            valtozasAtlag()
            tovabb = False
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("Lekredezesek\nMit szeretne: \n\t\"valtozasatlag\"\n\t...\n>").lower()

def valtozasAtlag():
    osszesAdatErtek = 0
    osszesAdatSzazalek = 0
    elozo = int(list[0]["termelesertek"])
    for item in list:
        osszesAdatErtek+= int(item["termelesertek"])-elozo
        osszesAdatSzazalek+= (int(item["termelesertek"]) - elozo) / int(item["termelesertek"]) * 100
        elozo = int(item["termelesertek"])
    print(f"Atlagos eves valtozas: {round(osszesAdatErtek  / len(list),2)}FT | {round(osszesAdatSzazalek / len(list),2)}%")


def main():
    beolvasas(list)
    a = input("mit szeretne: \n\t\"adatbazis\"\n\t\"termelesnovekedes\"\n\t\"lekerdezesek\"\n\t...\n>").lower()
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
        else:
            print("Nem a megadott lehetosegek kozul van.")
            a = input("mit szeretne: \n\t\"adatbazis\"\n\t\"termelesnovekedes\"\n\t\"lekerdezesek\"\n\t...\n>").lower()


main()





