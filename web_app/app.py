from flask import Flask, render_template, url_for, request, jsonify, json
# from flask_sqlalchemy import SQLAlchemy
# import json


app = Flask(__name__)


# app.config['SQLALCHEMY DATABASE_URL'] = 'sqlite///blog.db'
# db = SQLAlchemy(app)
# class Article(db.Model):
#     pass


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        CarYear = request.form['CarYear']
        EngineCapacity = request.form['EngineCapacity']
        HorsePower = request.form['HorsePower']
        CarOdo = request.form['CarOdo']

        return render_template('result.html', CarYear=CarYear, EngineCapacity=EngineCapacity, HorsePower=HorsePower, CarOdo=CarOdo )
    else:
        return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
