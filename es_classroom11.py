#Una lista contiene dizionari con chiavi nome, categoria, prezzo. Scrivere una funzione che restituisca solo i prodotti di una 
# certa categoria con prezzo inferiore a un valore dato.

def categoria_con_prezzo_inferiore(prodotti, max, categoria):
    lis = []
    for i in prodotti:
        if i["categoria"] == categoria and i["prezzo"] < max:
            lis.append(i)
    return lis

def main():
    prodotti = [
    {"nome": "Laptop", "categoria": "elettronica", "prezzo": 899.99},
    {"nome": "Mouse", "categoria": "elettronica", "prezzo": 29.99},
    {"nome": "Scrivania", "categoria": "arredamento", "prezzo": 199.99},
    {"nome": "Tastiera", "categoria": "elettronica", "prezzo": 79.99},
    {"nome": "Sedia", "categoria": "arredamento", "prezzo": 149.99},
    {"nome": "Monitor", "categoria": "elettronica", "prezzo": 349.99}
    ]
    max = int(input("Inserisci il prezzo di cui vuoi cercare i valori inferiori: "))
    categoria = input("Inserisci categoria che stai cercando: ")
    print(categoria_con_prezzo_inferiore(prodotti, max, categoria))

if __name__ == "__main__":
    main()

