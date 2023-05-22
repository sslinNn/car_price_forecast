from flask import Flask, render_template, url_for, request, redirect, session, jsonify
from flask_session import Session
from machine_learning import main_ml_script as mms
from shit import mrk_list, car_dict
from class__ import Car


app = Flask(__name__)
app.secret_key = 'ec5rv6tb7ynu8jmio,*&(HNJMK<L'
app.config['SESSION_TYPE'] = 'filesystem'  # Можно использовать другие типы хранилища сессий
Session(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['POST'])
def index():
    if request.method == 'POST':
        car = Car(CarYear=request.form['CarYear'],
                  EngineCapacity=request.form['EngineCapacity'],
                  HorsePower=request.form['HorsePower'],
                  CarOdo=request.form['CarOdo'],
                  CarMark=request.form['brand'],
                  CarModel=request.form['model'],
                  CarTrans=request.form['CarTrans'],
                  FuelType=request.form['FuelType'],
                  CarDrive=request.form['CarDrive']
                  )
        session['car'] = car
        return redirect(url_for('result'))
    else:
        return render_template('index.html', brands=car_dict.keys())


@app.route('/get_models', methods=['POST'])
def get_models():
    selected_brand = request.json['brand']
    available_models = car_dict.get(selected_brand, [])
    return jsonify({'models': available_models})


@app.route('/result')
def result():
    car = session.get('car')
    info = car.get_info().split(sep=';')
    res = mms.ml(car=car)
    return render_template('result.html', info=info, res=res, mrk_list=mrk_list)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
