## Web Scrapping avec python & Ingestion de données avec Docker dnas MYSQL

Mise en place un système automatisé de collecte d'offres d'emploi, avec un stockage structuré dans une base de données MySQL, le tout orchestré à l'aide de Docker.

## Objectif

L'objectif de ce projet est de récupérer des données provenant de sites d'offres d'emploi à l'aide d'un script Python et de les enregistrer dans une base de données MySQL. Le tout est exécuté dans des conteneurs Docker pour faciliter l'environnement d'exécution.

## Fonctionnement

- Le script Python de scraping récupère les offres d'emploi.
- Ces données sont ensuite envoyées à la base de données MySQL.
- La base de données est configurée dans un conteneur séparé, accessible via le réseau Docker.
- Les données sont insérées dans la table `jobs` de la base de données, avec les informations suivantes : `TITRE_OFFRE`, `DATE_OFFRE`, `RESUME_OFFRE`.
