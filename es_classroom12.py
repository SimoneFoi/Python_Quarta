#Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti. #Scrivere funzioni per: 
# (a) contare le presenze di uno studente, 
# (b) trovare chi ha più presenze, 
# (c) trovare chi era presente in una certa data.

def conta_presenze(presenze, studente):
    if studente in presenze:
        return len(presenze[studente])

def record_presente(presenze):
    max = 0
    for i in presenze:
        if len(presenze[i]) > max:
            max = len(presenze[i])
    for i in presenze:
        if len(presenze[i]) == max:
            print(f"{i},", end= " ")
    print()

def presente_in_data(presenze, data):
    for i in presenze:
        for idx in presenze[i]:
            if idx == data:
                print(f"{i},", end= " ")
    print()

def main():
    presenze = {
    "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
    "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
    "Luca": ["2024-01-10", "2024-01-11"],
    "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }

    studente = input("Studente di cui vuoi calcolare le presenze: ")
    print(conta_presenze(presenze, studente))
    print("Studente con più presenze: ")
    record_presente(presenze)
    data = input("Data in cui vuoi scoprire chi era presente: ")
    presente_in_data(presenze, data)

if __name__ == "__main__":
    main()
