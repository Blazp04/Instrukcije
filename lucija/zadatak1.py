# Definiraj funkciju koja kao parametar prima 2 broja te vraća niz brojeva djeljivih s 3 između njih.

# Zatražiti od korisnike unos intervala i ispisati duljinu te aritmetičku sredinu niza koji smo dobili pozivom
# ranije definirane funkcije.


def djeljivisSa3(broj1, broj2):
    niz = []
    for i in range(broj1, broj2+1):
        if i % 3 == 0:
            niz.append(i)
    return niz


a = int(input("Unesi neki broj: "))
b = int(input("Unesi drugi broj: "))


rez = djeljivisSa3(a, b)
duljina = len(rez)
suma = sum(rez)
sredina = suma/duljina

print("Aritmetička sredina je: ", sredina)
