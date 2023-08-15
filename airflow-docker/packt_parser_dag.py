from airflow import DAG # type: ignore
from airflow.operators.bash_operator import BashOperator # type: ignore
from airflow.utils.dates import days_ago # type: ignore

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'is_paused_upon_creation': True,}

with DAG(
    dag_id='packt_parser',
    schedule_interval='0 6 * * *',
    catchup=False,
    tags=['parser'],
    default_args=default_args,
    ) as dag:

    parser_task = BashOperator(
        task_id='parser',
        bash_command='python3 ./src/parser_script.py',
        dag=dag,
        cwd=dag.folder,)

    parser_task