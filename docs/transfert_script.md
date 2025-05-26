# Transfert Script

## Introduction

Pour transférer les données de ventes depuis un fichier CSV et une base MySQL vers les tables `raw_*` que tu as créées, voici deux méthodes adaptées à ton environnement Linux local :

---

## 📥 Importer un fichier CSV dans une table MySQL

### ✅ Utilisation de `LOAD DATA INFILE`

Cette méthode est efficace pour importer rapidement des données depuis un fichier CSV.

1. **Vérifie la configuration de `secure_file_priv` :**

   MySQL peut restreindre les opérations de lecture/écriture de fichiers à un répertoire spécifique défini par la variable `secure_file_priv`. Pour vérifier cette configuration, exécute la commande suivante dans MySQL :

   ```sql
   SHOW VARIABLES LIKE 'secure_file_priv';
   ```

   * Si un chemin est retourné (par exemple, `/var/lib/mysql-files/`), cela signifie que tu ne peux utiliser `LOAD DATA INFILE` que dans ce répertoire.([MySQL Tutorial][1])

   * Si la valeur est vide, il n'y a pas de restriction, et tu peux utiliser n'importe quel chemin accessible par le serveur MySQL.

   * Si la valeur est `NULL`, cela signifie que l'option `secure_file_priv` est désactivée, et tu peux utiliser n'importe quel chemin.

2. **Place le fichier CSV dans le répertoire autorisé :**

   Si `secure_file_priv` est défini, déplace ton fichier CSV dans le répertoire spécifié. Par exemple :

   ```bash
   sudo mv /chemin/vers/ton_fichier.csv /var/lib/mysql-files/
   ```

3. **Importe le fichier CSV dans la table `raw_paiements` :**

   Assure-toi que la structure de ton fichier CSV correspond à celle de la table `raw_paiements`. Ensuite, exécute la commande suivante dans MySQL :

   ```sql
   LOAD DATA INFILE '/var/lib/mysql-files/ton_fichier.csv'
   INTO TABLE raw_paiements
   FIELDS TERMINATED BY ',' 
   ENCLOSED BY '"'
   LINES TERMINATED BY '\n'
   IGNORE 1 ROWS;
   ```

   * `FIELDS TERMINATED BY ','` indique que les champs sont séparés par des virgules.

   * `ENCLOSED BY '"'` signifie que les champs sont entourés de guillemets.

   * `LINES TERMINATED BY '\n'` spécifie que chaque ligne se termine par un saut de ligne.

   * `IGNORE 1 ROWS` permet d'ignorer la première ligne du fichier CSV, généralement utilisée pour les en-têtes.([MySQL Tutorial][1])

   **Note :** Si tu rencontres des erreurs liées aux permissions, assure-toi que le fichier CSV est accessible en lecture par l'utilisateur sous lequel s'exécute le serveur MySQL.

---

## 🔄 Transférer des données depuis une base MySQL vers une autre table

Si tu souhaites copier des données depuis une table existante (par exemple, `ventes`) vers une table `raw_ventes`, utilise la commande suivante :

```sql
INSERT INTO raw_ventes
SELECT id, client_id, produit_id, quantite, date_vente
FROM ventes;
```

Cette commande insère toutes les lignes de la table `ventes` dans la table `raw_ventes`.

---

## 🛠️ Automatiser le processus avec Apache Airflow

Pour automatiser l'importation des données depuis un fichier CSV et le transfert depuis une table existante vers une table "raw", tu peux créer un DAG (Directed Acyclic Graph) dans Apache Airflow. Voici un exemple simple :

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 5, 26),
    'retries': 1,
}

with DAG('import_ventes_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    import_csv = BashOperator(
        task_id='import_csv_to_raw_paiements',
        bash_command="""
        mysql -u ton_utilisateur -p'ton_mot_de_passe' -e "
        LOAD DATA INFILE '/var/lib/mysql-files/ton_fichier.csv'
        INTO TABLE raw_paiements
        FIELDS TERMINATED BY ',' 
        ENCLOSED BY '\"'
        LINES TERMINATED BY '\\n'
        IGNORE 1 ROWS;"
        """
    )

    transfer_data = MySqlOperator(
        task_id='transfer_ventes_to_raw',
        mysql_conn_id='ta_connexion_mysql',
        sql="""
        INSERT INTO raw_ventes
        SELECT id, client_id, produit_id, quantite, date_vente
        FROM ventes;
        """
    )

    import_csv >> transfer_data
```

Assure-toi de remplacer `ton_utilisateur`, `ton_mot_de_passe`, `ton_fichier.csv` et `ta_connexion_mysql` par les valeurs appropriées à ton environnement.

---

Si tu souhaites que je t'aide à adapter ce DAG à ta configuration spécifique ou à gérer d'autres aspects de l'importation des données, n'hésite pas à le demander.

[1]: https://www.mysqltutorial.org/mysql-basics/import-csv-file-mysql-table/?utm_source=chatgpt.com "Import CSV File Into MySQL Table"
