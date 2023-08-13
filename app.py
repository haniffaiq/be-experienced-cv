from flask import Flask, request, jsonify
import psycopg2
from config import DATABASE_CONFIG

app = Flask(__name__)


def connect_to_database():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        query1 = 'SELECT * FROM public.dummy_table;'
        cursor.execute(query1)  # Ganti dengan nama tabel Anda
        data = cursor.fetchall()
        print(data)
        cursor.close()
        conn.close()

        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
