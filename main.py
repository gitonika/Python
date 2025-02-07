import random, gracz, mozg, os


def usuwanie_pliku():
    if os.path.exists("wyniki.txt"):
        os.remove("wyniki.txt")


talia = ['♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A','♠2', '♠3', '♠4', '♠5', '♠6',
         '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K', '♠A','♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J',
         '♦Q', '♦K', '♦A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K', '♣A']

ilosc_komputerow = 3
#gracz dostaje karty na reke
reka = []
for proba in range(0, 5):
    reka.append(talia.pop(random.randint(0, len(talia) - 1)))
print(f"Oto Twoje karty: {reka}")

usuwanie_pliku()

#tworze 3 graczy - komputery
gracz1 = gracz.Gracz(talia)
gracz2 = gracz.Gracz(talia)
gracz3 = gracz.Gracz(talia)
#gracz wymienia karty
karta1 = (input("Podaj kartę, którą chcesz wymienić (skopiuj kartę z talii). Jeżeli nie chcesz wymienić karty wpisz 'X': ")).upper()
if karta1 != 'X':
    reka.pop(reka.index(karta1))
    reka.append(talia.pop(random.randint(0, len(talia) - 1)))
karta2 = (input("Podaj drugą kartę, którą chcesz wymienić (skopiuj kartę z talii). Jeżeli nie chcesz wymienić karty wpisz 'X': ")).upper()
if karta2 != 'X':
    reka.pop(reka.index(karta2))
    reka.append(talia.pop(random.randint(0, len(talia) - 1)))
print(f"Oto Twoje nowe karty: {reka}")
#komputery wymieniaja karty
gracz1.wymien_karte(talia)
gracz2.wymien_karte(talia)
gracz3.wymien_karte(talia)

mozg = mozg.Mozg()
wynik_gracz = mozg.porownaj_karty(reka)
wynik1 = mozg.porownaj_karty(gracz1.reka)
uklad_gracz = mozg.wynik
uklad1 = mozg.wynik
wynik2 = mozg.porownaj_karty(gracz2.reka)
uklad2 = mozg.wynik
wynik3 = mozg.porownaj_karty(gracz3.reka)
uklad3 = mozg.wynik
wyniki = [wynik_gracz, wynik1, wynik2, wynik3]
print(f"Gracz pierwszy wykłada karty: {gracz1.reka}")
print(f"Gracz drugi wykłada karty: {gracz2.reka}")
print(f"Gracz trzeci wykłada karty: {gracz3.reka}")
if wyniki.count(max(wyniki)) > 1:
    print(f"Remis!")
    with open("wyniki.txt", "w", encoding="utf-8") as plik_wynikow:
        plik_wynikow.write(f"Remis.")
elif wyniki.index(max(wyniki)) == 0:
    print(f"Wygrywasz! Twój układ: {uklad_gracz}.")
    with open("wyniki.txt", "w", encoding="utf-8") as plik_wynikow:
        plik_wynikow.write(f"Wygrał użytkownik z wynikiem {uklad_gracz}.")
elif wyniki.index(max(wyniki)) == 1:
    print(f"Wygrywa gracz 1! Z układem {uklad1}")
    with open("wyniki.txt", "w", encoding="utf-8") as plik_wynikow:
        plik_wynikow.write(f"Wygrał gracz 1 z wynikiem {uklad1}.")
elif wyniki.index(max(wyniki)) == 2:
    print(f"Wygrywa gracz 2! Z układem {uklad2}.")
    with open("wyniki.txt", "w", encoding="utf-8") as plik_wynikow:
        plik_wynikow.write(f"Wygrał gracz 2 z wynikiem {uklad2}.")
elif wyniki.index(max(wyniki)) == 3:
    print(f"Wygrywa gracz 3! Z układem {uklad3}.")
    with open("wyniki.txt", "w", encoding="utf-8") as plik_wynikow:
        plik_wynikow.write(f"Wygrał gracz 3 z wynikiem {uklad3}.")

