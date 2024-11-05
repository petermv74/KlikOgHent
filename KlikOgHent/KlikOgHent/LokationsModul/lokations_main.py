from lokationsdatamodel import LokationsDatamodel
from DataModel import Ordre
from lokations_presenter import LokationsPresenter
from lokations_view import LokationsView

class LokationsMain:
    def __init__(self):
        model = LokationsDatamodel()
        view = LokationsView()
        presenter = LokationsPresenter()
        
    def addOrdre(self):
        self.model.addOrdre("peter@moeller-vestfal")
        