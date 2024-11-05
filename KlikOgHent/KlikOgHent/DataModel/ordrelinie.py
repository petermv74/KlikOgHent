class Ordrelinie:
    #initializer function, definerer også classen
    def __init__(self, varenummer ,antal_bestilt, antal_modtaget):
        self.varenummer = varenummer
        self.antal_bestilt = antal_bestilt
        self.antal_modtaget = 0
        
    def modtageVare(self, antal):
        self.antal_modtaget += antal
        return self.antal_modtaget >= self.antal_bestilt
