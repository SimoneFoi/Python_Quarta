def oscuraPassword(s):
    nCaratteri = len(s)
    return s[0] + (nCaratteri - 1) * "*"

lista = ["ciao", "mondo"]
newLista = []
for password in lista:
    newLista.append(oscuraPassword(password))
print(newLista)