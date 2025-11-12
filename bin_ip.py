#chiede all'utente il numero di bit, poi chiede un numero binario (gestito come stringa). Se la lunghezza del numero binario inserito
#è minore del numero inserito aggiungiamo a sinistra tanti 0 quanti bastano per arrivare al numero di bit

n_bit = int(input("Inserisci il numero di bit: "))
n_bin = input("Inserisci un numero binario: ")
lunghezza = len(n_bin)
if lunghezza < n_bit:
    print(n_bin + ((n_bin - lunghezza) * "0"))
elif lunghezza > n_bit:
    print("Hai fornito un numero sbagliato")
else:
    print(n_bin)