from .connection import connection

class userModel():
    """Class to perform all queries related to the users table in the database
        Classe pour effectuer toutes les requêtes liées à la table des utilisateurs dans la base de données"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        # Créer une instance de la classe de connexion pour accéder à la base de données
        self.db = connection()

    def check_pseudo(self, pseudo):
        """Given a pseudo return the corresponding user from the database
            Étant donné un pseudo retour, l'utilisateur correspondant de la base de données"""
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM users WHERE pseudo = %s", (pseudo,))
        # Use fetchone to avoid having a list as a result
        # Utilisez fetchone pour éviter d'avoir une liste à la suite
        result = self.db.cursor.fetchone()
        self.db.close_connection()
        return result

    def check_email(self, email):
        """Given an email, check if it already exists and return it
            Étant donné un e-mail, vérifiez s'il existe déjà et retournez-le"""
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
        result = self.db.cursor.fetchall()
        self.db.close_connection()
        return result

