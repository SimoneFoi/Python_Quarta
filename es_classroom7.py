#Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente), trovare quale voto compare più spesso.

studenti_voti = {
"Marco": 7,
"Sara": 8,
"Luca": 6,
"Elena": 8,
"Paolo": 7,
"Giulia": 8,
"Andrea": 6,
"Chiara": 7
}

diz_voti = {}
voti_record = {}

for i in studenti_voti:
    if studenti_voti[i] in diz_voti:
        diz_voti[studenti_voti[i]] += 1
    else:
        diz_voti[studenti_voti[i]] = 1
print(diz_voti)

max_frequenza = 0
for voto in diz_voti:
    if diz_voti[voto] > max_frequenza:
        max_frequenza = diz_voti[voto]
print(f"Il/i voto/i che compare/compaiono più spesso, {max_frequenza} volte, è/sono: ")
for voto in diz_voti:
    if diz_voti[voto] == max_frequenza:
        print(voto, end= ", ")

