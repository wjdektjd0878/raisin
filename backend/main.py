from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://id:pw@url/db'
db = SQLAlchemy(app)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main = db.Column(db.String(500))
    choice = db.Column(db.String(500))

@app.route('/start', methods=['POST'])
def start():
    name = request.json['name']
    # 이름을 처리하는 로직
    return jsonify({'message': 'success'}), 200

@app.route('/story', methods=['GET'])
def get_story():
    # id는 기본적으로 1로 설정하였습니다. 이 부분은 실제 구현에 따라 다르게 설정하셔야 합니다.
    story = Story.query.get(1)
    if story is None:
        return jsonify({'error': 'Story not found'}), 404
    return jsonify({'main': story.main, 'choice': story.choice}), 200

if __name__ == '__main__':
    app.run(port=5000)
