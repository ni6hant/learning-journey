class Car:
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__fuel} litres"

    def __init__(self):
        self.__fuel = 0
        self.__odometer = 0

    def fill_up(self):
        self.__fuel = 60
    
    def drive(self,km:int):
        fuel_per_km = 1
        km_per_fuel = 1
        fuel_consumed = fuel_per_km*km
        
        if self.__fuel-fuel_consumed<0:
            self.__odometer += self.__fuel*km_per_fuel
            self.__fuel = 0
        else:
            self.__fuel -= int(fuel_consumed)
            self.__odometer += km

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)