#l'utente inserisce in input una password
#il programma stampa la password oscurata da asterischi

password = input("Inserisci una password: ")
password_blanked = "*" * len(password)
print(f"Hai inserito la password: {password_blanked}")