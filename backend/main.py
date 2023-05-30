# Python (backend.py)

import random
import string
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS를 사용하도록 Flask 애플리케이션에 설정

@app.route('/getRandomValue', methods=['GET'])
def get_random_value():
    random_value = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    response = {
        'randomValue': random_value
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
