class Kunde:
    def __init__(self, email_adresse):
        self.email_adresse = email_adresse
        
    def meldOrdreKlarTilAfhentning(self):
        print("Email til " + self.email_adresse + " om at ordre kan afhentes")