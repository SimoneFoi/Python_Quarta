#Leggere un file di testo e stampare: numero di righe, numero di parole, numero di caratteri (esclusi gli spazi).

file = open("./testo_classroom1.txt", "r", encoding= "utf8")
righe = file.readlines()
file.close()

contRighe = 0
contParole = 0
contCaratteri = 0

for i in righe:
    parole = i.split(" ")
    contParole += len(parole)
    contCaratteri += len(i.replace(" ", ""))
contRighe = len(righe)
print(f"Numero caratteri: {contCaratteri}, Numero parole: {contParole}, Numero righe: {contRighe}")