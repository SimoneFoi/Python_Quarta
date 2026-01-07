#Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni per: 
# (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più recente.

def cerca_libri_autore(autore, libri):
    for i in libri:
        if(i["autore"] == autore):
            print(i)

def calcola_prezzo_medio(libri):
    somma = 0
    cont = 0
    for i in libri:
        somma += i["prezzo"]
        cont += 1
    media = somma / cont
    return media

def trova_libro_piu_recente(libri):
    recente = libri[0]
    for i in libri:
        if i["anno"] > recente["anno"]:
            recente["anno"] = i["anno"]
    print(recente)

def main():
    libri = [
    {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
    {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
    {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
    {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]

    for i in libri:
        print(i)
    print("Libri per autore: ")
    autore = input("Inserisci l'autore che vuoi ricercare (nome e cognome): ")
    print("Libro/i: ", end= " ")
    cerca_libri_autore(autore, libri)
    print("Prezzo medio libri: ", end= " ")
    media = calcola_prezzo_medio(libri)
    print(media)
    print("Libro più recente: ", end= " ")
    trova_libro_piu_recente(libri)

if __name__ == "__main__":
    main()