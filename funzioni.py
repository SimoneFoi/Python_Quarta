# MODULARITA': proprietà del codice che consiste nel suddividere il codice in funzioni

#COSTANTE è una variabile di tipo globale. Le variabili locali sono accessibili da tutte le funzioni soltanto in LETTURA
COSTANTE = 3.14

def prima_lettera_maiuscola(stringa):
    """ 
    DOCSTRING:
    La funzione restituisce stringa con la lettera iniziale maiuscola
    La funzione help() restituisce quanto scritto qua dentro
    """
    #stringa è una variabile locale alla funzione
    s = stringa[0].upper() + stringa[1:]
    return s

def media(lista):
                                #La funzione restituisce la media dei valori presenti in lista e il numero di elementi di lista
    somma = 0.
    nlista = len(lista)
    for val in lista:           #val non è l'indice ma il VALORE
        somma = somma + val
    return somma / nlista, nlista;

def main():
    #print(help(prima_lettera_maiuscola))
    nome = input("Inserisci una parola: ")
    print(prima_lettera_maiuscola(nome))
    voti = [4.5, 10, 8.25, 7, 6]
    m, n = media(voti)
    print(f"La media è {m}, il numero di voti {n}.")
    if m > 6.:
        print("😊")
    else:
        print("😡")

if __name__ == "__main__":
    main()