# Récupération des offres de stage à partir d'un serveur IMAP

## Fonctionnement

- On se connecte au serveur imap de MADOC sur le compte de l'utilisateur hyperplan avec `imapConnection(self)`
- On récupère les mails sous forme de liste en les divisant en 5 parties avec `getMails(self)` :
    - L'ID du mail : int
    - L'émetteur du mail : str
    - La date de réception : str
    - Le corps du mail : str
    - Les pièces jointes (nom, contenu) en les séparant avec des ',' : str
- On stocke cette liste dans une base de données SQLite avec `storeMails(slef, imap)`
- On peut récupérer toutes les informations de chaque mail avec `fetchMails(self)` :
    - On peut récupérer les pièces jointes ou même les écrire dans leur format d'origine en les décodant
        ```
        if(mail.index(element) == 5):
            attachments = element.split(',')

            for i in range(0, len(attachments), 2):
                print('Nom de la pièce jointe : %s\n' % attachments[i])
                open(attachments[i], 'wb').write(base64.b64decode(attachments[i + 1]))
        ```
- On peut aussi simplement lire les mails directement dans la console avec readMails(self, imap) mais cela n'affiche pas les pièces jointes
- Enfin, on se déconnecte du serveur avec `imapDisconnection(self, imap)`


## Difficultées rencontrées

### Problèmes d'authentification

Lors de la connexion au serveur IMAP avec la commande `mail.login(imap_user, imap_pass)`, Python renvoyait cette erreur :

> imaplib.error: b'[AUTHENTICATIONFAILED] Authentication failed.'

L'erreur était due au fait que l'utilisateur est *hyperplan* et non *hyperplan.etu.univ-nantes.fr*.

### Problèmes liés à l'encodage

Il a été très long de trouver une manière pour stocker les pièces jointes en brut et les récuperer dans le bon format.

Solution : stocker la version encodée et la décoder en base 64 lors de la récupération.

# Adresses mail à éviter : 
- informations-universite@univ-nantes.fr
- ne-pas-repondre@univ-nantes.fr
- president@univ-nantes.fr
- representation@interassonantes.org
- bougetoncampus.interassonantes@gmail.com
- voixindependante@gmail.com