#crea un programma in python che chiede all'utente un numero intero e stampa se il numero è divisibile per 2, per 3 o per 5 
#Usare operatore % per il resto della divisione

numero = int(input("Inserisci un numero intero: "))
if numero % 2 == 0:
    print(f"{numero} è divisibile per 2. ")
elif numero % 3 == 0:
    print(f"{numero} è divisibile per 3. ")
elif numero % 5 == 0:
    print(f"{numero} è divisibile per 5. ")
else:
    print(f"{numero} non e' divisibile per nessuno di questi numeri")