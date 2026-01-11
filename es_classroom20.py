#Scrivere una funzione che disegni un poligono regolare dato il numero di lati e la lunghezza del lato. Esempi di chiamata:
#poligono(4, 100) --> quadrato
#poligono(6, 80)  --> esagono
#poligono(8, 60)  --> ottagono

import turtle

def disegna(n_lati, lunghezza):
    for i in range(n_lati):
        turtle.forward(lunghezza)
        turtle.left(360 / n_lati)

def main():
    n_lati = int(input("Inserisci il numero dei lati del poligono: "))
    lunghezza = int(input("Inserisci la lunghezza del lato: "))
    disegna(n_lati, lunghezza)

if __name__ == "__main__":
    main()