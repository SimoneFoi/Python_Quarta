def temp_media(dati):
    somma = 0
    for i in dati:
        somma += i["temp"]
    return somma / len(dati)

def filtra_citta(dati, nome):
    l = []
    for i in dati:
        if i["citta"] == nome:
            l.append(i["temp"])
    return l

def temp_per_citta(dati):
    diz = {}
    for i in dati:
        if i["citta"] in diz:
            pass
        else:
            diz[i["citta"]] = filtra_citta(dati, i["citta"])
    return diz

def carica_regioni(nome_file):
    diz = {}

    file = open(nome_file, "r", encoding="utf8")
    righe = file.readlines()
    file.close()

    for i in righe:
        parole = i.strip().split(" ")
        diz[parole[0].replace(";", "")] = parole[1]
    return diz

def main():
    dati = [
        {"citta": "Milano", "temp": 12},
        {"citta": "Roma", "temp": 18},
        {"citta": "Milano", "temp": 14},
        {"citta": "Napoli", "temp": 20},
        {"citta": "Roma", "temp": 17},
        {"citta": "Napoli", "temp": 22},
        {"citta": "Milano", "temp": 10}
    ]
    print(f"La media delle temperature è: {temp_media(dati):.2f} gradi Celsius")

    nome = "Milano"
    print(f"Le temperature nella città di Milano sono: {filtra_citta(dati, nome)}")

    print(f"Temperature per città: {temp_per_citta(dati)}")

    print("Elenco città e regioni: ", end= " ")
    print(carica_regioni("regioni.txt"))

if __name__ == "__main__":
    main()