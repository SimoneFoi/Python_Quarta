import funzioni
import random

def main():
    voti = [random.randint(2, 10) for i in range(10)] #crea una lista di 10 numeri casuali
    print(f"Voti: {voti}")
    m, n = funzioni.media(voti)
    print(m)

if __name__ == "__main__":
    main()