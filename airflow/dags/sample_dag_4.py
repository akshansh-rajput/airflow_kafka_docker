# from airflow.decorators import task
# from airflow import DAG
# from datetime import datetime

# with DAG(
#     dag_id="demo_dag_4",
#     default_args={
#         'retries': 0
#     },
#     start_date=datetime(2022, 10, 1),
#     catchup= False
# ) as dag:

#     @task.python
#     def print_first_message():
#         print("=========>HELLO first message<=============")

#     t_1 = print_first_message()

#     @task.sensor(poke_interval=6*1, timeout=60*1, mode="reschedule")
#     def file_checker():
#         import os
#         from airflow.sensors.base import PokeReturnValue  
#         if os.path.exists("./dags/file/f.txt"):
#             return PokeReturnValue(is_done=True, xcom_value=True)
#         else:
#             return PokeReturnValue(is_done=False, xcom_value=True)


#     t_2 = file_checker()


#     @task.python
#     def print_second_message():
#         print("=========>ENDING<=============")

#     t_3 = print_second_message()

#     t_1 >> t_2 >> t_3
