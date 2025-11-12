a = input("Inserisci una stringa: ")
n = int(input("inserisci un numero: "))
if n <= len(a):
    a = a[0 : (len (a) - n)] + "*" * n
    print(a)
else:
    print(f"Impossibile")