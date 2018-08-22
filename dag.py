import airflow
from builtins import range
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from datetime import timedelta

from mypackage import foo

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(dag_id='example_bash_operator', default_args=args)

sleep1 = BashOperator(
    task_id='sleepy_1', bash_command='sleep 1m', dag=dag)

python_run = PythonOperator(
    task_id='run_class_function',
    provide_context=True,
    python_callable=foo.hello,
    dag=dag)

sleep2 = BashOperator(
    task_id='sleepy_2', bash_command='sleep 1m', dag=dag)

python_run2 = PythonOperator(
    task_id='run_class_function_2',
    provide_context=True,
    python_callable=foo.foo,
    dag=dag)

python_run.set_upstream(sleep1)
sleep2.set_upstream(python_run)
python_run2.set_upstream(sleep2)
