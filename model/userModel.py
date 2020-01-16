from .connection import connection

class userModel():
    """Class to perform all queries related to the users table in the database
        Classe pour effectuer toutes les requêtes liées à la table des utilisateurs dans la base de données"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        # Créer une instance de la classe de connexion pour accéder à la base de données
        self.db = connection()
