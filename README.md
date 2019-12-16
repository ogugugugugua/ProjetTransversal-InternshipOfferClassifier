# Classifieur d'offres

## Démarrage

Dans le répertoire contenant `docker-compose.yml `(avec Hyperplan et PostgreSQL):

```console
$ sudo docker-compose up
```

Build de l'image (à faire au premier démarrage)

```console
$ cd algorithms/tf-idf-heuristic/
$ docker build . -t simple_heuristic:latest
```

Création et lancement du conteneur (la première fois):

```console
$ docker run --network=hyperplan --name=simple_heuristic simple_heuristic:latest
```

Lancement du conteneur (après création):

```console
$ docker start -a simple_heuristic
```

Fermeture du conteneur:

```console
$ docker stop simple_heuristic
```

### Nettoyage (si nécessaire)

```console
$ docker ps -a
$ docker rm simple_heuristic
```


## Organisation du projet


## Test du backend

```console
$ python server.py
$ curl -X POST http://127.0.0.1:5000 -H 'Content-Type: application/json' -d '{ "text": "développeur machine" }'
```

    "[{\"label\":\"Developpement\",\"probability\":0.5},{\"label\":\"Machine Learning\",\"probability\":0.5},{\"label\":\"Traitement de l'image\",\"probability\":0.0}]"

# Notes par rapport à Hyperplan

## Etude des fonctionnalités

+ Ou vérifier l'intégrité des données transférées ?
+ Redondance serveur Flask

## Bugs rencontrés

+ Erreur au lancement de commandes non documentées sans argument
+ Erreur de demarrage liée à Java ?
+ Comment supprimer une feature ?

```console
ProjectIdIsNotAlphaNumerical : Project id offer_classifier is not alphanumerical
Ready to start predicting ! 
```

+ Peut pas utiliser des underscores
+ Eviter les espaces dans les labels retournés en JSON!
+ udpate project => 1. choose default algorithm error



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

+ Echec d'authentification a logger (http 401)
+ Bien utiliser l'attribut json de requests.post pour éviter les problèmes de JSON malformés