pesel = input('Podaj pesel: ')
if len(pesel) == 11:
    tab_pesel = list(map(int, ' '.join(str(pesel)).split()))

# wartosc pobrana z wikipedii
# c1·1 + c2·3 + c3·7 + c4·9 + c5·1 + c6·3 + c7·7 + c8·9 + c9·1 + c10·3 + c11·1
tab_kontrolna = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

wynik = []
for i in range(len(tab_pesel)):
    wynik.append(tab_pesel[i] * tab_kontrolna[i])
suma = sum(wynik)

tab_suma = list(map(int, ' '.join(str(suma)).split()))
if tab_suma[2] == 0:
    print("POPRAWNY")
else:
    print("NIEPOPRAWNY")

