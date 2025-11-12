#chiedere una stringa, metterla tutta minuscola e controllare se è palindroma

a = input("Inserisci una stringa: ")
a = a.lower()
if a == a[::-1]:
    print("ok")
else:
    print("La stringa non è palindroma")