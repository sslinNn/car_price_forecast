from flask import Flask, render_template, url_for, request, jsonify, json, redirect
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

        return redirect(url_for('result',
                        CarYear=CarYear,
                        EngineCapacity=EngineCapacity,
                        HorsePower=HorsePower,
                        CarOdo=CarOdo,
                        CarTrans=CarTrans,
                        FuelType=FuelType,
                        CarDrive=CarDrive,
                        CarMark=CarMark,
                        CarModel=CarModel,
                        result=result))
    else:
        return render_template('index.html')


@app.route('/result')
def result():
    CarYear = request.args.get('CarYear'),
    EngineCapacity = request.args.get('EngineCapacity'),
    HorsePower = request.args.get('HorsePower'),
    CarOdo = request.args.get('CarOdo'),
    CarTrans = request.args.get('CarTrans'),
    FuelType = request.args.get('FuelType'),
    CarDrive = request.args.get('CarDrive'),
    CarMark = request.args.get('CarMark'),
    CarModel = request.args.get('CarModel'),
    result = request.args.get('result')
    return render_template('result.html',
                           CarYear=CarYear[0],
                           EngineCapacity=EngineCapacity[0],
                           HorsePower=HorsePower[0],
                           CarOdo=CarOdo[0],
                           CarTrans=CarTrans[0],
                           FuelType=FuelType[0],
                           CarDrive=CarDrive[0],
                           CarMark=CarMark[0],
                           CarModel=CarModel[0],
                           result=result[:-2:]
                           )


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
