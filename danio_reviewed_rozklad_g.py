# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy.stats import genextreme
import scipy.stats as ss


def srednie(plik_in):
    listy = []
    domeny = []
    li = 0
    d1 = 0

    with open(plik_in, 'r+') as f:
        for line in f:
            w = line.split()
            d = line.split()
            w = float(w[1])
            d = float(d[2])
            listy.append(w)
            # print(listy)
            domeny.append(d)

        for x, el in enumerate(domeny):
            if el == 0.0:
                domeny[x] = 1.0
        for x in domeny:
            li += 1
            if x == 1.0:
                d1 += 1

    # -------------------------DANIO RERIO REVIEWED----------------------
    data4 = pd.read_csv('Danio_reviewed_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

    # histogram długosc łańcucha
    dwiekolumny4 = data4[data4.columns[1:3]]
    np.seterr(divide='ignore', invalid='ignore')
    dwiekolumny4.hist(column='Długość łańcucha', bins=100, figsize=(10, 10), color='mediumvioletred', density=True)

    p = genextreme.fit(listy, -1)
    print(p)
    ss.genextreme.fit(listy)
    plt.plot(np.linspace(0, 3500), genextreme.pdf(np.linspace(0, 3500), p[0], p[1], p[2]), 'b--', lw=3,
             label='Generalized extreme value distribution ')

    plt.title('Danio rerio reviewed - Histogram długości łańucha', color='black')
    plt.xlabel('Długość łańcucha')
    plt.ylabel('Liczebność')
    plt.legend(loc='upper right')
    pylab.xlim([-10, 3500])
    plt.show()


srednie('Danio_reviewed_out.txt')
