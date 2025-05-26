# Raw SQL Tables Scripts

## Introduction

Voici les scripts SQL pour créer des tables "raw" dans MySQL, où toutes les colonnes sont de type `TEXT`, sans clés primaires ni étrangères. Ces tables sont conçues pour stocker les données brutes telles qu'elles sont extraites, facilitant ainsi leur ingestion dans un processus ETL avec Apache Airflow.

## Scripts SQL pour les tables "raw"

---

### 🗃️ 1. Table `raw_categories`

```sql
CREATE TABLE raw_categories (
    id TEXT,
    nom TEXT
);
```

---

### 🗃️ 2. Table `raw_produits`

```sql
CREATE TABLE raw_produits (
    id TEXT,
    nom TEXT,
    prix TEXT,
    categorie_id TEXT
);
```

---

### 🗃️ 3. Table `raw_clients`

```sql
CREATE TABLE raw_clients (
    id TEXT,
    nom TEXT,
    email TEXT,
    adresse TEXT
);
```

---

### 🗃️ 4. Table `raw_ventes`

```sql
CREATE TABLE raw_ventes (
    id TEXT,
    client_id TEXT,
    produit_id TEXT,
    quantite TEXT,
    date_vente TEXT
);
```

---

### 🗃️ 5. Table `raw_paiements`

```sql
CREATE TABLE raw_paiements (
    id TEXT,
    vente_id TEXT,
    montant TEXT,
    mode_paiement TEXT,
    date_paiement TEXT
);
```

---

### ✅ Remarques

* **Type `TEXT`** : Toutes les colonnes sont définies en tant que `TEXT` pour permettre une flexibilité maximale lors de l'ingestion des données brutes, sans se soucier des types de données spécifiques.

* **Absence de contraintes** : Aucune contrainte de clé primaire ou étrangère n'est définie, ce qui est courant dans les zones de staging ou de "landing" des architectures ETL, où l'objectif est de capturer les données telles quelles avant de les transformer et de les charger dans des tables structurées.

* **Préparation pour l'ETL** : Ces tables peuvent servir de point de départ pour des processus de transformation ultérieurs, où les données seront nettoyées, validées et insérées dans des tables finales avec des types de données appropriés et des contraintes d'intégrité référentielle.

Si tu souhaites que je t'aide à créer un DAG Airflow pour automatiser le processus d'extraction, de transformation et de chargement (ETL) de ces données, n'hésite pas à le demander.
