
       

"""module casino contenant la fonction table"""

import os 

from math import ceil



# Le joueur somme sur un numéro compris entre 0 et 49 (50 numéros en tout). En choisissant son numéro, il y dépose la somme qu'il souhaite sommer.

gain = 1000
continuer_partie = True
print("Vous vous installez à la table avec", gain, "$.")

while continuer_partie: # Tant qu'on doit continuer la partie
    # on demande à l'utilisateur de saisir le nombre sur
    # lequel il va sommer
    num = -1
    while num < 0 or num > 49:
        num = input("Tapez le nombre sur lequel vous voulez sommer (entre 0 et 49) : ")
        # On convertit le nombre misé
        try:
            num = int(num)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            num = -1
            continue
        if num < 0:
            print("Ce nombre est négatif")
        if num > 49:
            print("Ce nombre est supérieur à 49")

    somme = 0
    # On attend que l'utilisateur fournisse une somme
    while somme <= 0 or somme > gain:
        somme = input("Saisissez une somme à sommer : ")
        try:
            somme = int(somme)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            somme = -1
            continue
        if somme <= 0:
            print("La somme saisie est négative ou nulle.")
        if somme > gain:
            print("Vous ne pouvez sommer autant, vous n'avez que", gain, "$")
        
    gain = gain - somme
    import random
	# roulette = 1
    roulette = random.randint(0, 49)
    
    print("Le numero que vous avez choisi est le ")
    print(num)
    print("la somme que vous avez choisi est :")
    print(somme)
    print("la roulette s'est arrêté sur le :")
    print(roulette)

    if num == roulette :
	    print("C'est gagné !")
	    gain = gain + (somme * 3)
	    print("Vos gains sont maintenant de :")
	    print(gain)
    else:
	    print("c'est perdu !")
	    print("Vos gains sont maintenant de :")
	    print(gain)

    if num%2 == 0:
	    pairNum = 1
    else:
	    pairNum = 0

    if roulette%2 == 0:
	    pairRoulette = 1
    else:
	    pairRoulette = 0

    if pairRoulette == pairNum:
	    print("Vous avez eu la même couleur !")
	    gain = gain + (somme / 2)
	    print("Vos gains sont maintenant de :")
	    print(gain)
    else:
	    print("Vous n'êtes pas tombé sur la bonne couleur")
	    print("Vos gains sont maintenant de :")
	    print(gain)

    if gain <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", gain, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False

# On met le programme en pause pour éviter qu'il ne se referme (Windows)

os.system("pause")