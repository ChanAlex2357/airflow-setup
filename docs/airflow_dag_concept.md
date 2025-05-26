# Airflow - DAG Concept

## Introduction

Un **DAG** (pour *Directed Acyclic Graph*, ou *graphe orienté acyclique*) est un concept fondamental dans Apache Airflow. Il représente un **workflow** ou **pipeline de données**, c’est-à-dire une suite de tâches à exécuter dans un ordre précis, sans boucles ni cycles.

---

## Concepts clés d'un DAG

### 🧠 Qu'est-ce qu'un DAG dans Airflow ?

Dans Airflow, un DAG est une structure qui définit :

* **Les tâches** (*tasks*) : unités de travail individuelles, comme l'exécution d'une requête SQL ou le traitement d'un fichier.

* **Les dépendances** : relations entre les tâches, indiquant l'ordre d'exécution.([Medium][1])

* **Le planning** (*schedule*) : fréquence d'exécution du workflow (par exemple, quotidiennement à 2h du matin).

* **Les paramètres globaux** : comme la date de début, le nombre de tentatives en cas d'échec, etc.

Un DAG est défini en Python et est interprété par Airflow pour orchestrer les tâches selon les dépendances et le planning spécifiés.

---

### ⚙️ Comment fonctionne un DAG ?

Lorsqu'un DAG est déclenché (automatiquement selon le planning ou manuellement), Airflow crée une instance d'exécution du DAG (*DAG Run*). Chaque tâche du DAG devient une instance de tâche (*Task Instance*), qui est exécutée selon les dépendances définies.

Airflow suit l'état de chaque tâche (succès, échec, en attente, etc.) et gère les réexécutions en cas d'échec, selon les paramètres définis dans le DAG.

---

### 🛠️ Exemple simple de DAG

Voici un exemple de DAG minimal en Python :

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='exemple_dag',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    tache_1 = BashOperator(
        task_id='afficher_date',
        bash_command='date'
    )

    tache_2 = BashOperator(
        task_id='afficher_utilisateur',
        bash_command='whoami'
    )

    tache_1 >> tache_2  # tache_2 dépend de tache_1
```

Dans cet exemple :

* `tache_1` exécute la commande `date`.

* `tache_2` exécute la commande `whoami`.

* `tache_2` s'exécute uniquement après le succès de `tache_1`.

---

### 📊 Visualisation dans l'interface Airflow

Airflow fournit une interface web qui permet de :

* Visualiser la structure des DAGs.([ProjectPro][2])

* Suivre l'état des exécutions.

* Déclencher manuellement des DAGs.

* Consulter les journaux d'exécution des tâches.

---

### 📚 Pour aller plus loin

Pour une introduction plus visuelle et approfondie, tu peux consulter cette vidéo :

[Apache Airflow Overview | Architecture | What is DAG](https://www.youtube.com/watch?v=s6PgXq-SO4I&utm_source=chatgpt.com)

Cette vidéo explique les concepts de base d'Airflow, y compris les DAGs, leur architecture et leur fonctionnement.

---

Si tu souhaites créer un DAG spécifique pour importer des données depuis un fichier CSV ou une base de données MySQL vers tes tables `raw_*`, n'hésite pas à me le demander, et je t'aiderai à le concevoir.

[1]: https://medium.com/%40ansam.yousry/what-is-a-dag-in-apache-airflow-093df990ab8e?utm_source=chatgpt.com "What is a DAG in Apache Airflow? - Medium"
[2]: https://www.projectpro.io/article/apache-airflow-dags/848?utm_source=chatgpt.com "The Ultimate 101 Guide to Apache Airflow DAGS - ProjectPro"
