# from airflow.decorators import task
# from airflow import DAG
# from datetime import datetime, timedelta
# from airflow.operators.python import get_current_context
# import random


# with DAG(
#     dag_id="demo_dag_3",
#     default_args={
#         'retries': 3,
#         "retry_delay": timedelta(seconds=30),
#         # 'schedule_interval': '@once'
#     },
#     # schedule='1/2 * * * *',
#     start_date=datetime(2022, 10, 1),
#     catchup=False
# ) as dag:

#     @task.python
#     def random_number_fail():
#         list1 = [1, 2, 3, 4, 5, 6]
#         num = random.choice(list1)
#         if num > 3:
#             raise ValueError("Number is equal or greater than 3")
#         else:
#             print("Number is less than 3")

#     t_1 = random_number_fail()

#     # @task.python
#     # def second_method():
#     #     context = get_current_context()
#     #     dag_run = context['dag_run']
#     #     config = dag_run.conf
#     #     print("====>", config.get('message', 'No value found'))
    
#     # t_2 = second_method()

#     # t_1 >> t_2
