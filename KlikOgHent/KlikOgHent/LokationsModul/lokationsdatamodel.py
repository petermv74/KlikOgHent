from DataModel import Ordre


class LokationsDatamodel:
    #initializer function, definerer også classen
    def __init__(self):
        self.ordre = {}
        
    def addOrdre(self, email):
        self.ordre.append(email, Ordre(email))
