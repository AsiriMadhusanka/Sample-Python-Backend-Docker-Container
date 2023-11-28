from flask import Flask, request, jsonify
from db import get_conn, release_conn

app = Flask(__name__)

@app.route('/setup', methods=['GET'])
def setup():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE TABLE schools( id SERIAL PRIMARY KEY, name VARCHAR(100), address VARCHAR(100))')
        conn.commit()
        return jsonify(message="Successfully created table"), 200
    except Exception as e:
        print(str(e))
        return jsonify(message="An error occurred"), 500
    finally:
        release_conn(conn)

@app.route('/', methods=['POST'])
def create_school():
    name = request.json.get('name')
    location = request.json.get('location')

    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO schools (name, address) VALUES (%s, %s)', (name, location))
        conn.commit()
        return jsonify(message="Successfully added child"), 200
    except Exception as e:
        print(str(e))
        return jsonify(message="An error occurred"), 500
    finally:
        release_conn(conn)

@app.route('/', methods=['GET'])
def get_schools():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM schools')
        data = cursor.fetchall()
        return jsonify(data), 200
    except Exception as e:
        print(str(e))
        return jsonify(message="An error occurred"), 500
    finally:
        release_conn(conn)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


