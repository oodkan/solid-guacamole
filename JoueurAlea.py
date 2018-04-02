import numpy.random as rnd

from Joueur import *


class JoueurAlea(Joueur):
    def jouerTour(self, cartesJouee, defausse):
        carte = rnd.choice(self.cartesEnMain)
        self.cartesEnMain.remove(carte)
        return carte

    def jouerDernierTour(self, cartesVisibles):
        return 0

    def annoncerManche(self, annoncesPrecedentes):
        if sum(annoncesPrecedentes) == (self.tour - 1):
            annonce = 0
        else:
            annonce = 1
        return annonce
