# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.
from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        # self.speed = randint(30,70)

    def go(self):
        print("Car is gone!")

    def stop(self):
        print("Car is stop")

    def turn(self, direction):
        print(f"Car turn on {direction}")

    def show_speed(self):
        print(f"Current speed: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"WARNING: SPEED EXCEEDED! Current speed: {self.speed}")
        else:
            print(f"Current speed: {self.speed}")
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"WARNING: SPEED EXCEEDED! Current speed: {self.speed}")
        else:
            print(f"Current speed: {self.speed}")
class SportCar(Car):
    pass

class PoliceCar(Car):
    pass
car1 = Car(100, 'green', 'Lexus', False)
car1.go()
car1.stop()
car1.turn("left")
car1.show_speed()
towncar1 = TownCar(100, 'Red', 'Lada', False)
towncar1.show_speed()
towncar1.go()