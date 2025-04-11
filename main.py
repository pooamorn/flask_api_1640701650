from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, BUs 1640701650'



if __name__ == '__main__':
    app.run(debug=True, port=80)


