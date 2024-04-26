import psycopg2

try: 

    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '1234',
        database = 'Database',
    )

    print('Conexion Exitosa')
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)
    cursor.execute("SELECT car FROM questions")
    rows = cursor.fetchall()
    for row in rows:
            print(row)

except Exception as ex:
    print(ex)

