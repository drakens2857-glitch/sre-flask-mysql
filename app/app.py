import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)


def get_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST", "servidor-bd"),
        user=os.getenv("MYSQL_USER", "usuario"),
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE", "adso_db"),
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "API Flask funcionando"
    }), 200


@app.route("/health")
def health():
    connection = get_connection()
    connection.close()

    return jsonify({
        "status": "ok",
        "database": "connected"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
