#A partire da una lista produce una stringa formato dalle 3 stringhe concatenate

l = ["ciao", "python", "casa"]
string = ""                         #definizione di una stringa per evitare che non resti non dichiarata
for i in l:
    string = string + " " + i
    print(string)

print("MODO 2:")
string = l[0]
for i in l[1:]:
    string = string + " " + i
    print(string)