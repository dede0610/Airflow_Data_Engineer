from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Define the path to your Python script
SCRIPT_PATH_PURPOSE = "./purpose.py" 
SCRIPT_PATH_PIPELINE = "./data_eng_project.py" 
SCRIPT_PATH_TERMINATION = "./termination.py" 

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
with DAG(
    "daily_weather_data_pipeline",
    default_args=default_args,
    description="A simple DAG to fetch and store daily weather data for Melbourne in a database",
    schedule_interval="0 11 * * *", # Scheduled to run dayly at 11:00 am
    start_date=datetime(2024, 10, 1),  
    end_date=datetime(2024, 10, 31), 
    catchup=False,
) as dag:


    # Task 1: Run print_purpose.py script
    def print_purpose():
        subprocess.run(["python", SCRIPT_PATH_PURPOSE], check=True)

    task_print_purpose = PythonOperator(
        task_id="purpose_message",
        python_callable=print_purpose,
    )


    # Task 2: Run the Data_eng_project.py script
    def task_run_weather_script():
        subprocess.run(["python", SCRIPT_PATH_PIPELINE], check=True)

    # Task to run the Python script
    task_run_script = PythonOperator(
        task_id="run_weather_script",
        python_callable=task_run_weather_script,
    )


    # Task 3: Run print_termination_message.py script
    def print_termination_message():
        subprocess.run(["python", SCRIPT_PATH_TERMINATION], check=True)

    task_print_termination = PythonOperator(
        task_id="termination_message",
        python_callable=print_termination_message,
    )

# Set task dependencies to run them in sequence
task_print_purpose >> task_run_script >> task_print_termination
