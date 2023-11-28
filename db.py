import psycopg2
from psycopg2 import pool

minconn = 1
maxconn = 10

db_pool = psycopg2.pool.SimpleConnectionPool(minconn, maxconn,
    host="db",
    database="db123",
    user="user123",
    password="password123",
    port="5432")
    

def get_conn():
    return db_pool.getconn()

def release_conn(conn):
    return db_pool.putconn(conn)
