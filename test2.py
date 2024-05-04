from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "Rh_tver"
# MongoDB-tilkoblingsstreng og navn på databasen

def get_collection(collection_name):
    client = MongoClient(CONNECTION_STRING)
    db = client[DATABASE]
    return db[collection_name]

def print_items(collection_name):
    collection = get_collection(collection_name)
    items = collection.find()
    for item in items:
        print(item)

def add_item(collection_name):
    fornavn = input("Legg til varenavn: ")
    etternavn = input("Legg til vekt: ")
    item = {"fornavn": fornavn, "etternavn": etternavn}
    get_collection(collection_name).insert_one(item)

def slett_objekt(indata="Lagrer"):
    col = get_collection(indata)
    fornavn = input("skriv in navnet på varen du ønsker og slette: ")
    etternavn = input("skriv in vekt klassen på varen du ønsker og slette: ")
    col.delete_one({"fornavn": fornavn, "etternavn": etternavn})

    print(f"vi har sletten varen med vekt klasse: {fornavn} {etternavn}")

def update_item(Indata="Lagrer"):
    col = get_collection(Indata)
    fornavn = input("Skriv inn navnet på varen du vil oppdatere: ")
    etternavn = input("Skriv inn vekten på varen du vil oppdatere: ")
    nytt_fornavn = input("Skriv inn det nye varenavnet: ")
    nytt_etternavn = input("Skriv inn den nye vekten: ")
    filter = {"fornavn": fornavn, "etternavn": etternavn}
    updatering = {'$set': {'nyttfornavn': nytt_fornavn, 'nytt_etternavn': nytt_etternavn}}
    col.update_one(filter, updatering)


def main_menu():
    while True:
        print("Velkommen!")
        print("1. Legg til vare.")
        print("2. Slett vare.")
        print("3. Skriv ut alle varer.")
        print("4. Oppdater vare.")
        print("5. Avslutt.")
        choice = input("Velg et alternativ fra listen: ")

        if choice == "1":
            add_item("Items")
        elif choice == "2":
            slett_objekt("Items")
        elif choice == "3":
            print_items("Items")
        elif choice == "4":
            update_item("Items")

        elif choice == "5":
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    main_menu()