#ci sono tanti modi di fare il for in Python
#vediamo il primo modo, detto C-style (solitamente da evitare)

for i in range(4):    #range è una funzione python che prende un numero
    print(i)          # = for i in range(0,4) --> stampa dal primo incluso al quarto escluso
for i in range (8, 1, -2):        #range([START], STOP, [GAP])
    print(i)
#START e GAP sono parametri facoltativi, quindi nella documentazione comparirebbe tra parentesi quadre