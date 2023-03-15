ids = 0


# Classe Joueur
class Player :

    def __init__(self,nom, id):
        self.id = id
        self.nom = nom
        self.listScores = [0,0,0,0,0]

    # Return le score total de toutes les musiques
    def scoreTotal(self) :
        total = 0
        for score in self.listScores :
            total += score

        return total

    # Return la moyenne des scores des musiques déjà enregistrée
    def moyenne(self) :
        nbScoreEnregistre = 0
        for score in self.listScores :
            if score != 0 :
                nbScoreEnregistre += 1  

        return self.scoreTotal()/nbScoreEnregistre

    # Return le numéro de la musique déjà enregistrée qui a le meilleur score
    def meilleureMusique(self) :
        numMusique = -1
        meilleurScore = 0
        for i in range(len(self.listScores)) :
            if self.listScores[i] > meilleurScore :
                numMusique = i
                meilleurScore = self.listScores[i]

        return numMusique

    # Return le numéro de la musique déjà enregistrée qui a le pire score
    def pireMusique(self) :
        numMusique = 0
        pireScore = 100
        for i in range(len(self.listScores)) :
            if self.listScores[i] < pireScore and self.listScores[i] > 0 :
                numMusique = i
                pireScore = self.listScores[i]

        return numMusique

    # Affiche la liste des chansons avec leur score
    def afficherScores(self) :
        print("Scores "+self.nom+" :")
        for i in range(len(self.listScores)) :
            print(str(i) + " : " + str(self.listScores[i]))

    # Ajoute un score à la liste du joueur si le score dépasse 50 et s'il est plus grand que le précédent
    def ajouterScore(self, numMusique, score) :
        if self.listScores[numMusique] < score and score >= 50 :
            self.listScores[numMusique] = score

    def getId(self) :
        return self.id

    def infoJoueur(self) :
        print("------Infos "+ self.nom +"------")
        print("Nom : "+ self.nom)
        print("Id : "+ str(self.id))
        print("Score total :"+ str(self.scoreTotal()))
        print("Moyenne : "+str(self.moyenne()))
        print("----------------------")

    def getScoreList(self):
        return self.listScores


# Classe Karaoke
class Karaoke :

    def __init__(self, player, nbChanson):
        self.listJoueurs = []
        self.listJoueurs.append(player)
        self.listChansons = []
        for i in range(nbChanson) :
            self.listChansons.append(0)

    def ajouterJoueur(self,joueur) :
        self.listJoueurs.append(joueur)

    def supprimerJoueur(self,idJoueur) :
        for i in range(self.listJoueurs):
            if self.listJoueurs[i].getId() == idJoueur and len(self.listJoueurs) > 0 :
                self.listJoueurs.remove(self.listJoueurs[i])

    def meilleurScoreChanson(self, numMusique) :
        meilleurScore = 0
        for joueur in self.listJoueurs :
            if joueur.getScoreList()[numMusique] > meilleurScore :
                meilleurScore = joueur.getScoreList()[numMusique]
        
        return meilleurScore

    def meilleurScoreAllChansons(self) :
        meilleurScore = 0

        for numMusique in range(self.listChansons):
            for joueur in self.listJoueurs :
                if joueur.getScoreList()[numMusique] > meilleurScore :
                    meilleurScore = joueur.getScoreList()[numMusique]
        
        return meilleurScore

    def meileurJoueurScoreTotal(self):
        meilleurScoreTotalPlayer = 0
        meilleurJoueur = 0
        for joueur in self.listJoueurs :
            if joueur.scoreTotal() > meilleurScoreTotalPlayer :  
                meilleurScoreTotalPlayer = joueur.scoreTotal()
                meilleurJoueur = joueur
        
        return joueur

    def meilleurJoueurMoyenne(self):
        meilleurMoyennePlayer = 0
        meilleurJoueur = 0
        for joueur in self.listJoueurs :
            if joueur.moyenne() > meilleurMoyennePlayer :  
                meilleurMoyennePlayer = joueur.moyenne()
                meilleurJoueur = joueur
        
        return joueur

       
########## TESTS KARAOKE + PLAYER ##########
# ça marche normalement 