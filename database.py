import  psycopg2

def connection():
    con=psycopg2.connect(
        host="db",
        user="postgres",
        database="school_reg",
        password="password",
        port="5432"
    )