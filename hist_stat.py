# -*- coding: utf-8 -*-

import sys
# from imp import reload

# reload(sys)
# sys.setdefaultencoding('utf8')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab

# import scipy.stats as stats

'''
STATYSTYKI
'''
'''
#liczba domen statystyki
srednia=data["Liczba domen"].mean()
print(srednia', srednia)

odchylenie=data["Liczba domen"].std()
print(ochylenie', odchylenie)

#dlugosc lancucha staty

srednia1=data['Długość łańcucha'].mean()
print(srednia',srednia1)

odchylenie1=data['Długość łańcucha'].std()
print(ochylenie',odchylenie1)
'''

# -------------------------DROZDZE_UNREVIEWED----------------------

data1 = pd.read_csv('Drozdze_unreviewed_out.txt',
                    sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# histogram długosc łańcucha
dwiekolumny = data1[data1.columns[1:3]]
dwiekolumny.hist(column='Długość łańcucha', bins=50, figsize=(10, 10), color='lawngreen', density=True)
plt.title('Saccharomyces cerevisiae unreviewed - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 3000])

dwiekolumny.hist(column='Liczba domen', bins=30, figsize=(10, 10), color='lawngreen', density=True)
plt.title('Saccharomyces cerevisiae unreviewed ', color='black', fontsize=18)
plt.xlabel('Naber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 45])

# -------------------------DROZDZE REVIEWED----------------------
data2 = pd.read_csv('Drozdze_reviewed_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# histogram długosc łańcucha
dwiekolumny2 = data2[data2.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny2.hist(column='Długość łańcucha', bins=30, figsize=(10, 10), color='palegreen', density=True)
plt.title('Saccharomyces cerevisiae reviewed  - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 2000])


dwiekolumny2.hist(column='Liczba domen', bins=30, figsize=(10, 10), color='palegreen', density=True)
plt.title('Saccharomyces cerevisiae reviewed', color='black', fontsize=18)
plt.xlabel('Naber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 6])

# -------------------------DROZDZE ALL----------------------
data3 = pd.read_csv('Drozdze_all_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# histogram długosc łańcucha
dwiekolumny3 = data3[data3.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny3.hist(column='Długość łańcucha', bins=70, figsize=(10, 10), color='darkgreen', density=True)
plt.title('Saccharomyces cerevisiae all - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 3000])


dwiekolumny3.hist(column='Liczba domen', bins=70, figsize=(10, 10), color='darkgreen', density=True)
plt.title('Saccharomyces cerevisiae all', color='black', fontsize=18)
plt.xlabel('Naber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 45])

# -------------------------DANIO RERIO REVIEWED----------------------
data4 = pd.read_csv('Danio_reviewed_out2.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# histogram długosc łańcucha
dwiekolumny4 = data4[data4.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny4.hist(column='Długość łańcucha', bins=100, figsize=(10, 10), color='mediumvioletred', density=True)
plt.title('Danio rerio reviewed - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 3500])


dwiekolumny4.hist(column='Liczba domen', bins=40, figsize=(10, 10), color='mediumvioletred', density=True)
plt.title('Danio rerio reviewed', color='black', fontsize=18)
plt.xlabel('Naber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 30])

# -------------------------DANIO RERIO UNREVIEWED----------------------
data5 = pd.read_csv('Danio_unreviewed_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# histogram długosc łańcucha
dwiekolumny5 = data5[data5.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny5.hist(column='Długość łańcucha', bins=300, figsize=(10, 10), color='purple', density=True)
plt.title('Danio rerio all - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 6000])


dwiekolumny5.hist(column='Liczba domen', bins=200, figsize=(10, 10), color='m', density=True)
plt.title('Danio rerio all', color='black', fontsize=18)
plt.xlabel('Nuber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 30])

# -------------------------DANIO RERIO ALL----------------------
data6 = pd.read_csv('Danio_all_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# histogram długosc łańcucha
dwiekolumny6 = data6[data6.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny6.hist(column='Długość łańcucha', bins=300, figsize=(10, 10), color='purple', density=True)
plt.title('Danio rerio unreviewed - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 6000])


dwiekolumny6.hist(column='Liczba domen', bins=200, figsize=(10, 10), color='purple', density=True)
plt.title('Danio rerio unreviewed', color='black', fontsize=18)
plt.xlabel('Nuber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 30])

# -------------------------HOMO SAPIENS REVIEWED----------------------
data7 = pd.read_csv('human_reviewed_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# Stosunek długości łańcucha do ilości domen
data7.plot(legend=False, figsize=(10, 10))
plt.title('Homo Sapiens reviewed - stosunek liczby domen do długości łańcucha', color='black')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Białka')
plt.ylabel('Długość')
pylab.ylim([0, 20000])


# histogram długosc łańcucha
dwiekolumny7 = data7[data7.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny7.hist(column='Długość łańcucha', bins=300, figsize=(10, 10), color='tomato', density=True)
plt.title('Homo Sapiens reviewed - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 5000])


dwiekolumny7.hist(column='Liczba domen', bins=300, figsize=(10, 10), color='tomato', density=True)
plt.title('Homo Sapiens reviewed', color='black', fontsize=18)
plt.xlabel('Nuber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 30])

# -------------------------HOMO SAPIENS ALL----------------------
data8 = pd.read_csv('human_all_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# Stosunek długości łańcucha do ilości domen
data8.plot(legend=False, figsize=(10, 10))
plt.title('Homo Sapiens all - stosunek liczby domen do długości łańcucha', color='black')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Białka')
plt.ylabel('Długość')
pylab.ylim([0, 40000])


# histogram długosc łańcucha
dwiekolumny8 = data8[data8.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny8.hist(column='Długość łańcucha', bins=300, figsize=(10, 10), color='red', density=True)
plt.title('Homo Sapiens all - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 5000])


dwiekolumny8.hist(column='Liczba domen', bins=300, figsize=(10, 10), color='red', density=True)
plt.title('Homo Sapiens all', color='black', fontsize=18)
plt.xlabel('Nuber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 30])

# -------------------------HOMO SAPIENS UNREVIEWED----------------------
data = pd.read_csv('human_unreviewed_out.txt', sep='\t', names=['Nazwa białka', 'Długość łańcucha', 'Liczba domen'])

# Stosunek długości łańcucha do ilości domen
data.plot(legend=False, figsize=(10, 10))
plt.title('Homo Sapiens unreviewed - stosunek liczby domen do długości łańcucha', color='black')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Białka')
plt.ylabel('Długość')
pylab.ylim([0, 40000])


# histogram długosc łańcucha
dwiekolumny = data[data.columns[1:3]]
np.seterr(divide='ignore', invalid='ignore')
dwiekolumny.hist(column='Długość łańcucha', bins=300, figsize=(10, 10), color='red', density=True)
plt.title('Homo Sapiens unreviewed - Histogram długości łańucha', color='black')
plt.xlabel('Długość łańcucha')
plt.ylabel('Liczebność')
pylab.xlim([0, 5000])


dwiekolumny.hist(column='Liczba domen', bins=300, figsize=(10, 10), color='red', density=True)
plt.title('Homo Sapiens unreviewed', color='black', fontsize=18)
plt.xlabel('Nuber of domains', fontsize=16)
plt.ylabel('Density', fontsize=16)
pylab.xlim([0, 30])

# a = data['Długość łańcucha'].describe()
# print(a)
# a1 = data['Liczba domen'].describe()
# print(a1)
