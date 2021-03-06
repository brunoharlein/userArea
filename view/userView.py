import hashlib
import os
import time
from getpass import getpass

from model.userModel import userModel

class userView():
    """View or controller taking care of all the logic related to user in the app.
    Allow to login, create and show a user. When showing a user, allow to update or delete the user
        Vue ou contrôleur prenant en charge toute la logique liée à l'utilisateur dans l'application.
        Permet de se connecter, de créer et d'afficher un utilisateur.
        Lors de l'affichage d'un utilisateur, autorisez la mise à jour ou la suppression de l'utilisateur"""

    def __init__(self):
        pass

    def login(self):
        """Ask for pseudo and password and check that credentials are valid
        If so call the profil method
           Demandez un pseudo et un mot de passe et vérifiez que les informations d'identification sont valides
         Si c'est le cas, appelez la méthode de profil"""

        # Instanciate the model to operate queries on users table
        # Instancier le modèle pour exécuter des requêtes sur la table des utilisateurs
        model = userModel()
        # Ask the credentials
        # Demandez les informations d'identification
        print("Votre pseudo utilisateur : ")
        pseudo = input(": ")
        print("Votre mot de passe")
        password = getpass(": ")
        # Look for a user based on a pseudo
        # Recherchez un utilisateur basé sur un pseudo
        user = model.check_pseudo(pseudo)
        # If the pseudo exists and the password are the same
        # Si le pseudo existe et le mot de passe sont les mêmes
        # Show the profil page, otherwise go bakc to main file
        # Afficher la page de profil, sinon revenir au fichier principal
        if user and self.verifiy_password(user, password):
            self.profil(user)
        else:
            print("Identifiants incorrects")
        time.sleep(3)

    def profil(self, user):
        """Display information about a given user from the database
        Let the user delete or update his profile
           Afficher des informations sur un utilisateur donné à partir de la base de données
           Laisser l'utilisateur supprimer ou mettre à jour son profil"""

        # Instanciate the model to operate queries on users table
        # Instancier le modèle pour exécuter des requêtes sur la table des utilisateurs
        model = userModel()
        # Show user
        print("Bonjour voici nos informations sur vous : ")
        print(
            "nom : {}\nprénom : {}\nage : {}\npseudo : {}\nemail : {}\n"
            .format(user['name'], user['firstname'], user['age'], user['pseudo'], user['email'])
        )
        # Get action from user
        # Obtenir une action de l'utilisateur
        print("Actions possible s: supprimer son compte, m: modifier une information, tapez entrée pour revenir à l'accueil")
        action = input(": ")
        # Call the right method based on the action
        # Appeler la bonne méthode en fonction de l'action
        if action == "s":
            model.delete_user(user)
        elif action == "m":
            # Ask which column to change and the new value to set
            # Demandez quelle colonne modifier et quelle nouvelle valeur définir
            column = input("Que voulez-vous modifier ? (name, firstname, email, age, password, pseudo) : ")
            value = input("Nouvelle valeur : ")
            # If the user changes the password with crypt it
            # Si l'utilisateur change le mot de passe avec crypt il
            if column == "password":
                value = hashlib.sha256(bytes(value, encoding="ascii")).hexdigest()
            # Update the dictionnary representing the user
            # Mettre à jour le dictionnaire représentant l'utilisateur
            user[column] = value
            # Update the database
            # Mettre à jour la base de données
            model.update_user(user)

    def new(self):
        """Ask information to create a new user in database"""
        # Instanciate the model to operate queries on users table
        # Instancier le modèle pour exécuter des requêtes sur la table des utilisateurs
        model = userModel()
        # Store the translations for the names of the columns
        # Stockez les traductions pour les noms des colonnes
        infos_text = ["nom", "prénom", "pseudo", "email", "âge", "mot de passe"]
        # Store user's values
        # Stocker les valeurs de l'utilisateur
        user = []
        # Show an input for each column and add the value to user
        # Afficher une entrée pour chaque colonne et ajouter la valeur à l'utilisateur
        for text in infos_text:
            user.append(input(text + " : "))
        # Crypt the password
        user[-1] = hashlib.sha256(bytes(user[-1], encoding="ascii")).hexdigest()
        # Check that both pseudo and email are available
        # Vérifiez que les pseudo et les e-mails sont disponibles
        while model.check_pseudo(user[2]):
            user[2] = input("Ce pseudo est déjà pris : ")
        while model.check_email(user[3]):
            user[3] = input("Cette adresse mail est déjà prise : ")
        os.system('cls' if os.name == 'nt' else 'clear')
        # Add the user in the database
        # Ajouter l'utilisateur dans la base de données
        if model.add_user(user):
            print("Votre compte a été créé, vous n'avez plus qu'à vous connecter")
        time.sleep(3)

    def verifiy_password(self, user, password):
        """Check that a given password matches a user's one"""
        # Hash the given password
        # Hachage du mot de passe donné
        password = hashlib.sha256(bytes(password, encoding="ascii")).hexdigest()
        if password == user['password']:
            return True
        return False






