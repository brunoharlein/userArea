un espace utilisateur
Dans cet exercice, vous allez simuler le fonctionnement d’un espace privé auquel les utilisateurs accèdent grâce à leur compte personnel protégé par mot de passe. Vous allez ainsi travailler les requêtes en bases de données, mais aussi la gestion des mots de passe.
L’application présentera les fonctionnalités suivantes :
- Une page d’accueil, qui permet à l’utilisateur de choisir entre se connecter avec un compte existant ou se créer un compte
- Pour se créer un compte l’utilisateur a accès à une série de prompts demandant les informations nécessaires. Une fois les informations rentrées, celles-ci sont enregistrées en base de données.
- Si le pseudo ou le mail rentrés par l’utilisateur sont déjà pris on demande à l’utilisateur d’en entrer un nouveau
- Pour se connecter l’utilisateur doit rentrer le pseudo et le mot de passe choisis lors de la création du compte. Si les identifiants sont corrects, l’utilisateur accède alors à la page de son profil, autrement on lui affiche un message d’erreur.
- Sur sa page de profil l’utilisateur peut choisir de supprimer son compte, ses informations sont alors effacées de la base de données. Il peut également choisir de mettre à jour une information en indiquant la colonne à modifier et sa nouvelle valeur
- L’utilisateur peut quitter l’application à tout moment en tapant une commande de votre choix
Spécifications techniques :
- Les mots de passe sont cryptés en base de données, autrement-dit ils ne sont pas stockés en clair, ils sont illisibles en l’état par un être humain
Cette base de données ne contiendra qu’une seule table : users, dont voici la structure.
id (integer, clé primaire, non nul)
name (varchar maximum 50 caractères, non nul) firstname (varchar maximum 50 caractères, non nul) pseudo (varchar maximum 50 caractères, unique, non nul) email (varchar maximum 250 caractères, unique, non nul) age (integer, non nul)
password (varchar de minimum 64 caractères, non nul)
NB : nous ne nous intéressons pas ici à la notion de salage de mot de passe mais il s’agit d’un élément très important de la sécurité d’une application. Vous pouvez lire cet article pour en savoir plus : https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/
Si vous souhaitez aller plus loin, vous pouvez également rajouter des vérifications de sécurité. Par exemple :
- S’assurer que les chaînes de caractères pour le nom et le prénom ne contiennent pas de caractères spéciaux
- S’assurer que l’âge est bien un nombre
- S’assurer que l’adresse mail est une adresse mail valide - Saler le mot de passe