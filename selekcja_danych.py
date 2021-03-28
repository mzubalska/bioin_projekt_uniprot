# -*- coding: utf-8 -*-

# Program przyjumujacy na wejsciu dane pobrane z bazy danych Uniprot a nastepnie
# Tworzacy bazy danych zawierających informacje o ID białek, długościach sekwencji oraz ilości domen.

# Skrypt w tym projekcie został wykorzystany dla danych: 'human_all.txt', 'human_revieved.txt',
# 'human_unreviewed.txt','Drozdze_all', 'Drozdze_reviewed.txt', 'Drozdze_unreviewed.txt',
# 'Danio_all.txt', 'Danio_reviewed.txt', 'Danio_unreviewe.txt', 'human_2010.txt', 'drozdze_2010.txt', danio_2010.txt.

lista = []
lista_all = []


with open('Danio_reviewed.txt', 'r') as k:
    lines = k.readlines()
for line in lines:
    line = line.split()

    if len(line) > 1:
        lista_all.append(line)

for i in range(len(lista_all)):
    if lista_all[i][0] == 'ID':
        lista.append(lista_all[i][0:4])
    if lista_all[i][1] == 'Pfam;':
        a = len(lista)
       # print(a)
        lista[a-1].append((float(lista_all[i][4])))

for i in range(len(lista)):
    del lista[i][2]

liczba = []
dlugosc = []

for i in lista:
    s = sum(i[3:])
    liczba.append(s)
    c = i[2]
    dlugosc.append(int(c))
   # sum_lenght = sum(i[2])

l_n = []
for i in lista:
     l_n.append(i[:3])

for i in range(len(liczba)):
    l_n[i].append((liczba[i]))
    
def save(plik):
    with open(plik, 'w+') as f:
       # f.write('Id    lenght    domeny \n')
        for i in l_n:
        #    f.write('Id    lenght    domeny')
       #     f.write(i[0] + '    ')
            f.write(i[1] + '\t')
            f.write(i[2] + '\t')
            f.write(str(i[3]) + '\n')

save('Danio_reviewed_out.txt')

# srednia liczba dommen sum(liczba)/a)
mean_dom = sum(liczba)/a

# srednia dlugosc lancucha
mean_chain = sum(dlugosc)/a

print('srednia liczba dommen: ', mean_dom)
print('srednia dlugosc lancucha: ', mean_chain)
