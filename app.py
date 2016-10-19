from flask import Flask, jsonify
from flask import json

app = Flask(__name__)

post1 = {
    'title': 'Good day',
    'content': 'No content. OK?'
}
post2 = {
    'title': 'Bad day',
    'content': 'Nothing'
}
posts = [post1, post2]


@app.route('/')
def hello_world():
    print({'name': 'Tung', 'class': 'Android gen 5'})
    return jsonify({'name': 'Tung',
                    'class': 'Android gen 5'})


@app.route('/posts', methods=['GET'])
def all_post():
    return json.dumps(posts)


@app.route('/posts/<int:id>')
def post_hanle():
    if id == 1:
        return json.dumps(post1)
    if id == 2:
        return json.dumps(post2)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
