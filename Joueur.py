class Joueur(object):
    def __init__(self):
        self.cartesEnMain = 0
        self.vies = 0
        self.annonce = 0

        # Start of user code -> properties/constructors for Joueur class

    # End of user code
    def jouerTour(self, cartesJouee, defausse):
        # Start of user code protected zone for jouerTour function body
        raise NotImplementedError
        # End of user code

    def annoncerManche(self, annoncesPrecedentes):
        # Start of user code protected zone for annoncerManche function body
        raise NotImplementedError
        # End of user code

    def jouerDernierTour(self, cartesVisibles):
        # Start of user code protected zone for dernierTour function body
        raise NotImplementedError
        # End of user code

    def recevoirCartes(self, cartes):
        self.cartesEnMain = list(cartes)

        self.tour = len(cartes)

    # Start of user code -> methods for Joueur class
    def perdreVie(self, viesperdues):
        self.vies = max(self.vies - viesperdues, 0)
    # End of user code
