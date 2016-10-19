from flask import Flask, jsonify
from flask import request

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


@app.route('/posts', methods=['GET', 'POST'])
def all_post():
    if request.method == 'GET':
        return jsonify(posts=[post.serialize for post in posts])

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_post = {
            'title': title,
            'content': content
        }
        posts.append(new_post)
        return jsonify(new_post)


@app.route('/posts/<int:id>')
def post_hanle():
    if id == 1:
        return json.dumps(post1)
    if id == 2:
        return json.dumps(post2)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
