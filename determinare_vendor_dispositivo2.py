def main():
    file = open(".\mac-vendors-export.csv", "r", encoding= 'utf-8')
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []
    date = []  
    for riga in righe[1:]:
        campi = riga.split(",")
        mac_address.append(campi[0])
        vendor.append(campi[1])
        date.append(campi[4])

    mac = input("Inserisci il MAC address: ").upper()
    for m, v, d in zip(mac_address, vendor, date):
        if m[0:8] == mac[0:8]:
            print(f"Il produttore è {v}, data {d}")

if __name__ == "__main__":
    main()