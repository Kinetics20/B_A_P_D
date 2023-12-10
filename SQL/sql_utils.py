from psycopg2 import connect

user = 'postgres'
password = 'coderslab'
host = '127.0.0.1'


def execute_sql(db_name, row_query):
    cnx = connect(
        user=user,
        password=password,
        host=host,
        database=db_name
    )
    cnx.autocommit = True
    cursor = cnx.cursor()
    cursor.execute(row_query)
    if row_query.lower().startswith('select'):
        return cursor
    else:
        return None
