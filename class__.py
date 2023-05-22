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

    def get_info(self):
        info = f"Марка: {self.CarMark};" \
               f"Модель: {self.CarModel};" \
               f"Год: {self.CarYear};" \
               f"Объем двигателя: {self.EngineCapacity};" \
               f"Мощность: {self.HorsePower};" \
               f"Пробег: {self.CarOdo};" \
               f"КПП: {self.CarTrans};" \
               f"Топливо: {self.FuelType};" \
               f"Привод: {self.CarDrive};"
        return info.split(sep=';')
