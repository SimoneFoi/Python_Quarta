intero = int(input("Inserisci un numero intero: "))
print(f"Hai inserito {intero} che e' di tipo {type(intero)}") 

decimale = float(input("Inserisci un numero reale: "))
print(f"Hai inserito {decimale} che e' di tipo {type(decimale)}") 

somma = decimale + intero
print(f"La somma tra i due numeri vale {somma} ed è di tipo {type(somma)}")