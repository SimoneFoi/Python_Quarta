#Attributi: lato, colore, x, y del vertice
#Metodi: area, perimetro, disegna
#Scrivere un programma che disegni 100 quadrati casuali 

import turtle
import random

class Quadrato:
    def __init__(self, lato, colore, x, y):
        self.lato = lato
        self.colore = colore
        self.x = x
        self.y = y

    def area(self):
        return self.lato * self.lato

    def perimetro(self):
        return self.lato * 4

    def disegna(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.colore)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.right(90)
        turtle.end_fill()

def main():
    for _ in range(100):
        lato = random.randint(10, 50)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        colore = random.choice(["red", "blue", "green", "black"])

        q = Quadrato(lato, colore, x, y)
        q.disegna()

if __name__ == "__main__":
    main()