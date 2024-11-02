# Airflow_Data_Engineer


This project was designed as a training exercise to help me understand and practice sequencing tasks in Apache Airflow. 
The goal of the DAG is to simulate a simple data pipeline with three distinct steps, each executed by a separate Python script. 

The first task runs `print_purpose.py`, a script that prints the project’s purpose, which is to fetch and store daily weather data. 
The second task, `data_eng_project.py`, is responsible for extracting real-time weather data for Melbourne through an API and saving it to a local SQLite database. 
Finally, the third task, `print_termination_message.py`, outputs a message confirming the successful completion of the DAG. 

By structuring these tasks in sequence, I learnt how to manage and organize workflows in Airflow, 
specifically focusing on task dependencies and controlled execution order.
'''
