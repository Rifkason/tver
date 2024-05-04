from pymongo import MongoClient as MC

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "Rh_tver"
# Testdata: vare, type, adresse

# Angi om båt er opptatt (True) eller ledig (False) og vektklasse
# vektklasse 1 er vare opptil 2-10kg, vektklasse 2 er vare opptil 10-50kg
bater = [[True, 2], [False, 1], [False, 2], [True, 1]]

def get_collection(indata):
    cluster = MC(CONNECTION_STRING)
    database = cluster[DATABASE]
    collection = database[indata]
    return collection

def lagre_objekt():
    Navn = input("Skriv in navn:")
    Telefonnummer = input("skriv Tlf:")
    Epost = input("Skriv in E-post:")
    nyeleier = {"Navn": Navn, "Telefonnummer": Telefonnummer, "Epost": Epost}
    get_collection(indata="Leiere").insert_one(nyeleier)

def skjekk_kontorledig(indata="Kontor"):
    col = get_collection(indata)
    romnavn = "Trena"
    filter = {"Kontor": romnavn}
    rom = col.find_one(filter)
    return rom["ledig"]

def kontor_ledig(indata="Kontor"):
    romnavn = input("Skriv inn rommet du ønsker å leie: ")
    ledig = skjekk_kontorledig()
    if ledig:
        print("Rommet er ledig!")
        ønske = input("Ønsker du å leie rommet? (ja/nei): ")
        if ønske.lower() == "ja":
            col = get_collection(indata)
            navn = input("Ditt navn?: ")
            datofra = input("Dato fra?: ")
            datotil = input("Dato til?: ")

            filter = {"Kontor": romnavn}
            updatering = {'$set': {'Kontor': romnavn, 'ledig': False}}
            col.update_one(filter, updatering)
    else:
        print("Rommet er ikke ledig..")

def finn_ledig_bat(vekt):
    for bat in bater:
        if not bat[0] and vekt == bat[1]:
            bat[0] = True
            return True
    return False

def utfør_ordre(vare):
    for vare in varer:
        for bat in bater:
            if vare[1] == bat[1] and not bat[0]:
                bat[0] = True
                print(f'Båt på oppdrag til {vare[2]} med {vare[0]}')
                break

def menu_menubs():
    while True:
        print("Velkommen!")
        print("Velg et tall eller avslutt programmet!")
        print("1 For å legge til en leier.")
        print("2 For å leie et rom.")
        print("3 For å utføre en ordre.")

        valg = input("Velg et tall: ")

        if valg == "1":
            lagre_objekt()
        elif valg == "2":
            kontor_ledig()
        elif valg == "3":
            vare = input("Skriv inn varen du ønsker å levere: ")
            vekt = int(input("Skriv inn vekten av varen: "))
            adresse = input("Skriv inn leveringsadressen: ")
            varer.append([vare, vekt, adresse])
            utfør_ordre(vare)
        else:
            break

menu_menubs()
