class IPAddress():
    def __init__(self, ip, sm):
        #ip e sm sono stringhe
        self.ip = ip
        self.sm = sm

    def networkAddress(self):
        #restituisce l'indirizzo di rete
        ip = self.ip.split(".")
        sm = self.sm.split(".")
        risultato = ""
        for i in range(4):
            if sm[i] == "255":            # se la subnet è 255, il numero resta uguale
                risultato = risultato + ip[i]
            else:                         # se la subnet è 0, il numero diventa 0
                risultato = risultato + "0"
            if i < 3:
                risultato = risultato + "."
        return risultato

    def broadcastAddress(self):
        ip = self.ip.split(".")
        sm = self.sm.split(".")

        risultato = ""
        for i in range(4):
            # se la subnet è 255, il numero resta uguale
            if sm[i] == "255":
                risultato = risultato + ip[i]
            else:
                # se la subnet è 0, il numero diventa 255
                risultato = risultato + "255"
            if i < 3:
                risultato = risultato + "."
        return risultato
        #devo prendere la sm e riscriverla finchè non trovo uno 0
        #poi da lì devo scrivere 32 - len(nuova_stringa) 1

    def hostNumer(self):
        #restituisce il numero di host
        #devo fare 2^(32-n_1) - 2
        sm = self.sm.split(".")
        host = 1
        for i in range(4):
            if sm[i] == "0":
                host = host * 256
        return host - 2

def main():
    ip1 = IPAddress("192.168.10.1", "255.255.255.0")
    print("Indirizzo di rete:      ", ip1.networkAddress())
    print("Indirizzo di broadcast: ", ip1.broadcastAddress())
    print("Numero di host:         ", ip1.hostNumer())

if __name__ == "__main__":
    main()