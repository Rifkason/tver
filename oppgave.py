from pymongo import MongoClient as MC

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
COLLECTION = "Lagrer"
DATABASE = "Rh_tver"
# MongoDB-tilkoblingsstreng og navn på samlingen og databasen
# Funksjon for å få tak i en spesifikk samling i MongoDB
bater = [[True, 2], [False, 1], [False, 2], [True, 1]]

varer = [['Sykkel',1,'Lovund'],['traktordel',2,'Tomma'],['Noetungt',2,'Nesna'],['Storvare1',2,'Lovund'],['Storpakke',1,'Nesna']]

def get_collection(col):
    cluster = MC(CONNECTION_STRING).
    database = cluster[DATABASE]
    collection = database[col]
    return collection
# Funksjon for å skrive ut alle dokumentene i en angitt samling


#henter ut all data som ligger i en mappe i mongodv.
#in data er navn på mappen jeg ønsker og hente.
def print_mappe(inndata="Lagrer"):
    col = get_collection(inndata).find()
    listeOfdata = []
    for c in col:
        listeOfdata.append(c)
    return listeOfdata
# Funksjon for å legge til et nytt dokument i en angitt samling




def print_båt(inndata="Båt_locak"):
    col = get_collection(inndata).find()
    listeOfdata = []
    for c in col:
        listeOfdata.append(c)
    return listeOfdata
#"print_mappe" denne funksjonen skriver ut data om båt.
#den bruker "indata" for å hente informasjon fra MongoDB-samlinger.



def lagre_objekt(indata="Lagrer"):
    fornavn = input("Legg til vare navn: ")
    etternavn = input("legg til vekt klasse: ")
    nyelev = {"fornavn": fornavn, "etternavn": etternavn}
    get_collection(indata).insert_one(nyelev)
#"lagre_objekt" denne funksjonen ber våre brukere om å legge inn informasjon som "Vare og Vekt klasse."
#den lagrer denne informasjonen/dataene i MongoDB-databasen.



def slett_objekt(indata="Lagrer"):
    col = get_collection(indata)
    fornavn = input("skriv in navnet på varen du ønsker og slette: ")
    etternavn = input("skriv in vekt klassen på varen du ønsker og slette: ")
    col.delete_one({"fornavn": fornavn, "etternavn": etternavn})

    print(f"vi har sletten varen med vekt klasse: {fornavn} {etternavn}")
# "slett_objekt" denne funksjonen lar brukeren slette leiers informasjon ved å oppgi navnet. 





# Her skriver man inn hvilken vare du vill redigere med navn og vekt, og da vil den send et signal til databasen slikt at varen blir kastet ut/slettet fra Lagret.
def rediger_objekt(indata="Lagrer"):
    col = get_collection(indata)
    fornavn = input("skriv in navnet på varen du ønsker og redigere: ")
    etternavn = input("skriv in vekt klassen på personen du ønsker og redigere: ")
    nyttfornavn = input("skriv in nytt varenavn: ")
    nyttetternavn = input("skriv in nytt vektklassen: ")
    filter = {"fornavn": fornavn, "etternavn": etternavn}
    updatering = {'$set': {'fornavn': nyttfornavn, 'etternavn': nyttetternavn}}
    col.update_one(filter, updatering)

# Planen her er at man skal kunne søke opp båten du trenger, vis båten er ledig så skal man kunne lei den og da leie båten (bli send til videre kode)
# framtids plan: dette er her man kan leie båt for vare, tanken er å få det slikt at man kan søk om båt og sette opp på Klokke slet.
#istede får å ta båten hele tiden.
#slikt at det holder seg rolig og at man ungår kras mellom personene.
def utføre_oppdrag():
    for vare in varer:
        for bat in bater: 
            if vare[1] == bat[1] and not bat[0]:
                bat[0] = True
                # printer ut for debug
                print(bater)
                print(f'båt på oppdrag til {vare[2]} med {vare[0]}')
                break


def vis_ordre():
    for vare in varer:
        for bat in bater:
            if vare[1] == bat[1] and not bat[0]:
                bat[0] = True
                print(f'Båt på oppdrag til {vare[2]} med {vare[0]}')
                break

#"menu_menu" denne hovedmenyen gir brukerne en rekke alternativer, som å legge til, leie eller frigi.
#se på båt eller avslutt programmet.
def menu_menu():
    while True:
        print("Velkommen!")
        print("1. får og legge til vare: ")
        print("2. får og slette vare: ")
        print("3. får og skrive ut alle varer: ")
        print("4. får og liste ut båter: ")
        print("5. får og rediger vare status: ")
        print("6. for oppdrag:")
        print("7. for å se båter på oppdrag: ")
        valg = input("velg et nummer fra listen over: ")
        if valg == "1":
            lagre_objekt()
        
        elif valg == "2":
            slett_objekt()

        elif valg == "3":
            liste = print_mappe()
            print(liste)

        elif valg == "4":
            liste = print_båt()
            print(liste)

        elif valg == "5":
            rediger_objekt()

        elif valg == "6":
            vare = input("Skriv inn varen du ønsker å levere: ")
            utføre_oppdrag(vare)

        elif valg == "7":
            vis_ordre()
        else:
            break

menu_menu()