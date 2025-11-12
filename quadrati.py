#chiede all'utente un numero positivo e stampa i quadrati dei numeri fino a n

n = int(input("Inserisci un numero: "))
if n >= 0:
    for i in range (n+1):
        print(i*i, end = " ")
else:
    print(f"Non posso stampare quadrati minore di {n}, perchè non esistono quadrati minori di 0 ")