# from airflow.decorators import task
# from airflow import DAG
# from datetime import datetime

# with DAG(
#     dag_id="demo_dag_1",
#     default_args={
#         'retries': 0
#     },
#     schedule='1/2 * * * *',
#     start_date=datetime(2022, 10, 1),
#     catchup=False
# ) as dag:

#     @task.python
#     def print_message():
#         print("=========>HELLO EVERYONE<=============")

#     print_message()
