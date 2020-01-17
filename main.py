import os
import time
from view.userView import userView

# Main file acting like a routing system
# Call the right method from the view, depending on user input
# Fichier principal agissant comme un système de routage
# Appelez la bonne méthode à partir de la vue, en fonction de l'entrée de l'utilisateur

# Simple intro for the app
os.system('cls' if os.name == 'nt' else 'clear')
print("BONJOUR ET BIENVENUE SUR CET ESPACE PERSONNEL")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Un exercice pour apprendre à gérer les mots de passe en python")
time.sleep(2)

# The action the user wants to do, by default nothing
# L'action que l'utilisateur veut faire, par défaut rien
action = ""

# while the user does not chose to leave the program
# alors que l'utilisateur n'a pas choisi de quitter le programme
while action != 'q':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Que voulez-vous faire ? (c: connexion, n: création d'un compte, q: quitter)")
    action = input(": ")
    os.system('cls' if os.name == 'nt' else 'clear')
    # Display the right view method according to user command
    # Afficher la bonne méthode d'affichage selon la commande utilisateur
    view = userView()
    if action == "n":
        view.new()
    elif action == "c":
        view.login()

# Leave the program
exit()
