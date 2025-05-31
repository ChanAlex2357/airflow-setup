
# Fixing MySQL and PostgreSQL Hooks in Apache Airflow

To **fix MySQL and PostgreSQL hooks** in **Apache Airflow**, you'll want to ensure that the appropriate database **providers** are installed and **configured correctly**. Here's a step-by-step guide for both:

---

## ✅ 1. **Install the Required Providers**

Airflow uses *provider packages* to interface with databases like MySQL and PostgreSQL. These are **not included by default**.

### 🐘 PostgreSQL Hook

```bash
pip install 'apache-airflow-providers-postgres'
```

### 🐬 MySQL Hook

```bash
pip install 'apache-airflow-providers-mysql'
```

You can install both at once:

```bash
pip install 'apache-airflow-providers-postgres' 'apache-airflow-providers-mysql'
```

---

## ✅ 2. **Ensure the Python Drivers Are Installed**

These are required by the hooks to connect to the DBs.

### PostgreSQL

```bash
pip install psycopg2-binary
```

### MySQL

```bash
pip install mysqlclient
```

If you have issues building `mysqlclient`, you can use the pure Python fallback:

```bash
pip install pymysql
```

...and tell SQLAlchemy to use it:

```python
# In your connection string (for example):
mysql+pymysql://user:password@host/dbname
```

---

## ✅ 3. **Add Connections in Airflow**

Go to **Airflow UI** → **Admin** → **Connections**.

### For PostgreSQL

* Conn Id: `postgres_default`
* Conn Type: `Postgres`
* Host, Schema, Login, Password, Port

### For MySQL

* Conn Id: `mysql_default`
* Conn Type: `MySQL`
* Host, Schema, Login, Password, Port

Or from the CLI:

```bash
airflow connections add 'postgres_default' \
    --conn-uri 'postgresql://user:pass@host:5432/dbname'

airflow connections add 'mysql_default' \
    --conn-uri 'mysql://user:pass@host:3306/dbname'
```

---

## ✅ 4. **Verify in a DAG or Shell**

Test PostgreSQL:

```python
from airflow.providers.postgres.hooks.postgres import PostgresHook

hook = PostgresHook(postgres_conn_id="postgres_default")
conn = hook.get_conn()
cursor = conn.cursor()
cursor.execute("SELECT 1;")
```

Test MySQL:

```python
from airflow.providers.mysql.hooks.mysql import MySqlHook

hook = MySqlHook(mysql_conn_id="mysql_default")
conn = hook.get_conn()
cursor = conn.cursor()
cursor.execute("SELECT 1;")
```

---

## ✅ 5. **Restart Airflow**

After installing packages or modifying connections:

```bash
airflow db upgrade
airflow scheduler
airflow webserver
```

---

## 🔍 Troubleshooting

| Issue                                                            | Fix                                                                |
| ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| `ModuleNotFoundError: No module named 'airflow.providers.mysql'` | Install the provider: `pip install apache-airflow-providers-mysql` |
| `ImportError: No module named 'MySQLdb'`                         | Install `mysqlclient` or switch to `pymysql`                       |
| `psycopg2.errors` or connection errors                           | Confirm host, port, DB are reachable; install `psycopg2-binary`    |

---

Let me know if you're using **Docker, Astronomer, or a specific Airflow version**, and I can tailor the steps further.
