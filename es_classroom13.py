#Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: 
# (a) calcolare la media di una materia, 
# (b) trovare la materia con media più alta, 
# (c) aggiungere un voto a una materia.

def media_materia(voti_materie, materia):
    if materia in voti_materie:
        somma = 0
        cont = 0
        for i in voti_materie[materia]:
            somma += i
            cont += 1
        return somma / cont
    return 0

def media_piu_alta(voti_materie):
    max = 0
    for i in voti_materie:
        ris = media_materia(voti_materie, i)
        if ris > max:
            max = ris
    if ris == max:
        print(f"{i}: {max},", end= " ")
    print()
    
def add_voto_materia(voti_materia, voto, materia_to_add):
    if materia_to_add in voti_materia:
        voti_materia[materia_to_add].append(voto)

def main():
    voti_materie = {
    "Matematica": [6, 7, 5, 8, 7],
    "Italiano": [7, 8, 7, 6],
    "Inglese": [8, 8, 9, 7, 8],
    "Informatica": [9, 8, 9, 10, 8]
    }

    materia = input("Materia di cui vuoi calcolare la media: ")
    print(f"{materia}: ", media_materia(voti_materie, materia))

    print("Materia/e con media più alta/e: ")
    print(media_piu_alta(voti_materie))

    voto = int(input("Inserisci il voto che vuoi aggiungere: "))
    materia_to_add = input("Materia a cui vuoi aggiungere il voto: ")
    print(voti_materie[materia_to_add])
    add_voto_materia(voti_materie, voto, materia_to_add)
    print(voti_materie[materia_to_add])

if __name__ == "__main__":
    main()