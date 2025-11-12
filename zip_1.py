def main():
    lista_nomi = ["Alice", "Mario", "Luca", "Giovanni"]
    lista_voti = [[6, 10, 5],
                  [7, 6],
                  [8, 10, 9, 9],
                  [5, 8]]
    #Modificare il codice sotto per: 
     #-stampare la media di ognuno
     #-stampare il numero di voti per ognuno
     #-stampare il voto massimo e il voto minimo di ognuno

    for nome, voti in zip(lista_nomi, lista_voti):
        somma = 0
        massimo = voti[0]
        minimo = voti[0]
        for v in voti:
            somma = somma + v
            if v > massimo:
                massimo = v
            if v < minimo:
                minimo = v
            media = somma / len(voti);
        print(f"Nome: {nome} - Voti: {voti} - Massimo: {massimo} - Minimo: {minimo} - Media: {media}")


if __name__ == "__main__":
    main()