from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from utils.db import get_db

def VisualizzaDipendentePage(page):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM TDipendenti")
    data = cur.fetchall()

    Lb = Listbox(page, width=100)
    
    for x in data:
        if x[6]:
            cf = x[6]
        else:
            cf = "none"
        Lb.insert(x[0], str(x[0]) + " - " + str(x[1]) + " - " + str(x[2]) + " - " + str(x[3]) + " - " + str(x[4]) + " - " + str(x[5]) + " - " + str(cf))

    Lb.pack()

    page.mainloop()