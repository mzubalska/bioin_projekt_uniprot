# bioin_projekt_uniprot

Założenia projektu:
* Ustalenie jakiej długości oraz ilu domenowe białka preferuje człowiek (Homo sapiens).
* Zestawienie danych z dwoma przykładowymi organizmami: Danio rerio oraz Saccharomyces cerevisiae

Narzędzia:
* Uniprot SwissPro
* Pfam.xfam.org
* Python: Pandas, Matplotlib, Numpy, Scipy.stats

Metodologia:
* Pobranie wszystkich danych dla białek Homo sapiens, Danio rario i Saccharomyces civisareas z bazy Uniprot.
* Utworzenie bazy danych zawierających informacje o ID białek, długościach sekwencji oraz ilości domen. -> skrypt selekcja_danych.py
* Wykonanie statystyk.
  hist_stat.py
  danio_reviewed_rozkla_g.py - skryp z wizualizacja rozkładu wartości ekstremalnej tu przykladowo dla danio
* Porównanie otrzymanych wyników z danymi z publikacji („Mathematical modeling and comparison of protein
  size distribution in different plant, animal, fungal and microbial species reveals a negative correlation between protein size and protein number")
  
