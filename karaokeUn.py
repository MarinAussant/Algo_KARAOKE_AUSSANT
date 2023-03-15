class Player :

    def __init__(self,nom):
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


########## TESTS PLAYER ##########

def testsClassPlayer() :

    joueurUn = Player("Jean")
    joueurDeux = Player("Alice")

    print("Test Ajout_Score et Score_Total :")
    joueurUn.ajouterScore(0,60)
    joueurUn.ajouterScore(1,82)
    joueurUn.ajouterScore(2,96)
    joueurUn.ajouterScore(3,55)
    joueurUn.ajouterScore(4,74)
    joueurUn.ajouterScore(1,10)
    joueurUn.ajouterScore(3,51)
    joueurUn.ajouterScore(0,90)

    joueurDeux.ajouterScore(0,32)
    joueurDeux.ajouterScore(0,70)
    joueurDeux.ajouterScore(1,83)
    joueurDeux.ajouterScore(2,78)
    joueurDeux.ajouterScore(1,76)
    joueurDeux.ajouterScore(2,90)

    print("Good.") if joueurUn.scoreTotal() == 397 and joueurDeux.scoreTotal() == 243 else print("Not Good.")
    print(" ")

    print("Test Moyenne :")

    print("Good.") if joueurUn.moyenne() == 79.4 and joueurDeux.moyenne() == 81 else print("Not Good.")
    print(" ")

    print("Test Meilleure_Musique :")

    print("Good.") if joueurUn.meilleureMusique() == 2 and joueurDeux.meilleureMusique() == 2 else print("Not Good.")
    print(" ")

    print("Test Pire_Musique :")

    print("Good.") if joueurUn.pireMusique() == 3 and joueurDeux.pireMusique() == 0 else print("Not Good.")
    print(" ")

    print("Test Afficher_Score :")

    joueurUn.afficherScores()
    print(" ")
    joueurDeux.afficherScores()

testsClassPlayer()


