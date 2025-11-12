#crea un programma che chiede all'utente una frase e stampi la stringa un carattere si e uno no

frase = input("Inserisci una frase: ")
print(f"La frase modificata e' {frase[::2]}")