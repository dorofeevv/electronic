import psycopg2
import pandas as pd



def connect2db(dbname):
    host = "localhost"
    user = "postgres"
    password = "postgres"
    port = "5432"
    conn = psycopg2.connect(database=dbname, user=user, password=password, host=host,
                            port=port)
    return conn

def tableCreation(conn, qfile):
    file = open(qfile, 'r')
    query = file.read()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

def tableDrop(conn, tablename):
    query = 'DROP TABLE ' + tablename
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

conn = connect2db('electronic_db')
tableDrop(conn, 'dialogmanager')
tableCreation(conn, '/home/vladislav/Desktop/2021/Статьи/Нейроинформатика/Development/SQLCreationQueries/DialogManagerCreation')
