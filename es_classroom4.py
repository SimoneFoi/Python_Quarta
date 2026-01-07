#Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.

lista_a = [1, 5, 8, 12, 15, 20]
lista_b = [3, 5, 10, 12, 18, 20, 25]
nuova_lista = []

for elemento in lista_a:
    trovato = False
    for x in nuova_lista:
        if elemento == x:
            trovato = True
    if elemento in lista_b and trovato == False:
        nuova_lista.append(elemento)

print(nuova_lista)
