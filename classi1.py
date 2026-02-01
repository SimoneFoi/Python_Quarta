#In Python tutto è un oggetto! Anche int o float sono oggetti! Anche le funzioni sono oggetti.

#Creare classi ci permette di creare nuovi oggetti

import math
import turtle

class Punto():
    #costrutttore viene chiamato da Punto()
    def __init__(self, x, y):     #self è come this in Java
        #attributi (in Python tutto è pubblicato)
        self.x = x
        self.y = y

    def __str__(self):
        #deve ritornare una stringa
        return f"{self.x, self.y}"
    
    def distanza_origine(self):
        #ritorna la distanza del punto dall'origine 0,0
        return math.sqrt(self.x**2 + self.y**2)
    
    def scambia_coordinate(self):
        #questo metodo ritorna un nuovo punto con x, y scambiati
        b = Punto(self.y, self.x)
        return b
    
    def disegna(self):
        #questo metodo usa Turtle per disegnare il punto
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.dot()
        turtle.mainloop()

    def distanza(self, altro):
        #questo metodo restituisce la distanza tra il punto e altro
        #altro è una istanza di un altro punto
        dx = self.x - altro.x
        dy = self.y - altro.y
        return math.sqrt(dx * dx + dy * dy)

def main():
    a = Punto(1, 2)     #istanza di punto in coordinate
    b = Punto (4, 6)
    print(a)
    print(f"Il punto dista {a.distanza_origine():.2f} dall'origine")
    print(a.scambia_coordinate())
    print(a.distanza(b))
    a.disegna()

if __name__ == "__main__":
    main()