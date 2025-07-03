from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:192508Qp!@47.94.95.8/vertexa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 这个不关会有警告！
db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
