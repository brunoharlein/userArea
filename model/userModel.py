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

    def add_user(self, user):
        """Given a list with values related to the user entitiy store a new entry in database
        The query is in a try bloc to display an information message to the user if insert fails
            Étant donné une liste avec des valeurs liées à l'entité utilisateur,
            stocker une nouvelle entrée dans la base de données
        La requête est dans un bloc try pour afficher un message d'information à l'utilisateur si l'insertion échoue"""
        try:
            self.db.initialize_connection()
            self.db.cursor.execute("""
                INSERT INTO users (name, firstname, pseudo, email, age, password)
                VALUES (%s, %s, %s, %s, %s, %s)
                ,
                (user[0], user[1], user[2], user[3], user[4], user[5])
            """)
            self.db.connection.commit()
            return True
        except Exception as e:
            print("Il semble que nous n'ayons pas pu vous enregistrer, merci d'essayer à nouveau")
            return False
        finally:
            self.db.close_connection()

    def delete_user(self, user):
        """Delete a user by its id from the database
        The query is in a try block to display an error message if query fails
        Supprimer un utilisateur par son identifiant de la base de données
        La requête est dans un bloc try pour afficher un message d'erreur si la requête échoue"""
        try:
            self.db.initialize_connection()
            self.db.cursor.execute("DELETE FROM users WHERE id = %s", (user['id'],))
            self.db.connection.commit()
            return True
        except Exception as e:
            print("Un problème est survenu, nous n'avons pas pu supprimer votre compte")
            return False
        finally:
            self.db.close_connection()



