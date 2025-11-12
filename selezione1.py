print("Premi A per inserire. ")
print("Premi B per modificare. ")
print("Premi C per cancellare. ")
tasto = input("--> ")
tasto = tasto.upper()                                #METODO (non funzione) che trasforma testo in maiuscolo
                                                     #.lower trasforma tutto in minuscolo
if tasto == "A":
    print("L'utente vuole inserire")
elif tasto == "B":
    print("l'utente vuole modificare")
elif tasto == "C":
    print("l'utente vuole cancellare")
else:
    print("tasto non valido")