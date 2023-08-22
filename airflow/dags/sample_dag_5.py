# from airflow.decorators import task
# from airflow import DAG
# from datetime import datetime, timedelta
# from airflow.operators.python import get_current_context
# import random


# with DAG(
#     dag_id="demo_dag_5",
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
#     def random_number():
#         list1 = [1, 2, 3, 4, 5, 6]
#         num = random.choice(list1)
#         context = get_current_context()
#         ti = context['ti']
#         ti.xcom_push(key = "random", value = num)
#         print("====> ", num)

#     t_1 = random_number()

#     @task.python
#     def second_method():
#         context = get_current_context()
#         ti = context['ti']
#         num = ti.xcom_pull(task_ids= 'random_number', key= 'random')
#         print("===> ", num)
    
#     t_2 = second_method()

#     t_1 >> t_2
