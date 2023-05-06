from flask import Flask, render_template, url_for, request, jsonify, json
from machine_learning import main_ml_script as mms


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        CarYear = request.form['CarYear']
        EngineCapacity = request.form['EngineCapacity']
        HorsePower = request.form['HorsePower']
        CarOdo = request.form['CarOdo']
        CarMark = request.form['CarMark']
        CarModel = request.form['CarModel']

        CarTrans = request.form['CarTrans']
        FuelType = request.form['FuelType']
        CarDrive = request.form['CarDrive']

        result = mms.ml(car_year=CarYear,
                        car_odo=CarOdo,
                        engine_capacity=EngineCapacity,
                        horse_power=HorsePower,
                        car_trans=CarTrans,
                        fuel_type=FuelType,
                        car_drive=CarDrive,
                        car_mark=CarMark,
                        car_model=CarModel
                        )

        return render_template('result.html',
                               CarYear=CarYear,
                               EngineCapacity=EngineCapacity,
                               HorsePower=HorsePower,
                               CarOdo=CarOdo,
                               CarTrans=CarTrans,
                               FuelType=FuelType,
                               CarDrive=CarDrive,
                               CarMark=CarMark,
                               CarModel=CarModel,
                               result=result
                               )
    else:
        return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
