def main(): #leggere i file in python

    file = open("./dati.csv", "r")      #oggetto file
    righe = file.readlines()            #lista di stringhe che contiene le righe del file
    print(righe)                        #stampa tutte le righe
    file.close()

    print(righe[0])                     #stampa la prima riga
    titoli = righe[0].split(",")        #è una lista
    print(titoli)                       #stampa come prima ma separati da virgole
    titoli = righe[0][0:-1].split(",")  #stampa tutto tranne lo \n
    print(titoli)

    #unpacking (spacchettamento)
    titolo1, titolo2, titolo3 = righe[0][0:-1].split(",")
    print(titolo1)

    #leggere tutte le altre righe del file e stamparle. Usare un ciclo for pythonico (senza range)

    for i in righe[1:]:
        print(i)

if __name__ == "__main__":
    main()