# Classification d'offres

+ Auteurs: Eric Bizet, Julien Garcia, Yulin Xie
+ Description: Projet de test des fonctionnalités d'[Hyperplan](https://hyperplan.io/index.html). 


## Expérimentations annexes

+ https://github.com/jugrc/Hyperplan/tree/develop
+ https://github.com/ogugugugugua/Hyperplan


# Démarrage

## Prérequis

L'application utilise le module `persistqueue` (https://github.com/peter-wangxu/persist-queue) pour la gestion d'une FIFO persistente.
+ `flask` permet l'ouverture du serveur web pour la visualisation des résultats
+ `pickle` permet la récupération du modèle sklearn exporté
+ `PyPDF2` et `python-docx` servent à l'extraction de texte depuis les documents reçus par mail.
+ `scrapy` permet le scraping des offres du site *ouestjob*.

```console
$ pip install persist-queue PyPDF2 flask pickle python-docx scrapy
```

## Utilisation

Lancement de l'application :

```console
$ cd app/
$ python3 main.py
```

Lancement du producteur de test (après utilisation):

```console
$ cd app/
$ python3 producers/producer_test.py
```

Lancement du scraper:

```console
$ cd app/producers/scraper/ouestjob/ouestjob/spiders/
$ scrapy crawl ouestjob
```

# Organisation du projet

## Backend

Les algorithmes délivrant les prédictions sont contenus dans le dossier `app/algorithms/` qui contient le code des images Docker à déployer. Pour le moment il n'existe qu'un seul algorithme: `tf-idf-heuristic/`

## Application

Le dossier `app/` contient le script principal permettant la commande de predictions.


# Rapport d'utilisation d'Hyperplan

## v2.0

Cette itération intègre Hyperplan sous la forme d'un module python (implémenté en tant que *hyperplan-backend* http://backend.hyperplan.io/)

Par rapport à l'implémentation précédente:

+ L'intégration devient plus simple, avec moins d'étapes.
+ Plus besoin de gérer la formation des requêtes HTTP et l'authentification à un serveur
+ Il est plus facile de controler le transit des données, avec un support du Linter (du moins partiel sur VS Code)
+ Démarrage du service instantané
+ Présence d'un dictionnaire de metadata (pour stocker un id par ex), qui évite des montages de code peu conventionnels.

## v1.0

### Etude des fonctionnalités

Lors du transit des données textuelles, il n'y a pas de vérification d'intégrité des données, du moins pour un backend de type application Flask. Les seules garanties sont fournies par la bonne formation du `json` (cela lève une exception dans le serveur Hyperplan) et la concordance des noms des variables entre le projet Hyperplan, l'application "frontend", et les algorithmes en backend.

Le déploiement systématique de Flask peut constituer une redondance. Dans clipper nous avons pu noter que la partie admin (l'équivalent d'*hyperplan-server*) était capable de démarrer des conteneurs en backend et d'encapsuler les algorithmes automatiquement.

Même si cela n'est pas géré automatiquement, l'utilisation de Docker constitue un gain de temps réel pour effectuer les tests. L'environnement python est sous contrôle et la connexion réseau est automatique une fois paramétrée. Une commande suffit à ordonner le branchement de notre algorithme.

Pour commander des prédictions, l'appel depuis le frontend est toujours le même. Cela permet de ne plus s'en soucier une fois que le mécanisme est mis en place.

### Bugs rencontrés

+ Erreur au lancement de commandes non documentées sans argument (ex: `delete`)
+ Impossible de supprimer une feature depuis le CLI.
+ On ne peut pas utiliser des underscores (peut être est-ce voulu):

```console
ProjectIdIsNotAlphaNumerical : Project id offer_classifier is not alphanumerical
Ready to start predicting ! 
```

+ Un classique mais éviter les espaces dans les labels retournés en JSON!
+ Dans le CLI: `udpate project` => `1. choose default algorithm` retourne une erreur et quitte le CLI:


```console
hyperplan> update project offerClassifier
1. Set default algorithm
2. Set AB testing
choice: 1
Traceback (most recent call last):
  File "/home/eric/.local/lib/python3.7/site-packages/hyperplan/project.py", line 150, in list_algorithms
    algorithms = project['algorithms']
TypeError: 'RootLogger' object is not subscriptable
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/eric/.local/bin/hyperplan", line 10, in <module>
    sys.exit(main())
  File "/home/eric/.local/lib/python3.7/site-packages/hyperplan/index.py", line 96, in main
    create_api_and_start_cmd(default_service, logger, server, login, password)
  File "/home/eric/.local/lib/python3.7/site-packages/hyperplan/index.py", line 34, in create_api_and_start_cmd
    start_cmd(api, logger)
  File "/home/eric/.local/lib/python3.7/site-packages/hyperplan/index.py", line 38, in start_cmd
    HyperplanPrompt(api, logger).cmdloop()
  File "/usr/lib/python3.7/cmd.py", line 138, in cmdloop
    stop = self.onecmd(line)
  File "/usr/lib/python3.7/cmd.py", line 217, in onecmd
    return func(arg)
  File "/home/eric/.local/lib/python3.7/site-packages/hyperplan/hpcmd.py", line 125, in do_update
    update_project(self.api, self.logger, entity_id)
  File "/home/eric/.local/lib/python3.7/site-packages/hyperplan/project.py", line 204, in update_project
    list_algorithms(logger, project)
  File "/home/eric/.local/lib/python3.7/site-packages/hyperplan/project.py", line 160, in list_algorithms
    logger.warn('an unhandled error occurred in list_algorithms: {}'.format(err))
AttributeError: 'dict' object has no attribute 'warn'
```

+ Echec d'authentification non loggé dans le serveur: "*Accepted connection*" alors que le code réponse HTTP est 401.

### Autres difficultés rencontrées

+ En Python: bien utiliser l'attribut `json` de requests.post pour éviter les problèmes de JSON malformés (à cause des caractères unicode à échapper correctement).
+ Comportement étrange de IPython avec UTF-8.

### A considérer pour le futur

Ici l'application ne traite qu'un seul fichier et stocke ses résultats dans un fichier `json`. Il faudra pouvoir prendre en charge le stockage de multiples fichiers et stocker leur catégorie d'une certaine façon. On ne teste pas les capacités d'Hyperplan à délivrer des prédictions en masse.

Nous ne nous sommes pas penchés sur les fonctionnalités de branchement avec des applications de type TensorFlow serving mais on peut imaginer que le comportement entre l'application et le serveur Hyperplan reste le même.

Dans les jours à venir nous essaierons de mettre en place les nouvelles fonctionnalités proposées par *hyperplan-backend* (que nous n'avons pas encore pu tester). Des points soulignés ici ne sont peut-être plus pertinents depuis la sortie du logiciel.