
class Warehouse:
    ware = {}
    ware_count = {}

    def add_to_Ware(self, Eq, n=1):
        try:
            if isinstance(n, int):
                print(f'Добавленна позиция {Eq.type_of_eq}. Количество: {n}')
                while n:
                    self.ware.setdefault(Eq.type_of_eq, []).append(Eq)
                    self.ware_count.setdefault(Eq.type_of_eq, 0)
                    self.ware_count[Eq.type_of_eq] += 1
                    n -= 1
            else:
                raise ValueError
        except ValueError:
            print("Невозможно выполнить отправку в на склад. Введите корректное количетсво позиций.")

    def to_departament(self, Eq, n=1):
        try:
            if isinstance(n, int):
                print(f"Позиция{Eq.type_of_eq} В количетссве {n} отправленна в отдел продаж.")
                while n:
                    self.ware[Eq.type_of_eq].remove(Eq)
                    self.ware_count[Eq.type_of_eq] -= 1
                    n -= 1

            else:
                raise ValueError
        except ValueError:
            print("Невозможно выполнить отправку в отдел продаж. Введите корректное количетсво позиций.")


class OfficeEquipment:
    def __init__(self, type_of_eq, weight, manufacturer, name):
        self.type_of_eq = type_of_eq
        self.weight = weight
        self.manufacturer = manufacturer
        self.name = name


class Scanner(OfficeEquipment):
    def __init__(self, type_of_eq, type, weight, manufacturer, name):
        super().__init__(type_of_eq, weight, manufacturer, name)
        self.type = type


class Printer(OfficeEquipment):
    def __init__(self, type_of_eq, speed_of_print, weight, manufacturer, name):
        super().__init__(type_of_eq, weight, manufacturer, name)
        self.speed_of_print = speed_of_print


class Copier(OfficeEquipment):
    def __init__(self, type_of_eq, quality, weight, manufacturer, name):
        super().__init__(type_of_eq, weight, manufacturer, name)
        self.quality = quality


C_1 = Copier('Copier', '1900', '1,5', 'HP', 'LS-305')
S_2 = Scanner('Scanner', 'Table type', '1,35', 'Lenovo', "C02B")
P_3 = Printer('Printer', '15', '1,65', 'Samsung', 'SG500')

W = Warehouse()
W.add_to_Ware(C_1)
W.add_to_Ware(S_2)
W.add_to_Ware(P_3)
W.add_to_Ware(P_3)
W.add_to_Ware(P_3)
W.add_to_Ware(P_3, 2)
W.to_departament(P_3, "2")
print(W.ware_count)
W.to_departament(P_3,2)
print(W.ware_count)