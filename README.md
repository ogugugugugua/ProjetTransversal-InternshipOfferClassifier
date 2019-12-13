# Classifieur d'offres

## Organisation du projet

+ Ou vérifier l'intégrité des données transférées ?
+ Redondance serveur Flask

# Test du backend

```console
$ python server.py
$ curl -X POST http://127.0.0.1:5000 -H 'Content-Type: application/json' -d '{ "text": "développeur machine" }'
```

    "[{\"label\":\"Developpement\",\"probability\":0.5},{\"label\":\"Machine Learning\",\"probability\":0.5},{\"label\":\"Traitement de l'image\",\"probability\":0.0}]"