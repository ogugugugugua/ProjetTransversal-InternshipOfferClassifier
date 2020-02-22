# Récupération des offres de stage à partir d'un serveur IMAP

## Fonctionnement

On se connecte au serveur imap de MADOC sur l'utilisateur hyperplan et on lit les mails qui ont été envoyés et qui ne viennent pas de l'université.

## Difficultées rencontrées

### Problèmes d'authentification

Lors de la connexion au serveur IMAP avec la commande `mail.login(imap_user, imap_pass)`, Python renvoyait cette erreur :

> imaplib.error: b'[AUTHENTICATIONFAILED] Authentication failed.'

L'erreur était due au fait que l'utilisateur est *hyperplan* et non *hyperplan.etu.univ-nantes.fr*.

# Adresses mail à éviter : 
- informations-universite@univ-nantes.fr
- ne-pas-repondre@univ-nantes.fr
- president@univ-nantes.fr
- representation@interassonantes.org
- bougetoncampus.interassonantes@gmail.com
- voixindependante@gmail.com