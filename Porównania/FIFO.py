from random import randint

# Argumenty ktore uzytkownik moze zmieniac
ilosc_wykonan = 20  # ilosc wykonan stron
gorny_zakres = 10  # Górny zakres losowanych stron
ilosc_ramek = 5  # Ilość ramek do których sa umieszczane dane
# Argumenty ktorych uzytkownik nie powinnien zmieniac
wygenerowane_liczby = []  # Ciąg wygenerowanych liczb
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

# Losowanie stron z zakresu
for ilosc_wykonan in range(ilosc_wykonan):
    wygenerowane_liczby.append(randint(1, gorny_zakres))

# Zapisywanie do pliku
with open('FIFO_wyniki.txt', 'w') as plik:
    plik.write("Wygenerowany ciag liczb "+str(wygenerowane_liczby)+"\n\n")

    # Działania na tablicy ramek
    for y in range(ilosc_wykonan+1):
        value = wygenerowane_liczby[y]
        if y == 0:  # Zapisywanie pierwszej wartosci
            rzad.append(value)
            ilosc_bledow += 1
            for x in range(1, ilosc_ramek):
                rzad.append(0)
        else:
            if value in tablica_ramek[y - 1]:  # Sprawdzanie czy podane wartosci juz istnieją: jesli tak to rzad jest kopiowany
                rzad = tablica_ramek[y - 1].copy()
                opoznienie += 1
                ilosc_dopasowan += 1
            else:  # Jeśli nie to rzad jest zapisywany kolejna wartosci
                ilosc_bledow += 1
                for x in range(0, ilosc_ramek):
                    if x == (y - opoznienie) % ilosc_ramek:
                        rzad.append(value)
                    elif tablica_ramek[y - 1][x] != 0:
                        rzad.append(tablica_ramek[y - 1][x])
                    else:
                        rzad.append(0)

        tablica_ramek.append(rzad.copy())  # Tworzenie calej pamieci ramek
        plik.write("Podana liczba "+str(value)+"\n")
        plik.write("Aktualny przegladane ramki "+str(rzad)+"\n")
        rzad.clear()  # Czyszczenie aktulnych ramek
    plik.write("\n"+str(ilosc_bledow)+" bledow\n")
    plik.write(str(ilosc_dopasowan)+" dopasowan\n")
    plik.write("Cala historia tablicy ramek " + str(tablica_ramek) + "\n")
