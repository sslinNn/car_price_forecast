from flask import Flask, render_template, url_for, request, redirect
from machine_learning import main_ml_script as mms
from class__ import Car
import pickle


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['POST'])
def index():
    if request.method == 'POST':
        car = Car(CarYear=request.form['CarYear'],
                  EngineCapacity=request.form['EngineCapacity'],
                  HorsePower=request.form['HorsePower'],
                  CarOdo=request.form['CarOdo'],
                  CarMark=request.form['CarMark'],
                  CarModel=request.form['CarModel'],
                  CarTrans=request.form['CarTrans'],
                  FuelType=request.form['FuelType'],
                  CarDrive=request.form['CarDrive']
                  )
        mms.save_object(car, 'data.pkl')
        return redirect(url_for('result'))
    else:
        return render_template('index.html')


@app.route('/result')
def result():
    with open('data.pkl', 'rb') as inp:
        car = pickle.load(inp)
    return render_template('result.html', info=car.get_info(), res=mms.ml(car))


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
