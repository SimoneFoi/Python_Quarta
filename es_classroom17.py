#Leggere un file di testo e trovare la parola che compare più volte (ignorando maiuscole/minuscole).

file = open("./testo_classroom2.txt", "r", encoding= "utf8")
righe = file.readlines()
file.close()

diz = {}
for i in righe:
    parole = i.lower().split(" ")
    for p in parole:
        p = p.strip()
        if p in diz:
            diz[p] += 1
        else:
            diz[p] = 1
print(diz)