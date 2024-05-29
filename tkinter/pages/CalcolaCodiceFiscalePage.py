from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from codicefiscale import codicefiscale

from utils.db import get_db

def CalcolaCodiceFiscalePage(page):
    frm = ttk.Frame(page, padding=10)
    frm.pack()
    ttk.Label(frm, text="Calcolo CF").pack()

    widthButtons = 25

    ttk.Label(frm, text="id utente: ").pack()
    id = ttk.Entry(frm, width=widthButtons)
    id.pack()

    def confirm():
        conn = get_db()
        cur = conn.cursor()

        if id.get():
            cur.execute("SELECT * FROM TDipendenti WHERE id = ?", [str(id.get())])
            data = cur.fetchone()
            if not data:
                messagebox.showerror(title="Errore", message="Utente non trovato")
                return
            aus = str(data[3]).split("-")
            aus = str(aus[1] + "/" + aus[2] + "/" + aus[0])
            cf = codicefiscale.encode(
                firstname=data[1],
                lastname=data[2],
                gender=data[4],
                birthdate=aus,
                birthplace=data[5],
            )

            cur.execute("UPDATE TDipendenti SET codiceFiscale = ? WHERE id = ?", [str(cf), str(data[0])])
            conn.commit()

            messagebox.showinfo(title="CF", message=str(cf))
        else:
            messagebox.showerror(title="Errore", message="Inserire i dati correttamente!")

    ttk.Button(frm, text="Conferma", command=confirm, width=widthButtons).pack()
    ttk.Button(frm, text="Quit", command=page.destroy, width=widthButtons).pack()

    page.mainloop()