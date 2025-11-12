#l'utente inserisce in input una password
#il programma stampa la password oscurata da asterischi

password = input("Inserisci una password: ")
password_blanked = password[0] + "*" * (len(password) - 2) + password[-1]
print(f"Hai inserito la password: {password_blanked}")