from flask import Flask, jsonify
import os
import time
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER", "admin")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "admin")
MYSQL_DB = os.getenv("MYSQL_DB", "mydb")

# Retry MySQL connection
for i in range(10):
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        print("Connected to MySQL")
        break
    except Error:
        print(f"MySQL not ready, retry {i+1}/10")
        time.sleep(5)
else:
    print("Could not connect to MySQL")
    exit(1)

@app.route("/")
def index():
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = [table[0] for table in cursor.fetchall()]
    return jsonify({"message": "Flask + MySQL working!", "tables": tables})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_PORT", 5000)))

