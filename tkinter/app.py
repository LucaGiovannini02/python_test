from tkinter import ttk
from tkinter import *

from pages.AggiungiDipendentePage import AggiungiDipendentePage
from pages.VisualizzaDipendentiPage import VisualizzaDipendentePage
from pages.CalcolaCodiceFiscalePage import CalcolaCodiceFiscalePage

def OpenAggiungiDipendentePage():
    newPage = Toplevel()
    newPage.title("Aggiungi dipendente")
    AggiungiDipendentePage(newPage)

def OpenVisualizzaDipendentePage():
    newPage = Toplevel()
    newPage.title("Visualizza dipendenti")
    VisualizzaDipendentePage(newPage)

def OpenVisualizzaDipendentePage():
    newPage = Toplevel()
    newPage.title("Calcola CF")
    CalcolaCodiceFiscalePage(newPage)

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="CF").grid()

widthButtons = 25

ttk.Button(frm, text="Aggiungi dipendente", command=OpenAggiungiDipendentePage, width=widthButtons).grid()
ttk.Button(frm, text="Visualizza dipendente", command=OpenVisualizzaDipendentePage, width=widthButtons).grid()
ttk.Button(frm, text="Calcola CF", command=OpenVisualizzaDipendentePage, width=widthButtons).grid()
ttk.Button(frm, text="Chiudi", command=root.destroy, width=widthButtons).grid()

root.mainloop()