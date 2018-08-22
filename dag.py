import airflow
from builtins import range
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG
from datetime import timedelta


args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(dag_id='example_bash_operator', default_args=args)

run_this = BashOperator(
    task_id='echo_hello_world', bash_command='echo "hello world 1234567"', dag=dag)
