szerokosc = 10
wysokosc = 20

top_bottom =('+'+ ('-' * szerokosc) +'+')
print(top_bottom +('|'+ (' ' * szerokosc) +'|\n') * wysokosc + top_bottom, end='')

