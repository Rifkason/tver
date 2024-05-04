from pymongo import MongoClient as MC

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "Rh_tver"
# Testdata: vare, type, adresse

# Angi om båt er opptatt (True) eller ledig (False) og vektklasse
# vektklasse 1 er vare opptil 2-10kg, vektklasse 2 er vare opptil 10-50kg
bater = [[True, 2], [False, 1], [False, 2], [True, 1]]

varer = [['Sykkel',1,'Lovund'],['traktordel',2,'Tomma'],['Noetungt',2,'Nesna'],['Storvare1',2,'Lovund'],['Storpakke',1,'Nesna']]
#Angi om båt er opptatt (True) eller ledig (False) og vektklasse
# vektklasse 1 er vare opptil 2-10kg, vektklasse 2 er vare opptil 10-50kg
bater =[[True,2],[False,1],[False,2],[True,1]]
antallBater = len(bater)
def utføre_oppdrag():
    for vare in varer:
        for bat in bater: 
            if vare[1] == bat[1] and not bat[0]:
                bat[0] = True
                # printer ut for debug
                print(bater)
                print(f'båt på oppdrag til {vare[2]} med {vare[0]}')
                break



def get_collection(indata):
    cluster = MC(CONNECTION_STRING)
    database = cluster[DATABASE]
    collection = database[indata]
    return collection

def skjekk_kontorledig(indata="Kontor"):
    col = get_collection(indata)
    romnavn = "Trena"
    filter = {"Kontor": romnavn}
    rom = col.find_one(filter)
    return rom["ledig"]

def leie_bat():
    vekt = int(input("Skriv inn vekten av varen du skal levere: "))
    ledig_bat = finn_ledig_bat(vekt)
    if ledig_bat:
        print("Båt er tilgjengelig for levering!")
    else:
        print("Ingen båt tilgjengelig for denne vektklassen.")


def finn_ledig_bat(vekt):
    for bat in bater:
        if not bat[0] and vekt == bat[1]:
            bat[0] = True
            return True
    return False

def vis_Lagrer(inndata="Lagrer"):
    print("Lagrede varer og leveringsadresser:")
    for vare in Lagrer:
        print(f"Vare: {vare[0]}, Vekt: {vare[1]}, Adresse: {vare[2]}")
        get_collection().insert_one()

def menu_menubs():
    while True:
        print("Velkommen!")
        print("Velg et tall eller avslutt programmet!")
        print("1 For å legge til en leier.")
        print("3 For å leie en båt.")
        print("4 For å utføre en ordre.")
        print("5 For å vise lagrede varer og leveringsadresser.")

        valg = input("Velg et tall: ")

        if valg == "3":
            leie_bat()
        elif valg == "4":
            vare = input("Skriv inn varen du ønsker å levere: ")
            utføre_oppdrag(vare)
        elif valg == "5":
            vis_Lagrer()
        else:
            break

menu_menubs()