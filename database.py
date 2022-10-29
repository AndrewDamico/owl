import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os

def get_current_tag():
    conn = psycopg2.connect(
            database = os.environ.get('raven_DATABASE'),
            user = os.environ.get('raven_USER') ,
            password = os.environ.get('raven_PASSWORD'),
            host = os.environ.get('raven_HOST'),
            port = '5432'
            )

    cursor = conn.cursor()

    sql = '''SELECT label FROM labels ORDER BY record_id DESC LIMIT 1''';

    cursor.execute(sql)
    data = cursor.fetchone()
    conn.close()
    return data[0]

