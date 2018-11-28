slownik = {'imie': [
    'Lukasz', 'Ala', 'Ola'
],
    'nazwiska': [
        'Falkowicz', 'Kowalska', 'Malinowska'
    ]
}

miasta = {'miasta': ['Warszawa', 'Gdansk', 'Sopot', 'Krakow']}

print(type(slownik))
print(slownik)

print(slownik.values())
print(slownik.items())

for klucz, wartosc in slownik.items():
    print('#' + klucz)
    for elem in wartosc:
        print('\t ->' + elem)

nazwiska = slownik["nazwiska"]
for elem in nazwiska:
    print('\t ->' + elem)


def wyswietl_slownik(slownik, miasta):
    for index, imie in enumerate(slownik['imie']):
        nazwiska = slownik['nazwiska'][index]
        miasto = miasta['miasta'][index]
        print('Mam na imie {} nazwisko {} i mieszkam w {}'.format(imie, nazwiska, miasto))


wyswietl_slownik(slownik, miasta)
