import os
import psycopg
from flask import Flask
import dotenv

app = Flask(__name__)

dotenv.load_dotenv()
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

connect_string = "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"

with psycopg.connect(connect_string) as conn:
    with conn.cursor() as cur:
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS products (id serial \
            PRIMARY KEY, name varchar(100), price float);''')
        cur.execute(
            '''INSERT INTO products (name, price) VALUES \
            ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')
        conn.commit()


@app.route('/')
def hello_world():
    return '<h1>Elska Ágústu svo mikið<h1>'


@app.route('/lol')
def lolol():
    with psycopg.connect(connect_string) as conn:
        data = conn.execute('''SELECT * FROM products''').fetchall()

    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
