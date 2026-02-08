from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import time

app = Flask(__name__)
CORS(app)

def wait_for_db():
    while True:
        try:
            return psycopg2.connect(
                host="database",
                database="todos",
                user="postgres",
                password="postgres"
            )
        except:
            print("Waiting for database...")
            time.sleep(2)

conn = wait_for_db()

@app.route("/todos")
def get_todos():
    cur = conn.cursor()
    cur.execute("SELECT text FROM todos;")
    rows = cur.fetchall()
    cur.close()
    return jsonify([r[0] for r in rows])

app.run(host="0.0.0.0", port=5000)



