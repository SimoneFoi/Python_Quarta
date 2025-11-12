#in Python abbiamo le collezioni, insieme di diversi elementi. Tra le condizioni abbiamo le liste, tuple, Set e dizionari

#Creare una lista
l = [3, 3.14, 10, "ciao", True]

#Per accedere agli elementi vigono le stesse regole di INDICIZZAZIONE e SLICING delle stringhe
print(f"L'ultimo elemento della lista e'{l[-1]}")
print(f"Elementi della lista: {l}")
print(f"Tutta la lista senza il primo e l'ultimo elemento è {l[1:-1]}")

#Aggiunta di un elemento
l.append("NUOVO")                       #Non restituisce nulla, ma modifica l
print(f"Elementi della lista: {l}")

#Eliminare un elemento
l.pop()
print(f"Elementi della lista: {l}")
