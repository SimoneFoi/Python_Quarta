#Un dizionario associa nomi di squadre a liste di giocatori. Scrivere funzioni per: 
# (a) trovare la squadra con più giocatori, 
# (b) verificare se un giocatore è in una squadra, 
# (c) trasferire un giocatore da una squadra all’altra.

def squadra_con_piu_giocatori(squadre):
    max = 0
    squadra = ""
    for i in squadre:
        if len(squadre[i]) > max:
            max = len(squadre[i])
            squadra = i
    print(squadra, "--> ", max, " giocatori")

def giocatore_in_squadra(squadre, giocatore):
    ok = False
    for i in squadre:
        if giocatore in squadre[i]:
            print(giocatore, "-->", i)
            ok = True
    if ok == False:
        print("Il giocatore non è presente o il suo cognome è stato scritto erroneamente")
    

def trasferisci_giocatore(squadre, giocatore, nuova_squadra):
    for i in squadre:
        if giocatore in squadre[i] and nuova_squadra in squadre:
            squadre[i].remove(giocatore)
            squadre[nuova_squadra].append(giocatore)
            
    print(squadre)

def main():
    squadre = {
    "Juventus": ["Vlahovic", "Chiesa", "Locatelli", "Bremer"],
    "Inter": ["Lautaro", "Thuram", "Barella", "Bastoni", "Calhanoglu"],
    "Milan": ["Leao", "Theo", "Reijnders"]
    }

    squadra_con_piu_giocatori(squadre)

    cognome = input("Inserisci il cognome del giocatore che vuoi cercare: ")
    giocatore_in_squadra(squadre, cognome)

    giocatore = input("Inserisci il calciatore che vuoi cedere: ")
    nuova_squadra = input(f"Inserisci la squadra a cui vuoi vendere il calciatore {giocatore}: ")
    trasferisci_giocatore(squadre, giocatore, nuova_squadra)

if __name__ == "__main__":
    main()