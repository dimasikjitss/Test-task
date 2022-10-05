import psycopg2
from config import *

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

        with connection.cursor() as cursor:
            cursor.execute(
            '''CREATE TABLE tests( 
                № serial PRIMARY KEY,
                заказ№           integer,
                стоимость$        integer ,
                срокпоставки     DATE,
                стоимость₽     integer);
            '''
        )

        print("[INFO] Table created")
except Exception as _ex:
    print("[INFO] Error while working with PSQL", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PSQL connection close")