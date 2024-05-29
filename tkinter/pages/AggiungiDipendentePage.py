from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

from utils.db import get_db

def AggiungiDipendentePage(page):
    frm = ttk.Frame(page, padding=10)
    frm.pack()
    ttk.Label(frm, text="Aggiungi dipendente").pack()

    widthButtons = 25

    ttk.Label(frm, text="Nome: ").pack()
    nome = ttk.Entry(frm, width=widthButtons)
    nome.pack()

    ttk.Label(frm, text="Cognome: ").pack()
    cognome = ttk.Entry(frm, width=widthButtons)
    cognome.pack()

    ttk.Label(frm, text="Data nascita: ").pack()
    cal = DateEntry(frm, width=widthButtons, date_pattern="yyyy/mm/dd")
    cal.pack(padx=10, pady=10)

    ttk.Label(frm, text="Sesso: ").pack()
    sesso = ttk.Combobox(frm, width=widthButtons)
    sesso['values'] = ('M', 'F')
    sesso.pack()

    ttk.Label(frm, text="Comune: ").pack()
    comune = ttk.Entry(frm, width=widthButtons)
    comune.pack()

    def confirm():
        aus = cal.get_date()
        aus = str(aus).split("-")
        aus = aus[0] + "-" + aus[2] + "-" + aus[1]

        if nome.get() and cognome.get() and sesso.get() and comune.get():
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT codiceCatastale FROM TCodiciCatastali WHERE comune = ?", [str(comune.get()).upper()])
            try:
                data = cur.fetchone()['codiceCatastale']

                cur.execute("INSERT INTO TDipendenti (nome, cognome, nascita, sesso, codiceComune) VALUES (?, ?, ?, ?, ?)", [str(nome.get()), str(cognome.get()), aus, str(sesso.get()), str(data)])
                conn.commit()
                page.destroy()
            except: 
                messagebox.showerror(title="Errore", message="Comune insesistente!")
        else:
            messagebox.showerror(title="Errore", message="Inserire i dati correttamente!")

    ttk.Button(frm, text="Conferma", command=confirm, width=widthButtons).pack()
    ttk.Button(frm, text="Quit", command=page.destroy, width=widthButtons).pack()

    page.mainloop()