from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('Hello gen5!')
    return jsonify({'name': 'Tung',
                    'class': 'Android gen 5'})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
