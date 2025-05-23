import tkinter as tk
import random
import time
from PIL import Image, ImageTk
import os  # Import os do sprawdzenia, czy plik istnieje

# Inicjalizacja okna głównego
root = tk.Tk()
root.title("Symulator Łowienia Ryb")

# Zmienna globalna do przechowywania labela obrazu
obraz_label = None  # Inicjalizujemy obraz_label na początku, aby uniknąć błędu
tlo_label = None  # Globalna zmienna do przechowywania tła

# Ustawienie tła - jezioro
def ustaw_tlo():
    global tlo_label  # Używamy zmiennej globalnej tlo_label
    try:
        # Wczytanie obrazu tła (np. jezioro)
        tlo_obraz = Image.open("jezioro.png")  # Zmień na nazwę swojego pliku z tłem
        tlo_obraz = tlo_obraz.resize((800, 600))  # Dopasuj rozmiar tła do okna
        tlo_obraz_tk = ImageTk.PhotoImage(tlo_obraz)
        
        # Ustawienie tła w oknie
        if tlo_label is None:  # Jeśli tło nie zostało ustawione wcześniej
            tlo_label = tk.Label(root, image=tlo_obraz_tk)
            tlo_label.place(x=0, y=0)  # Ustawienie w lewym górnym rogu
            tlo_label.image = tlo_obraz_tk  # Musimy zachować referencję, aby obrazek się nie zgubił
        print("Tło załadowane poprawnie!")  # Komunikat debugowy
    except Exception as e:
        print(f"Problem z wczytaniem tła: {e}")  # Komunikat o błędzie, jeśli nie uda się wczytać tła

# Funkcja łowienia ryb
def low_rybe():
    global obraz_label, aktualne_zdjecie

    wynik_label.config(text="Zarzucasz wędkę...")
    root.update()
    time.sleep(2)

    # Losowanie ryby
    zlowiona_ryba = random.choice(ryby)
    kolekcja.append(zlowiona_ryba)
    
    # Wyświetlenie informacji o złowionej rybie
    wynik_label.config(text=f"Złowiłeś: {zlowiona_ryba}!")
    
    # Wczytanie obrazu ryby
    nazwa_pliku = zlowiona_ryba + ".png"
    
    print(f"Sprawdzam plik: {nazwa_pliku}")  # Debugowanie: sprawdzamy, jaką nazwę pliku generujemy
    
    if not os.path.exists(nazwa_pliku):  # Sprawdzenie, czy plik istnieje
        wynik_label.config(text=f"Nie znaleziono pliku: {nazwa_pliku}")
        return

    try:
        obraz = Image.open(nazwa_pliku)
        obraz = obraz.resize((300, 200))  # Dopasowanie rozmiaru obrazu
        aktualne_zdjecie = ImageTk.PhotoImage(obraz)
        
        if obraz_label:  # Jeśli obraz_label już istnieje, zaktualizuj go
            obraz_label.config(image=aktualne_zdjecie)
        else:  # Jeśli obraz_label nie istnieje, stwórz nowy
            obraz_label = tk.Label(root, image=aktualne_zdjecie)
            obraz_label.pack(pady=10)
            
    except Exception as e:
        wynik_label.config(text=f"Problem z wczytaniem obrazu: {e}")
        print(f"Error: {e}")

# Funkcja pokazująca kolekcję ryb
def pokaz_kolekcje():
    kolekcja_window = tk.Toplevel(root)  # Nowe okno
    kolekcja_window.title("Twoja Kolekcja Ryb")
    
    kolekcja_text = "\n".join(kolekcja) if kolekcja else "Nie złowiłeś jeszcze żadnej ryby."
    label = tk.Label(kolekcja_window, text=kolekcja_text, font=("Arial", 12))
    label.pack(padx=20, pady=20)

# Lista ryb i kolekcja
ryby = ["karas", "sielawa", "sum", "pstrąg", "węgorz"]
kolekcja = []

# Etykieta do wyświetlania komunikatów
wynik_label = tk.Label(root, text="Witaj w Symulatorze Łowienia Ryb!", font=("Arial", 14))
wynik_label.pack(pady=20)

# Ustawienie tła jeziora na początku
ustaw_tlo()

# Przyciski
low_przycisk = tk.Button(root, text="Złóż wędkę", command=low_rybe, font=("Arial", 12), bg="lightblue")
low_przycisk.pack(pady=10)

kolekcja_przycisk = tk.Button(root, text="Pokaż kolekcję", command=pokaz_kolekcje, font=("Arial", 12), bg="lightgreen")
kolekcja_przycisk.pack(pady=10)

# Uruchomienie głównej pętli gry
root.mainloop()
