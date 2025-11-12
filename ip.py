ip = input("Inserisci un indirizzo ip: ")
ottetti_str = ip.split(".")            #split() è un metodo delle stringhe che suddivide una stringa cercando il carattere separatore passato
print(ottetti_str)

ottetti = []
for s in ottetti_str:
    ottetti.append(int(s))

print(ottetti)
print(bin(ottetti[0]))                  #stampa il binario
print(bin(ottetti[1]))                  #stampa il binario
print(bin(ottetti[2]))                  #stampa il binario
print(bin(ottetti[3]))                  #stampa il binario