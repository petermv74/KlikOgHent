from ordrelinie import Ordrelinie
from kunde import Kunde

class Ordre:
    #initializer function, definerer også classen
    def __init__(self, kunde_email):
        self.kunde = Kunde(kunde_email)
        self.ordrelinier = { }
        self.faerdige_ordrelinier = 0
        self.udleveret = False
        
    def addOrdrelinie(self, vare_nummer, antal):
        self.ordrelinier.update({vare_nummer, Ordrelinie(vare_nummer, antal)})

    def modtageVarer(self, varenummer, antal):
        ordrelinie = self.ordrelinier.get(varenummer)
        ordrelinie_faerdig = ordrelinie.modtageVare(antal)
        if (ordrelinie_faerdig):
            self.faerdige_ordrelinier += 1
        if (self.faerdige_ordrelinier == len(self.ordrelinier)):
            self.kunde.meldOrdreKlarTilAfhentning()