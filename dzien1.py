name = input('podaj name:')
name.upper()
print('elo ' + name)
dlugosc_imienia = len(name)
print('dlugosc imienia to ' + str(dlugosc_imienia))
ostatnia_litera_imienia = name[-1]


if ostatnia_litera_imienia == 'a':
    print("hej laska")
else:
    print("hej ziomek")


