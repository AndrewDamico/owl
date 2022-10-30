import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os

def connect_to_server():
    conn = psycopg2.connect(
            database = os.environ.get('raven_DATABASE'),
            user = os.environ.get('raven_USER') ,
            password = os.environ.get('raven_PASSWORD'),
            host = os.environ.get('raven_HOST'),
            port = '5432'
            )
    return conn
    
def get_current_tag():

    conn = connect_to_server()
    cursor = conn.cursor()

    sql = '''SELECT label FROM labels ORDER BY record_id DESC LIMIT 1''';

    cursor.execute(sql)
    data = cursor.fetchone()
    conn.close()
    return data[0]

def current_tag(tag):
    sql = """INSERT INTO labels VALUES (%s, NOW(), 'start');"""
    conn = None
    try:
        conn = connect_to_server()
        cursor = conn.cursor()
        cursor.execute(sql, (tag,))
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    print (get_current_tag())
