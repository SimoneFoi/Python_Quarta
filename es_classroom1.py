#Data una lista di interi, scrivere una funzione che restituisca due liste separate: una con i numeri pari e una con i dispari.
#numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]

numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]
l1 = []
l2 = []
for i in numeri:
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)
print(l1, l2)