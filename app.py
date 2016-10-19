from flask import Flask, jsonify
from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Post

engine = create_engine('sqlite:///tumblebog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)


@app.route('/')
def hello_world():
    print({'name': 'Tung', 'class': 'Android gen 5'})
    return jsonify({'name': 'Tung',
                    'class': 'Android gen 5'})


@app.route('/posts', methods=['GET', 'POST'])
def all_post():
    if request.method == 'GET':
        posts = session.query(Post).all()
        return jsonify(posts=[post.serialize for post in posts])

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post = Post(title=title,content=content)
        session.add(post)
        session.commit()
        return jsonify(post.serialize)


@app.route('/posts/<int:id>')
def post_hanle():
    post = session.query(Post).filter_by(id=id).first()
    return jsonify(post.serialize)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
