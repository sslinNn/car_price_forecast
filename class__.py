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
        info = f"CarMark: {self.CarMark};" \
               f"CarModel: {self.CarModel};" \
               f"CarYear: {self.CarYear};" \
               f"EngineCapacity: {self.EngineCapacity};" \
               f"HorsePower: {self.HorsePower};" \
               f"CarOdo: {self.CarOdo};" \
               f"CarTrans: {self.CarTrans};" \
               f"FuelType: {self.FuelType};" \
               f"CarDrive: {self.CarDrive};"
        return info.split(sep=';')
