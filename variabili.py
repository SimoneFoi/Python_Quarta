#il carattere # serve per i commenti
#in questi programma useremo l'assegnazione
#in python non ci sono dichiarazioni: Python fa dynamic type checking (controllo dinamico dei tipi)
#python capisce i tipi sulla base dei valori assegnati alle variabili
a = input("Scrivi qualcosa: ")              #e' simile a scanf
#input restituisce SEMPRE stringhe!
#facciamo una print con una f-string
print(f"Hai inserito {a} che e' di tipo {type(a)}")