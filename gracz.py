import random

#komputerowy przeciwnik, zawierający swoją talię, metodę wymiany karty
class Gracz:
    def __init__(self, karty):
        self.reka = []
        for proba in range(0,5):
            self.reka.append(karty.pop(random.randint(0,len(karty)-1)))

    def wymien_karte(self, karty):
        "Komputer wymienia przypadkowe 2 karty."
        for odrzut in range(0,3):
            self.reka.pop(random.randint(0,4))
            self.reka.append(karty.pop(random.randint(0, len(karty)-1)))







