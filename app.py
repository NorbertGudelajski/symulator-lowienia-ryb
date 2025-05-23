
import tkinter as tk
from ui import UI
from gra import Gra

class SymulatorLowienia:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Symulator Łowienia Ryb")
        self.root.attributes('-fullscreen', True)
        self.gra = Gra(self.root)
        self.ui = UI(self.root, self.gra)

    def uruchom(self):
        self.ui.ekran_powitalny()
        self.root.mainloop()

