import psycopg2
from decouple import config

def sql_read(query, parameters=[]):
    connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.close()
    return results


def sql_write(query, parameters=[]):
    connection = psycopg2.connect(dbname="itemsforhire", user='postgres', port=5433, password=config('SECRET_KEY'))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()