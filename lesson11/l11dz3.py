
c = []
while True:
    try:
        v = input('Введите число')
        if v == "stop":
            print(c)
            break
        elif v.isdigit():
            c.append(v)
        else:
            raise ValueError
    except ValueError:
        print('Вы ввели не число!')

