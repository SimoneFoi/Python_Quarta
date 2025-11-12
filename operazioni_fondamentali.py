#Scrivi un programma che permetta all'utente di effettuare le 4 operazioni aritmetiche. Per prima cosa chiede all'utente quale operazione
#desidera eseguire (0: somma, 1: sottrazione, 2: moltiplicazione, 3: divisione), poi chiede all'utente due numeri e stampa il risultato
#dell'operazione

n = int(input("Inserisci un numero che indica il tipo di operazione che vuoi effettuare: "))
if n == 0:
    print("Somma")
elif n == 1:
    print("Sottrazione")
elif n == 2:
    print("Moltiplicazione")
elif n == 3:
    print("Divisione")
v1 = int(input("Inserisci primo valore: "))
v2 = int(input("Inserisci secondo valore: "))      
if n == 0:
    somma = v1 + v2
    print(somma)
elif n == 1:
    differenza = v1 - v2
    print(differenza)
elif n == 2:
    prodotto = v1 * v2
    print(prodotto)
elif n == 3:
    rapporto = v1 / v2
    print(rapporto)