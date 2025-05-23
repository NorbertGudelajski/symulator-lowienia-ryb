
import random
from ryba import RYBY

class Gra:
    def __init__(self, root):
        self.root = root
        self.kolekcja = []

    def losuj_rybe(self):
        return random.choice(RYBY)

    def dodaj_do_kolekcji(self, ryba):
        self.kolekcja.append(str(ryba))

    def pokaz_kolekcje(self):
        return self.kolekcja

