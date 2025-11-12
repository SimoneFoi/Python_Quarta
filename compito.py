#Cra un programma in python che chiede all'utente il nome e lo stampa sempre con l'iniziale maiuscola

nome = input("Nome: ")                      #chiedo nome
nome = nome.lower()                         #tutto minuscolo
nome = nome[0].upper() + nome[1:len(nome)]  #prima maiuscola, slicing che tiene le altre
#1:len(nome) = 1:
print(nome)                                 #stampo