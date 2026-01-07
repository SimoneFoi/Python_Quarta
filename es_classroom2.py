#Scrivere una funzione che trovi il secondo valore più grande in una lista di numeri (senza usare sort o sorted).

valori = [45, 12, 78, 34, 67, 23, 89, 56]

max1 = valori[0]
max2 = valori[1]

for i in valori:
    if i > max1:
        max2 = max1
        max1 = i
        
print(valori)
print(max2)