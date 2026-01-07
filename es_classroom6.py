"""
Dato un dizionario italiano-inglese e una frase in italiano, restituire la frase tradotta. Se una parola non è nel dizionario, 
lasciarla invariata.
"""

dizionario = {
"ciao": "hello",
"mondo": "world",
"casa": "house",
"gatto": "cat",
"cane": "dog",
"libro": "book",
"albero": "tree"
}

frase = "ciao mondo il gatto è in casa"
s = ""

parole = frase.split(" ")
for i in parole:
    if i in dizionario:
        s = s + dizionario[i] + " "
    else:
        s = s + i + " "
print(s)