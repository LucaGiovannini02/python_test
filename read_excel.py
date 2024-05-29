import pandas as pd
import sqlite3 as sq

# exc = pd.read_excel('CodiciCatastali.xls')
# print(exc)

# aus = []
# conn = sq.connect('CodiceFiscale.sqlite3')
# cur = conn.cursor()

# for x in str(exc).splitlines():
#     j = x.split()
#     print(j)
#     if not j[0].isnumeric:
#         continue
#     cur.execute("INSERT INTO TCoidciCatastali (comune, provincia, codiceCatastale) VALUES (?, ?, ?)", [str(j[1]), str(j[2]), str(j[3])])
#     conn.commit()
    # print(j[1])

prova = pd.read_excel('CodiciCatastali.xls', index_col=0, header=0)
print(prova)

# print(aus)