#Verificare se la somma dei primi n numeri dispari è un quadrato perfetto

import math             #dentro math c'è una funzione che fa la radice quadrata e una che fa la radice quadrata intera

n = int(input("Inserisci un numero: "))
somma = 0
if n >= 0:
    for i in range (1, 2 * n + 1, 2):
        somma = somma + i
        radice_intera = math.isqrt(somma)                                                #radice intera della somma
    print(f"La somma vale {somma}, il quadrato perfetto: {radice_intera ** 2 == somma}") #condizione nella stampa che restituisce sempre true
else:
    print(f"Non puoi darmi un numero di elementi negativo! ")