from flask import Flask, render_template, url_for, request, redirect
from machine_learning import main_ml_script as mms
from test import Car


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

        # CarYear = request.form['CarYear']
        # EngineCapacity = request.form['EngineCapacity']
        # HorsePower = request.form['HorsePower']
        # CarOdo = request.form['CarOdo']
        # CarMark = request.form['CarMark']
        # CarModel = request.form['CarModel']
        # CarTrans = request.form['CarTrans']
        # FuelType = request.form['FuelType']
        # CarDrive = request.form['CarDrive']

        with open('data.txt', 'w') as f:
            f.write(car.get_indo())
        return redirect(url_for('result'))
    else:
        return render_template('index.html')


@app.route('/result')
def result():
    with open("data.txt", 'r') as f:
        data = f.read()
    data = data.split(sep=',')


    CarYear = data[0]
    EngineCapacity = data[1]
    HorsePower = data[2]
    CarOdo = data[3]
    CarMark = data[4]
    CarModel = data[5]
    CarTrans = data[6]
    FuelType = data[7]
    CarDrive = data[8]

    res = mms.ml(car_year=CarYear,
                 car_odo=CarOdo,
                 engine_capacity=EngineCapacity,
                 horse_power=HorsePower,
                 car_trans=CarTrans,
                 fuel_type=FuelType,
                 car_drive=CarDrive,
                 car_mark=CarMark,
                 car_model=CarModel)

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
                           res=res
                           )


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
