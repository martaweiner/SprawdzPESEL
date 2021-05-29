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

x = 10
if tab_pesel[9] % 2==0:
    print("Osoba z PESELem ", pesel, " jest kobieta")
else:
    print("Osoba z PESELem ", pesel, "jest mezczyzna")

rok = tab_pesel[0:2]
miesiac = tab_pesel[2:4]
dzien = tab_pesel[4:6]

r = (''.join([str(i) for i in rok]))
msc = (''.join([str(i) for i in miesiac]))
d = (''.join([str(i) for i in dzien]))

if msc == "01":
    m = "styczeń"
elif msc == "02":
    m = "luty"
elif msc == "03":
    m = "marzec"
elif msc == "04":
    m = "kwiecień"
elif msc == "05":
    m = "maj"
elif msc == "06":
    m = "czerwiec"
elif msc == "07":
    m = "lipiec"
elif msc == "08":
    m = "sierpien"
elif msc == "09":
    m = "wrzesien"
elif msc == "10":
    m = "pazdziernik"
elif msc == "11":
    m = "listopad"
elif msc == "12":
    m = "grudzien"


print("Ta osoba urodziła się", d, "dnia, ", "miesiaca ", m, " ,", r, "roku")