from random import randint

# Argumenty ktore uzytkownik moze zmieniac
poczatkowa_liczba_procesow = 40  # Początkowa liczba procesow do wykonania
gorny_zakres = 9  # Górny zakres losowanego procesu
gorny_zakres_czasu_procesu = 15  # Górny zakres trwania procesu
maksymalny_czas_nadejscia_procesu = 80  # Maksymalny czas nadejscia procesu po rozpoczeciu dzialania programu
# Argumenty ktorych uzytkownik nie powinnien zmieniac
tablica_oczekiwania_pojedynczego_procesu = []
średni_czas_oczekiwania_na_wykonanie = 0
czas_pracy_procesora = 0.0
czas_pojedynczego_procesu = 0
wygenerowane_procesy = []
wygenerowane_czasy_procesora = []
czas_wygenerowanych_procesow = []


# Możliwość podania swoich danych do symulacji
czy_chcesz_podac_wlasne_dane = input("Możesz skorzystać z ustawionych danych. Czy chcesz podać własne dane? (y/n):")
if czy_chcesz_podac_wlasne_dane == 'y':
    poczatkowa_liczba_procesow = int(input("Podaj początkową liczbę procesów:"))
    gorny_zakres = int(input("Podaj górny zakres losowanych procesow(wiekszy od jedynki):"))
    gorny_zakres_czasu_procesow = int(input("Podaj gorny czas wykonywania losowanych procesow(wiekszy od zera):"))


def generator(ilosc_wykonan):  # Generator procesow oraz czasu wykonania danych procesow
    for ilosc_wykonan in range(ilosc_wykonan):
        wygenerowane_procesy.append(randint(1, gorny_zakres))
        wygenerowane_czasy_procesora.append(randint(1, gorny_zakres_czasu_procesu))
        tablica_oczekiwania_pojedynczego_procesu.append(0)


generator(poczatkowa_liczba_procesow)  # Wygenerowanie procesow oraz ich czasow dla poczatkowej liczby procesow

with open('LCFS_wyniki.txt', 'w') as plik:
    plik.write("Wygenerowane procesy:           "+str(wygenerowane_procesy)+"\n")
    plik.write("Wygenerowane czasy dla procesow:"+str(wygenerowane_czasy_procesora)+"\n\n")
    ilosc_wykonan_petli_while = 0
    pomocnicza = poczatkowa_liczba_procesow - 1

    while len(wygenerowane_procesy) > 0:
        czas_pracy_procesora += 1
        ilosc_wykonan_petli_while += 1

        # Generowanie dodatkowych procesow
        if ilosc_wykonan_petli_while < maksymalny_czas_nadejscia_procesu:
            liczba = randint(1, 8)
            if liczba == 8:  
                generator(1)

        ostatni_proces = len(wygenerowane_procesy) - 1
        if wygenerowane_czasy_procesora[ostatni_proces] > 1:
            wygenerowane_czasy_procesora[ostatni_proces] -= 1
            czas_pojedynczego_procesu += 1
        else:  # Wykonywanie ostatniej jednostki czasu dla wykonywanego procesu
            if len(wygenerowane_procesy) > 1:  # Doliczenie czasu procesora z powodu zmiany procesu
                czas_zmiany_procesu = abs(wygenerowane_procesy[ostatni_proces] - wygenerowane_procesy[ostatni_proces-1])
            czas_pracy_procesora += 0.1 * czas_zmiany_procesu
            wygenerowane_procesy.pop(ostatni_proces)
            wygenerowane_czasy_procesora.pop(ostatni_proces)
            średni_czas_oczekiwania_na_wykonanie += tablica_oczekiwania_pojedynczego_procesu[ostatni_proces]
            tablica_oczekiwania_pojedynczego_procesu.pop(ostatni_proces)
            czas_pojedynczego_procesu = 0
            pomocnicza -= 1

        for x in range(0, pomocnicza):
            tablica_oczekiwania_pojedynczego_procesu[x] += 1

    średni_czas_oczekiwania_na_wykonanie = średni_czas_oczekiwania_na_wykonanie / poczatkowa_liczba_procesow
    plik.write("\nCzas wykonania wszystkich zadan: " + str(round(czas_pracy_procesora, 1)) + "[s]")
    plik.write("\nSredni czas oczekiwania zadania: " + str(round(średni_czas_oczekiwania_na_wykonanie, 1)) + "[s]")