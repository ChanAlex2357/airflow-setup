# How to create Dags

## Introduction

Creating DAGs (Directed Acyclic Graphs) in Apache Airflow involves writing Python scripts that define the workflow of your data pipelines. Here's a step-by-step guide to help you get started:

## Creation Process

---

### 📁 1. Ensure Your DAGs Folder Is Recognized by Airflow

By default, Airflow looks for DAGs in the `dags` folder located within your `AIRFLOW_HOME` directory. If you've manually created a `dags` folder, ensure that Airflow is configured to recognize it:

1. **Check `AIRFLOW_HOME` Environment Variable**: Run `echo $AIRFLOW_HOME` in your terminal to see the current setting. If it's not set, Airflow defaults to `~/airflow`.

2. **Verify `dags_folder` in `airflow.cfg`**: Open the `airflow.cfg` file located in your `AIRFLOW_HOME` directory and check the `dags_folder` setting under the `[core]` section. Ensure it points to your desired `dags` directory.([SparkCodeHub][1])

---

### 📝 2. Create Your First DAG

1. **Navigate to the DAGs Directory**:

   ```bash
   cd $AIRFLOW_HOME/dags
   ```

2. **Create a New Python File**: For example, `hello_world_dag.py`.([LinkedIn][2])

3. **Define the DAG**: Here's a simple example using the `BashOperator`:([marclamberti][3])

   ```python
   from airflow import DAG
   from airflow.operators.bash import BashOperator
   from datetime import datetime

   with DAG(
       dag_id='hello_world',
       start_date=datetime(2025, 1, 1),
       schedule_interval='@daily',
       catchup=False
   ) as dag:
       task = BashOperator(
           task_id='print_hello',
           bash_command='echo "Hello, World!"'
       )
   ```

   Save the file after adding the above content.

---

### 🚀 3. Start Airflow Services

1. **Initialize the Database** (if not already done):

   ```bash
   airflow db init
   ```

2. **Start the Webserver**:

   ```bash
   airflow webserver --port 8080
   ```

3. **Start the Scheduler**:

   ```bash
   airflow scheduler
   ```

   Access the Airflow UI by navigating to [http://localhost:8080](http://localhost:8080) in your web browser.

---

### ✅ 4. Verify Your DAG

1. **Refresh the DAGs**: In the Airflow UI, click on the "DAGs" tab. Your newly created DAG (`hello_world`) should appear in the list.

2. **Trigger the DAG**: Turn on the DAG by toggling the switch next to its name, then click on the "Trigger DAG" button to run it.

3. **Monitor the DAG**: Click on the DAG name to view its details, monitor its progress, and check logs for each task.

---

### 🧠 Additional Tips

* **Organizing Multiple DAGs**: You can organize your DAGs into subdirectories within the `dags` folder. Airflow will recursively search for DAGs in these subdirectories.

* **Dynamic DAG Generation**: For advanced use cases, consider dynamically generating DAGs using functions or external configurations. This approach is useful for creating multiple similar DAGs programmatically.

* **Best Practices**: Ensure each DAG has a unique `dag_id`, and avoid placing heavy computations or long-running code at the top level of your DAG files to prevent issues during DAG parsing.([marclamberti][3])

---

Feel free to ask if you need assistance with more complex DAGs, integrating with databases, or setting up task dependencies!

[1]: https://www.sparkcodehub.com/airflow/dags/file-structure?utm_source=chatgpt.com "DAG File Structure Best Practices - SparkCodeHub"
[2]: https://www.linkedin.com/pulse/create-your-first-airflow-dag-ranga-reddy?utm_source=chatgpt.com "Create your first Airflow DAG - LinkedIn"
[3]: https://marclamberti.com/blog/airflow-dag-creating-your-first-dag-in-5-minutes/?utm_source=chatgpt.com "Airflow DAG: Create your first DAG in 5 minutes - marclamberti -"
