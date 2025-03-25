import pdfplumber
import numpy as np


def extract_pdf():
    with pdfplumber.open('manual.4391de117.pdf') as file:
        f = file.pages[0]
        f = f.extract_text()[236:]

        c = sorted(filter(lambda x: len(x) > 4, f.split()))[:-1]

    a = []
    for i in c:
        a.append(float(str((i).replace(',','.'))))

    x = []

    i1 = 0.00
    for i in np.arange(0.0, 200):
        i1 += 0.01
        x.append(round(i1, 3))

    i2 = 2.00
    for j in np.arange(0.0, 100, 2):
        i2 += 0.02
        x.append(round(i2, 3))

    i3 = 3.00
    for k in np.arange(0.0, 200, 5):
        i3 += 0.05
        x.append(round(i3, 3))
    x.insert(00, 0.00)

    xf = {}
    for j, f in zip(x, a):
        xf[j] = f

    return xf





