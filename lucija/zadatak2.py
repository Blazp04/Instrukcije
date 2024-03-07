# Korištenjem while petlje i break izkaza od korisnika tražiti unos brojeva u niz sve dok ne unese “x” ili
# “X” . Unesene brojeve dinamički spremati u niz.
# Napisati funkciju koja kao argument prima niz i računa prosjek samo parnih brojeva.
# Funkcija kao rezultat vraća taj prosjek u glavni program.

# Wiile petllja
# traži unos brojeva
# ako korinnik unese x ili X onda prestani raditi
# inače spremi broj u niz

# funckija prima niz kao argument
# računamo veličinu niza
# računamo sumu niza
# suma / veličina = prosjek
# vrati prosjek

# pozovi funckiju i prosljedi parametar niza od gore

while True:
    broj = input("Unesi broj: ")
    if broj == "x":
        print("Izlaz")
        break
    print(broj)
