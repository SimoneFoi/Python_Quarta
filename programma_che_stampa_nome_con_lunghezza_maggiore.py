#stampare l'elemento con numero di lettere maggiore

lista = ["Luca", "Mario", "Alice", "Giovanni"]
lun_max = 0
nome_max = ""
for nome in lista:
    lun = len(nome)
    if lun > lun_max:
        lun_max = lun
        nome_max = nome
print(nome_max)
