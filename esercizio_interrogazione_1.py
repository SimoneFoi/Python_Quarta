file = open("./nomeFile", "r")
contenuto = file.readlines()
for riga in contenuto:
    if riga[0] == "#":
        print(riga)
file.close