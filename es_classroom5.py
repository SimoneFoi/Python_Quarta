#Data una stringa, costruire un dizionario che associ a ogni carattere il numero di volte che compare.

testo = "abracadabra"

diz = {}

for i in testo:
    if i in diz:
        diz[i] += 1
    else:
        diz[i] = 1
print(diz)