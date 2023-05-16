class Car:
    def __init__(self, CarYear, EngineCapacity, HorsePower, CarOdo, CarMark, CarModel, CarTrans, FuelType, CarDrive):
        self.CarYear = CarYear
        self.EngineCapacity = EngineCapacity
        self.HorsePower = HorsePower
        self.CarOdo = CarOdo
        self.CarMark = CarMark
        self.CarModel = CarModel
        self.CarTrans = CarTrans
        self.FuelType = FuelType
        self.CarDrive = CarDrive

    def get_indo(self):
        return f"CarYear:{self.CarYear}, EngineCapacity:{self.EngineCapacity}, HorsePower:{self.HorsePower}, CarOdo:{self.CarOdo}, CarMark:{self.CarMark}, CarModel:{self.CarModel}, CarTrans:{self.CarTrans}, FuelType:{self.FuelType}, CarDrive:{self.CarDrive}"


car1 = Car(2000, 1.6, 180, 100, 'Toyota', 'Mark 2', 'АКПП', 'Бензин', 'Задний')




print(car1.get_indo())