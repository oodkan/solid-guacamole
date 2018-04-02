import numpy as np


class Jeu(object):
    def __init__(self, verb=False):
        self.joueurs = []
        self.tour = 0
        self.maxTarrot = 21
        self.nombreDeJoueurs = 0
        self.dernierAnnonce = None
        self.numero_manche = 0
        self.verbose = verb
        self.viesDepart = 10
        self.viesJoueurs = []

    # Start of user code -> properties/constructors for Jeu class
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        self.viesJoueurs.append(self.viesDepart)
        self.nombreDeJoueurs += 1
        self.print_v("Joueur supplémentaire. " + str(self.nombreDeJoueurs) + " joueurs en jeu")

    def initialiserJeu(self):
        self.numero_manche = int(self.maxTarrot / self.nombreDeJoueurs)
        self.print_v("Jeu en " + str(self.numero_manche) + " manches")

    # End of user code
    def mancheClassique(self):
        if self.numero_manche <= 1:
            raise NameError('mancheClassique non compatible avec 1 ou moins')

        self.print_v("Depart manche " + str(self.numero_manche))
        # DISTRIBUTION DES CARTES
        cartes = self.distribuerCartes(self.numero_manche)
        self.print_v(str(cartes))
        for j in range(self.nombreDeJoueurs):
            self.joueurs[j].recevoirCartes(cartes[j])

        # ANNONCE
        ordreAnnonces = self.creerOrdreAnnonces()
        annonces = []
        for j in ordreAnnonces:
            annonces.append(self.joueurs[j].annoncerManche(annonces))
        annonces = [annonces[ordreAnnonces[i]] for i in range(self.nombreDeJoueurs)]  # Reorganise
        self.print_v("Annonces " + str(annonces))
        # TODO checker annonces

        # DEPART DU JEU
        ordreJeu = self.creerOrdreJeu((self.dernierAnnonce + 1) % self.nombreDeJoueurs)
        defausse = []
        score = [0] * self.nombreDeJoueurs

        for m in range(self.numero_manche):

            cartesJouees = [0] * self.nombreDeJoueurs

            for j in ordreJeu:
                carte = self.joueurs[j].jouerTour(cartesJouees, defausse)
                cartesJouees[j] = carte
                # TODO check si carte joue est valide
            self.print_v("Cartes jouees " + str(cartesJouees))
            gagnant_numero = cartesJouees.index(max(cartesJouees))
            score[gagnant_numero] += 1
            defausse.append(cartesJouees)
            ordreJeu = self.creerOrdreJeu(gagnant_numero)

        # PERTE DES VIES
        for j in range(self.nombreDeJoueurs):
            self.joueurs[j].perdreVie(abs(score[j] - annonces[j]))
            self.viesJoueurs[j] -= abs(score[j] - annonces[j])
        self.print_v("Score" + str(score))
        self.numero_manche -= 1

    def jouerPartie(self):
        self.initialiserJeu()
        while self.numero_manche > 1:
            self.mancheClassique()
        self.derniereManche()
        self.print_v("Jeu terminé")
        self.print_v("Vies restantes" + str(self.viesJoueurs))

    def print_v(self, texte):
        if self.verbose:
            print(texte)

    def derniereManche(self):
        self.print_v("Dernière manche")
        cartes = self.distribuerCartes(self.numero_manche).tolist()
        self.print_v(str(cartes))
        # DEPART DU JEU
        ordreJeu = self.creerOrdreJeu((self.dernierAnnonce + 1) % self.nombreDeJoueurs)

        annonces = [0] * self.nombreDeJoueurs
        for j in ordreJeu:
            cartesVisibles = list(cartes)  # Pas de copie en ref
            cartesVisibles.remove(cartesVisibles[j])
            self.print_v(str(cartesVisibles))
            annonces[j] = self.joueurs[j].jouerDernierTour(cartesVisibles)  # +1 pour max, 0 pour milieu et -1 pour min
            # TODO check si carte joue est valide
        self.print_v("Annonces " + str(annonces))
        # Convertir les cartes vers la codification annonce
        cartesClassees = [0] * self.nombreDeJoueurs
        cartesClassees[cartes.index(max(cartes))] = 1
        cartesClassees[cartes.index(min(cartes))] = -1

        score = []
        # PERTE DES VIES
        for j in range(self.nombreDeJoueurs):
            score.append(abs(cartesClassees[j] - annonces[j]))
            self.joueurs[j].perdreVie(score[-1])
        self.print_v("Score" + str(score))
        self.numero_manche -= 1

    # Start of user code -> methods for Jeu class

    def distribuerCartes(self, nombredeCartes):
        if nombredeCartes == 1:
            return np.random.choice(self.maxTarrot, self.nombreDeJoueurs, replace=False)
        else:
            return np.random.choice(self.maxTarrot, (self.nombreDeJoueurs, nombredeCartes), replace=False)

    def creerOrdreJeu(self, depart):
        ordreJeu = []
        for j in range(self.nombreDeJoueurs):
            ordreJeu.append((depart + j) % self.nombreDeJoueurs)
        return ordreJeu

    def creerOrdreAnnonces(self):
        if self.dernierAnnonce is None:
            self.dernierAnnonce = np.random.randint(low=0, high=self.nombreDeJoueurs) - 1
        else:
            self.dernierAnnonce = (self.dernierAnnonce + 1) % self.nombreDeJoueurs
        ordreAnnonces = self.creerOrdreJeu(self.dernierAnnonce)
        return ordreAnnonces
    # End of user code
