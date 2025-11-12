#In Python possiamo delimitare con "" oppure con ''
stringa = "ciao mondo!"
print(stringa)

#esempio di indicizzazione (estrarre un elemento) della stringa
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

#esempio di slicing (tagliare) delle stringhe
print(f"La sottostringa 2-5 è stringa {stringa[2:5]}.") #[a-b]: prende tutti i caratteri da sinistra incluso a destra escluso

#esempio di concatenazione di stringhe e di assegnazione multipla (vale per ogni tipo di dato)
nome, cognome = "Mario", "Rossi"
x = nome + " " + cognome #x è una stringa che concatena due stringhe
print(x)

#Concatenazione multipla
y = (nome + " ")*5
print(y)