from airflow.providers.postgres.operators.postgres import PostgresOperator

create_employees_table = PostgresOperator(
    task_id="create_employees_table",
    postgres_conn_id="tutorial_pg_conn",
    sql="sql/employees_schema.sql",
)

create_employees_temp_table = PostgresOperator(
    task_id="create_employees_temp_table",
    postgres_conn_id="tutorial_pg_conn",
    sql="sql/employees_schema_temp.sql",
)
