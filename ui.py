
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
import tkinter.messagebox
import random

class UI:
    def __init__(self, root, gra):
        self.root = root
        self.gra = gra
        self.frame_start = None
        self.frame_game = None
        self.wynik_label = None
        self.obraz_label = None
        self.walka_canvas = None
        self.aktualne_zdjecie = None

    def ekran_powitalny(self):
        self.frame_start = tk.Frame(self.root, width=1920, height=1080)
        self.frame_start.pack(fill="both", expand=True)
        self.ustaw_tlo(self.frame_start)
        powitalny_tekst = tk.Label(self.frame_start, text="Witaj w Symulatorze Łowienia Ryb!", font=("Comic Sans MS", 40), fg="black", bg="lightblue")
        powitalny_tekst.place(relx=0.5, rely=0.1, anchor="center")
        start_button = tk.Button(self.frame_start, text="Zacznij Łowić", font=("Comic Sans MS", 14, "bold italic"), command=self.przejdz_do_gry, bg="lightgreen", relief="flat")
        start_button.place(relx=0.5, rely=0.6, anchor="center")

    def ustaw_tlo(self, frame):
        sciezka = os.path.join("zdjecia", "jezioro.png")
        try:
            if not os.path.exists(sciezka):
                print(f"Plik {sciezka} nie istnieje!")
                return
            tlo_obraz = Image.open(sciezka)
            tlo_obraz = tlo_obraz.resize((1920, 1080))
            tlo_obraz_tk = ImageTk.PhotoImage(tlo_obraz)
            tlo_label = tk.Label(frame, image=tlo_obraz_tk)
            tlo_label.place(x=0, y=0, relwidth=1, relheight=1)
            tlo_label.image = tlo_obraz_tk
        except Exception as e:
            print(f"Problem z wczytaniem tła: {e}")

    def przejdz_do_gry(self):
        if self.frame_start:
            self.frame_start.destroy()

        self.frame_game = tk.Frame(self.root, width=1920, height=1080)
        self.frame_game.pack(fill="both", expand=True)
        self.ustaw_tlo(self.frame_game)

        self.wynik_label = tk.Label(self.frame_game, text="Zarzucaj wędkę i łów ryby!", font=("Comic Sans MS", 22), fg="black", bg="lightblue")
        self.wynik_label.place(relx=0.5, rely=0.05, anchor="center")

        self.walka_canvas = tk.Canvas(self.frame_game, width=500, height=50, bg="white", highlightthickness=0)
        self.walka_canvas.place_forget()

        low_przycisk = tk.Button(self.frame_game, text="Zarzuć wędkę", command=self.low_rybe,
                                 font=("Comic Sans MS", 12), bg="lightblue", relief="flat", width=50)
        low_przycisk.place(relx=0.5, rely=0.9, anchor="center")

        kolekcja_przycisk = tk.Button(self.frame_game, text="Pokaż kolekcję", command=self.pokaz_kolekcje,
                                      font=("Comic Sans MS", 12), bg="lightgreen", relief="flat", width=20)
        kolekcja_przycisk.place(relx=0.1, rely=0.95, anchor="w")

        zakoncz_button = tk.Button(self.frame_game, text="Zakończ Grę", command=self.zakoncz_gre,
                                   font=("Comic Sans MS", 12), bg="red", relief="flat", width=20)
        zakoncz_button.place(relx=0.9, rely=0.95, anchor="e")

    def low_rybe(self):
        if self.obraz_label:
            self.obraz_label.destroy()
            self.obraz_label = None
        self.wynik_label.config(text="Zarzucasz wędkę...")
        self.root.update()
        time.sleep(2)
        ryba = self.gra.losuj_rybe()
        self.walka_z_ryba(ryba)

    def walka_z_ryba(self, ryba):
        self.walka_canvas.place(relx=0.5, rely=0.2, anchor="center")
        self.walka_canvas.delete("all")
        self.walka_canvas.create_rectangle(10, 20, 490, 30, fill="gray")
        zielona_szerokosc = max(20, 80 - int(ryba.waga * 4))
        zielony_start = random.randint(100, 450 - zielona_szerokosc)
        zielony_koniec = zielony_start + zielona_szerokosc
        self.walka_canvas.create_rectangle(zielony_start, 20, zielony_koniec, 30, fill="green")
        kreska = self.walka_canvas.create_line(10, 15, 10, 35, fill="red", width=2)

        zatrzymaj = False

        def ruch_kreski():
            nonlocal zatrzymaj
            x = 10
            dx = 5
            def animacja():
                nonlocal x, dx
                if zatrzymaj:
                    return
                x += dx
                if x >= 490 or x <= 10:
                    dx = -dx
                self.walka_canvas.coords(kreska, x, 15, x, 35)
                predkosc = max(5, 30 - int(ryba.waga * 2))
                self.root.after(predkosc, animacja)
            animacja()

        def klik(e=None):
            nonlocal zatrzymaj
            self.root.unbind("<space>")
            zatrzymaj = True
            x_kreski = self.walka_canvas.coords(kreska)[0]
            self.walka_canvas.place_forget()
            if zielony_start <= x_kreski <= zielony_koniec:
                self.gra.dodaj_do_kolekcji(ryba)
                self.pokaz_rybe(ryba)
            else:
                self.wynik_label.config(text="Ryba uciekła!")

        self.root.bind("<space>", klik)
        ruch_kreski()

    def pokaz_rybe(self, ryba):
        self.wynik_label.config(text=str(ryba))
        nazwa_pliku = os.path.join("zdjecia", f"{ryba.nazwa}.png")
        if not os.path.exists(nazwa_pliku):
            self.wynik_label.config(text=f"Nie znaleziono pliku: {nazwa_pliku}")
            return
        try:
            obraz = Image.open(nazwa_pliku)
            obraz = obraz.resize((500, 300))
            self.aktualne_zdjecie = ImageTk.PhotoImage(obraz)
            if self.obraz_label:
                self.obraz_label.config(image=self.aktualne_zdjecie)
            else:
                self.obraz_label = tk.Label(self.root, image=self.aktualne_zdjecie)
                self.obraz_label.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            self.wynik_label.config(text=f"Problem z wczytaniem obrazu: {e}")

    def pokaz_kolekcje(self):
        kolekcja_window = tk.Toplevel(self.root)
        kolekcja_window.title("Twoja Kolekcja Ryb")
        kolekcja_text = "\n".join(self.gra.pokaz_kolekcje()) or "Nie złowiłeś jeszcze żadnej ryby."
        label = tk.Label(kolekcja_window, text=kolekcja_text, font=("Comic Sans MS", 12))
        label.pack(padx=20, pady=20)

    def zakoncz_gre(self):
        if tk.messagebox.askyesno("Zakończyć grę?", "Czy na pewno chcesz zakończyć grę?"):
            self.root.quit()
