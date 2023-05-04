from flask import Flask, render_template, url_for, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)


# app.config['SQLALCHEMY DATABASE_URL'] = 'sqlite///blog.db'
# db = SQLAlchemy(app)
# class Article(db.Model):
#     pass


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.form['data']
    age = request.form['age']
    with open('data.txt', 'a') as f:
        f.write('data - ' + data + '\n' + 'age - ' + age + '\n')
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='localhost')
