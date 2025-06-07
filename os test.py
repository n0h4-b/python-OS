def menu():
    print("\033c", end="")
    print("bureau:\n1.editeur de texte\n2.on verra\n3.on verra\n4.on verra\n5.on verra")
    choix = input()
    if choix == "1":
        editeurdetexte()
    elif choix == "2":
        print("fichiers texte")
        lecteurtxt()
    elif choix == "3":
        print("...")
    elif choix == "4":
        print("...")
    elif choix == "5":
        print("...")

# Dictionnaire pour stocker plusieurs textes nommés
textes_dict = {}

def editeurdetexte():
    global textes_dict
    print("\033c", end="")
    commande_fichiers = input("pour créer un texte, tapez 'txt'\npour l'afficher tapez 'txtopen'\npour quitter tapez 'exit': ")
    if commande_fichiers == "txt":
        nom = input("Nom du texte : ")
        contenu = input("Entrez votre texte : ")
        textes_dict[nom] = contenu
        print(f"Texte '{nom}' enregistré !")
    elif commande_fichiers == "txtopen":
        nom = input("Nom du texte à afficher : ")
        print("\033c", end="")
        if nom in textes_dict:
            print(f"Texte '{nom}' :\n{textes_dict[nom]}")
        else:
            print("Aucun texte enregistré sous ce nom.")
    elif commande_fichiers == "exit":
        return menu()
    else:
        print("Commande pas encore créée !!!")
    input("Appuyez sur Entrée pour continuer...")
    return editeurdetexte()

def demarage():
    print("entrez le mot de passe:")
    test_mdp = 3
    test_entrée = 0
    while test_entrée < test_mdp:
        mot_de_passe = input()
        if mot_de_passe == "1234":
            print("Mot de passe correct")
            menu()
            return
        else:
            print("Mot de passe incorrect")
            print("Acces refuse")
            test_entrée += 1

    if test_entrée >= test_mdp:
        print("Trop d'essais infructueux")
        print("Acces refuse")
        return
editeurdetexte()
#...