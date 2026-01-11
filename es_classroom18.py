#Un file contiene un numero intero per riga. Leggere il file e calcolare: somma, media, minimo e massimo.

file = open("testo_classroom3.txt", "r", encoding= "utf8")
righe = file.readlines()
file.close() 

min = 10000
max = 0
cont = 0
somma = 0

for i in righe:
    somma += int(i)
    cont += 1
    if int(i) < min:
        min = int(i)
    if int(i) > max:
        max = int(i)
media = somma / cont
print(somma, media, min, max)
