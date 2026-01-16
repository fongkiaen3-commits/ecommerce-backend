from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")

def check_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            connect_timeout=1
        )
        conn.close()
        return True
    except:
        return False

@app.route('/')
def home():
    return "<h1>Indestructible Shop</h1><p>Status: Online</p>"

@app.route('/health')
def health():
    if check_db_connection():
        return jsonify(status="healthy", db="connected"), 200
    else:
        return jsonify(status="unhealthy", db="disconnected"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
