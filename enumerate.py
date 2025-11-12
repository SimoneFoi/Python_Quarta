def main0():
    lista = ["Luca", "Mario", "Alice", "Giovanni"]
    nome_max = ""                   #scrivere "" è uguale a None
    len_max = 0
    for nome in lista:
        if len(nome) > len_max:
            nome_max = nome
            len_max = len(nome)
    print(nome_max)

def main():
    lista = ["Alice", "Mario", "Luca", "Giovanni"]
    for i, nome in enumerate(lista):
        print(f"{i} - {nome}")

if __name__ == "__main__":          #__ dunder (double underscore) è una variabile
                                    #è vera quando eseguo il programma
    print(__name__)                 #il __ indica che è privata
    main()
                                    #è falsa se la importo come libreria
