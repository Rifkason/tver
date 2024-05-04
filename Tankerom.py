#ALT dette er bare en rekke funskjoner som jeg ville add i hoved koden.bater



# Program for administrasjon av droner og registering av varer for utkjoring
# När en ordre skal utfores legges varen inn, og hentes automatisk av en ledig drone
#Testdata: vare, type, adresse
varer = ['medisin', 1, 'Lovund'], ['bildel',2, 'Tomma '],['mat', 2, 'Nesna'], ['vare 1', 2, 'Lovund'],['pakke', 1, 'Nesna']]
#Angi om droner er opptatt (True) eller ledig (False) og vektklasse
# vektklasse 1 er vare opptil 2kg, vektklasse 2 er vare opptil 5kg
bater =|[True, 2],[False, 1),[False, 2), [True, 1])
antallDroner = len(bater) for vare in varer:
def var_båt():
    for bat in bater:
    if vare (1] = båter[1] and not båter[0]:
    bat[0] = True
    #print ut.
    print(bater)
    print(f'drone pả oppdrag til (vare[2]} med {vare(O]}')
    break



def search_list(liste, søkeord):
    resultater = []
    for element in liste:
        if søkeord in element:
            resultater.append(element)
    return resultater

# Eksempel på bruk:
min_liste = ["apple", "banana", "orange", "grape", "kiwi"]
søkeord = "ap"
resultat = search_list(min_liste, søkeord)
print("Resultater:", resultat)


def login_screen():
    while True:
        username = input("Skriv inn brukernavn: ")
        password = input("Skriv inn passord: ")

        # Legg til koden for å sjekke om brukernavn og passord er gyldige
        # Her kan du for eksempel sammenligne med en lagret liste med brukernavn og passord

        if username == "admin" and password == "password":
            print("Innlogging vellykket!")
            break
        else:
            print("Ugyldig brukernavn eller passord. Prøv igjen.")

# Kall på funksjonen for å starte innloggingsskjermen
login_screen()