def val_checker(l_func):  # Внешняя, содержит аргумент в виде функции lambda
    def _val_checker(func):  # внутр., классическая,содержит аргумент функц., вокруг которой мы оборачиваем
        def wrapper(num):  # локальная
            if l_func(num): # аргумент оборачиваемой функции
                print(func(num))
            else:
                raise ValueError(f'wrong val {num}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
except ValueError as err:
    print(err)
