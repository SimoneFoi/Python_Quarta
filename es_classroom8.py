#Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. Se una chiave è presente in entrambi, sommare i valori.

vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}
dizionario_finale = {}

for i in vendite_gennaio:
    if i in vendite_febbraio:
        dizionario_finale[i] = vendite_gennaio[i] + vendite_febbraio [i]
    else:
        dizionario_finale[i] = vendite_gennaio[i]
for i in vendite_febbraio:
    if i in dizionario_finale:
        pass
    else:
        dizionario_finale[i] = vendite_febbraio[i]

print(dizionario_finale)