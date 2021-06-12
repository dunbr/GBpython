# 3. Реализовать базовый класс Worker (работник).
#
#     определить атрибуты: name, surname, position (должность), income (доход);
#     последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,\
#                                                                                         {"wage": wage, "bonus": bonus};
#     создать класс Position (должность) на базе класса Worker;
#     в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии \
#     (get_total_income);
#     проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Name of Worker: {self.name} {self.surname}")

    def get_total_income(self):
        print(f'income of Worker: {self._income["wage"] + self._income["bonus"]}')


worker1 = Position("john", "Stone", "Manager", 25000, 5000)
worker1.get_full_name()
worker1.get_total_income()
worker2 = Position("Sam", "Winchester", "Hunter", 50000, 10000)
worker2.get_full_name()
worker2.get_total_income()
