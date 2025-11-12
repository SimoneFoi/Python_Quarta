#creare una lista uguale a quella di partenza con i nomi in maiuscolo

lista = ["Luca", "Mario", "Alice", "Giovanni"]
lista2 = []
for nome in lista:
    lista2.append(nome.upper())
    print(f"{lista2[::-2]}")