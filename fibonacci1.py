n = int(input("Quanti numeri di Fibonacci vuoi: "))
a, b = 1, 1 #inizializzazione e non dichiarazione
if n > 2:
    for i in range(n):
         #pass = istruzione che rende il codice corretto e quindi eseguibile se non ci sono altre istruzioni al suo interno
         print(a, end = " - ")
         a, b = b, a + b    #funziona solo con assegnazione simultanea (multipla)

elif n == 0:
    print(f"Non hai inserito numeri")
elif n == 1:
    print(f"Hai inserito solo un numero")
elif n == 2:
    print(f"Hai già i due numeri che sono {a} e {b}")
else:
    print(f"Non puoi farlo con meno di due numeri")