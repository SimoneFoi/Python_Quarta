#Data una lista, restituire una nuova lista contenente gli stessi elementi ma senza duplicati, mantenendo l’ordine di prima apparizione.

elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]
nuova_lista = []

for i in elementi:
    if i in nuova_lista:
        pass
    else:
        nuova_lista.append(i)
print(elementi)
print(nuova_lista)