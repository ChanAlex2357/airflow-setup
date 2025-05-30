# Todo List

## 1 - Installation

- [x] Installation de airflow
- [x] Installation de postgres
- [x] Installation de mysq

## 2 - Extraction

- [x] Mysql
  - [x] Creation de la base de donnee
  - [x] Creation des tables
  - [x] Insertion des donnees de test
- [x] Telecharger le fichier csv
- [ ] Planifier tache extraction
  - [x] creation dag "transfer"
  - [x] etablir la liste des tables a transferer
  - [x] cree la base de donnee raw (dwh_raw)
  - [x] cree un schema pour les donnees raw dans postgres
  - [x] cree les tables raw pour recuperer les donnees
  - [x] tache 1 - extraire donnee mysql
    - [x] nettoyer les tables du data lakes
    - [x] recuperer les donnees des tables dans mysql
    - [x] insertion des donnees dans les tables de postgresql
  - [ ] tache 2 - extraire donnee csv
    - [ ] lecture fichier
    - [ ] copier lignes de donnees directement dans postgres
- [ ] Documentation
  - [ ] Operators
    - [ ] Python operator
    - [ ] Postgres operator
    - [ ] Mysql operator
  - [ ] documentation sur les hooks
