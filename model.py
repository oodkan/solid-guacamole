from Jeu import Jeu
from JoueurAlea import *

# Let's play

jeu = Jeu(True)  # type: Jeu
jeu.ajouterJoueur(JoueurAlea())
jeu.ajouterJoueur(JoueurAlea())
jeu.ajouterJoueur(JoueurAlea())
jeu.jouerPartie()
