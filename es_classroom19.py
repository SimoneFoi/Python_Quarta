#Leggere un file e scrivere su un nuovo file solo le righe che contengono una certa parola chiave.

file = open("testo_classroom4.txt", "r", encoding= "utf8")
righe = file.readlines()
file.close()

parola = input("Inserisci parola da ricercare nel file: ")

file_output = open("testo_classroom5.txt", "w", encoding= "utf8")
for i in righe:
    if parola in i:
        file_output.write(i)
file_output.close()