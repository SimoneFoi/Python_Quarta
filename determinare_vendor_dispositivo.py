#scrivere un programma python che dato i primi 3 byte del MAC Address, scorre il file e determina il vendor
#es: D4:1B:81

def main():
    file = open(".\mac-vendors-export.csv", "r", encoding= 'utf-8')
    righe = file.readlines()
    file.close()
    #MAC_ADDRESS = input(f"Inserisci il tuo indirizzo MAC: ")
    MAC_ADDRESS = "D4:1B:81"
    for k in righe:
        if k[0:8] == MAC_ADDRESS:
            print(k)

if __name__ == "__main__":
    main()