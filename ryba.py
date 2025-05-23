
import random

class Ryba:
    def __init__(self, nazwa, waga_zakres, dlugosc_zakres):
        self.nazwa = nazwa
        self.waga = round(random.uniform(*waga_zakres), 2)
        self.dlugosc = round(random.uniform(*dlugosc_zakres), 2)

    def __str__(self):
        return f"{self.nazwa} - Waga: {self.waga} kg, Długość: {self.dlugosc} m"

RYBY = [
    Ryba("Karas", (0.5, 1.5), (0.2, 0.4)),
    Ryba("Szczupak", (2, 15), (0.5, 1.2)),
    Ryba("Sum", (10, 50), (1.0, 2.5)),
    Ryba("Sandacz", (1.5, 7), (0.5, 1.0)),
    Ryba("Leszcz", (1.0, 5), (0.3, 0.6)),
    Ryba("Płoć", (0.2, 1.2), (0.3, 0.5)),
    Ryba("Pstrąg", (0.5, 5), (0.4, 1.0)),
    Ryba("Okoń", (0.2, 1), (0.2, 0.5)),
    Ryba("Węgorz", (0.2, 2.0), (0.4, 1.0)),
]

