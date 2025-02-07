from collections import Counter


class Mozg:
    def __init__(self):
     self.wynik = ""

    def porownaj_karty(self,reka):

        wartosci = [karta[1:] for karta in reka]
        kolory = [karta[0] for karta in reka]
        wartosci_konwersja = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11,
                           'Q': 12, 'K': 13, 'A': 14}

        wartosci_numeryczne = sorted([wartosci_konwersja[wartosc] for wartosc in wartosci])

        jakie_karty = Counter(wartosci_numeryczne)
        jakie_kolory = Counter(kolory)

        #poker krolewski - 5 kart od 10 do asa w tym samym kolorze
        if jakie_kolory.values() == 5 and wartosci_numeryczne == [10, 11, 12, 13, 14]:
            self.wynik = "Poker królewski"
            return 30
        #poker - 5 kart od 9 do 5 w tym samym kolorze
        elif jakie_kolory.values() == 5 and wartosci_numeryczne == [5, 6, 7, 8, 9]:
            self.wynik = "Poker"
            return 29
        #kareta - cztery karty o tej samej wartosci
        elif 4 in jakie_karty.values():
            self.wynik = "Kareta"
            return 28
        #full - trójka i dwójka
        elif 2 in jakie_karty.values() and 3 in jakie_karty.values():
            self.wynik = "Full"
            return 27
        #kolor - 5 kart w tym samym kolorze
        elif jakie_kolory.values() == 5:
            self.wynik = "Kolor"
            return 26
        #strit - 5 kart w różnych kolorach po kolei
        elif wartosci_numeryczne == list(range(wartosci_numeryczne[0], wartosci_numeryczne[0] + 5)):
            self.wynik = "Strit"
            return 25
        #trójka - 3 takie same karty
        elif 3 in jakie_karty.values():
            self.wynik = "Trójka"
            return 24
        #dwie pary -j.w
        elif list(jakie_karty.values()).count(2) == 2:
            self.wynik = "Dwie pary"
            return 23
        #para
        elif 2 in jakie_karty.values():
            self.wynik = "Para"
            return 22
        #wysoka karta
        else:
            self.wynik = "Najwyższa karta"
            return max(jakie_karty)