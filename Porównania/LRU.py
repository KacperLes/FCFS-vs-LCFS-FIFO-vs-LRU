from random import randint

# Argumenty ktore uzytkownik moze zmieniac
ilosc_wykonan = 20  # ilosc wykonan stron
gorny_zakres = 10  # Górny zakres losowanych stron
ilosc_ramek = 5  # Ilość ramek do których sa umieszczane dane
# Argumenty ktorych uzytkownik nie powinnien zmieniac
wygenerowane_liczby = []  # Ciąg wygenerowanych liczb
wiek_tablicy = []  # Stosowany do sledzenie wieku poszczegolnych stron w ramkach
rzad_w_wiek_tablicy = 0  # Stosowany do znajdowania najstarszego wieku w tablicy
tablica_ramek = []  # Tablica zawierająca wszystkie ramki
opoznienie = 0  # Stosowane do zapelniania tablicy
ilosc_bledow = 0  # Ilosc zdarzen gdy trzeba zmienic liczbe w ramkach
ilosc_dopasowan = 0  # Zdarzenie przeciwne do bledu
rzad = []  # Rzad na którym dzialamy

# Możliwość podania swoich danych do symulacji
czy_chcesz_podac_wlasne_dane = input("Możesz skorzystać z ustawionych danych. Czy chcesz podać własne dane? (y/n):")
if czy_chcesz_podac_wlasne_dane == 'y':
    ilosc_wykonan = int(input("Podaj ilość wykonań:"))
    ilosc_ramek = int(input("Podaj ilość ramek:"))
    gorny_zakres = int(input("Podaj górny zakres(wiekszy od jedynki):"))

# Losowanie stron
for ilosc_wykonan in range(ilosc_wykonan):
    wygenerowane_liczby.append(randint(1, gorny_zakres))

# Ustawianie wiek_tablicy by dzialala
for i in range(0, ilosc_ramek):
    wiek_tablicy.append(0)

# Zapisywanie do pliku
with open('LRU_wyniki.txt', 'w') as plik:
    plik.write("Wygenerowany ciag liczb " + str(wygenerowane_liczby) + "\n\n")

    # Działania na tablicy ramek
    for y in range(ilosc_wykonan):
        value = wygenerowane_liczby[y]
        if y == 0:  # Zapisywanie pierwszej wartosci
            rzad.append(value)
            ilosc_bledow += 1
            for x in range(1, ilosc_ramek):
                rzad.append(0)
        else:
            if value in tablica_ramek[y - 1]:  # Sprawdzanie czy podane wartosci juz istnieją: jesli tak to rzad jest kopiowany
                rzad = tablica_ramek[y-1].copy()
                ilosc_dopasowan += 1
                opoznienie += 1
                for x in range(0, ilosc_ramek):
                    if value == tablica_ramek[y-1][x]:
                        wiek_tablicy[x] = 0
            elif y < ilosc_ramek + opoznienie:  # Jeśli nie - oraz wszystkie ramki nie maja swoich wartosci -  to rzad jest zapisywany kolejna wartosci
                for x in range(0, y - opoznienie):
                    rzad.append(tablica_ramek[y - 1][x])
                rzad.append(value)
                ilosc_bledow += 1
                for x in range(y, ilosc_ramek - 1 + opoznienie):
                    rzad.append(0)
            else:
                najdluzszy_wiek = max(wiek_tablicy)  # Sprawdzanie wieku kazdej liczby w tablicy
                for x in range(0, ilosc_ramek):
                    if najdluzszy_wiek == wiek_tablicy[x]:  # Wyszukiwanie najdluzszego oraz resetowanie go
                        rzad_w_wiek_tablicy = x
                        wiek_tablicy[x] = 0

                for x in range(0, rzad_w_wiek_tablicy):  # Najdluzszy wyszukany wiek jest zastepowany przez nowa liczbe
                    rzad.append(tablica_ramek[y - 1][x])
                rzad.append(value)
                ilosc_bledow += 1
                for x in range(rzad_w_wiek_tablicy, ilosc_ramek - 1):
                    rzad.append(tablica_ramek[y - 1][x + 1])

        for x in range(0, min(y + 1 - opoznienie, ilosc_ramek)):  # Dodawanie wieku do tablicy
            wiek_tablicy[x] += 1

        tablica_ramek.append(rzad.copy())  # Tworzenie calej pamieci ramek
        plik.write("Podana liczba "+str(value)+"\n")
        plik.write("Aktualny przegladane ramki       "+str(rzad)+"\n")
        plik.write("Aktualny wiek przegladanej ramki " + str(wiek_tablicy) + "\n\n")
        rzad.clear()  # Czyszczenie aktulnych ramek
    plik.write("\n"+str(ilosc_bledow)+" bledow\n")
    plik.write(str(ilosc_dopasowan)+" dopasowan\n")
    plik.write("Cala historia tablicy ramek " + str(tablica_ramek) + "\n")