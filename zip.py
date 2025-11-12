def main():
    lista_nomi = ["Alice", "Mario", "Luca", "Giovanni"]
    lista_voti = [6, 10, 5, 7]

    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome} - {voto}")
    #zip mi permette di ciclare in parallelo su due o più liste
    #se due liste hanno lunghezze diverse il ciclo si interrompe su quella più corta


if __name__ == "__main__":
    main()