liczby = range(0, 51, 2)
for liczba in liczby:
    print(liczba)

napis = "Ala ma kota"
for litera in napis:
    print(litera)

lista_imion = ['Ola', 'Ala', 'Tomek', 'Jan']
for index, imie in enumerate(lista_imion):
    print('na pozycji {} jest imie {}'.format(index, imie))

lista_nazwisk = ['Kowalski', 'Malinowski', 'Iksinski', 'Igrekowski']
for imie, nazwisko in zip(lista_imion, lista_nazwisk):
    print(imie + ' ' + nazwisko)

import copy

lista = ['aaa', 'bbb', 'ccc', 'ddd']
przypisanie = lista

kopia_indexami = lista[:]
kopia_konstruktorem = list(lista)
kopia_metoda = lista.copy()
kopia_biblioteka = copy.copy(lista)

lista[0] = 'xxx'

print(lista)
print(przypisanie)
print(kopia_indexami)
print(kopia_konstruktorem)
print(kopia_metoda)
print(kopia_biblioteka)

lista2 = ['AAA', ['BBB', ['CCC', ['DDD']]]]

lista2_przypisanie = lista2
lista2_copy = copy.copy(lista2)
lista2_deepcopy = copy.deepcopy(lista2)

lista2_przypisanie[1][0] = 'YYY'

print(lista2)
print(lista2_przypisanie)
print(lista2_copy)
print(lista2_deepcopy)

napis = 'ala ma kota'


def wyswietl_napis(napis, koniec='.', poczek=''):
    do_wyswietlenia = str(poczek) + str(napis) + str(koniec)
    print(do_wyswietlenia)
    return do_wyswietlenia


# wyswietl_napis('Ala', '!')
# wyswietl_napis(napis)
# zmienna_na_koniec = '!'*20
# wyswietl_napis('Ala', zmienna_na_koniec )


wyswietl_napis(napis)


def policz_litery(litera, tekst):
    maly_tekst = tekst.lower()
    ile = maly_tekst.count(litera)
    print(ile)
    return ile

policz_litery('a', 'Ala ma kota')
