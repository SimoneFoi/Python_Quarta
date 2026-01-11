#Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
#(a) contare le canzoni totali, 
# (b) cercare in quale playlist si trova una canzone, 
# (c) unire due playlist in una nuova.

def num_canzoni(playlist):
    a = 0
    for i in playlist:
        a += len(playlist[i])
    return a

def playlist_con_canzone(playlist, canzone):
    for i in playlist:
        if canzone in playlist[i]:
            return i

def unisci_playlist(playlist, playlist1, playlist2):
    new_playlist = {}
    l = []
    trovato = False
    for i in playlist:
        if playlist1 in playlist and playlist2 in playlist:
            l = playlist[playlist1] + playlist[playlist2]
            if i != playlist1 and i != playlist2:
                new_playlist[i] = playlist[i]
            if i == playlist1 or i == playlist2 and trovato == False:
                new_playlist["Nuova playlist: "] = l
                trovato = True
        else:
            print("Uno dei due parametri passati, o entrambi, è/sono sbagliati")
    return new_playlist

def main():
    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }

    print("Numero di canzoni nelle playlist: ", end= "")
    print(num_canzoni(playlist))
    
    canzone = input("Inserisci la canzone che vuoi ricercare: ")
    print(f"La canzone {canzone} si trova nella playlist ", playlist_con_canzone(playlist, canzone))

    playlist1 = input("Inserisci la prima playlist che vuoi unire: ")
    playlist2 = input("Inserisci la seconda playlist che vuoi unire: ")
    print("Nuova playlist: ")
    print(unisci_playlist(playlist, playlist1, playlist2))    

if __name__ == "__main__":
    main()