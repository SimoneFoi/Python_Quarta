#Scrivi un programma in Python nel quale assegni alla variabile lista_voti una lista con tutti i tuoi voti (almeno 6). Sfrutta 
#l'indicizzazione per: stampare la lista senza il primo e l'ultimo voto, sostituire il 4o voto con un 10, stampare i primi 3 voti della lista

lista_voti = [7, 8, 9.5, 6, 8, 9, 10, 8.75]
print(f"La lista completa senza il primo e ultimo elemento è: {lista_voti[1:-1]}")
lista_voti[4] = 10
print(f"Il quarto elemento ora e' {lista_voti[4]}");
print(f"I primi 3 voti della lista sono: {lista_voti[0:3]}")