
d = 0
h = 0
m = 0
s = 0
duration = int(input('Введите число : '))
if duration <= 60:
    print(f'{duration} сек')
elif duration > 60 and duration <= 3600:
    m = (duration // 60)
    s = duration - (m * 60)
    print(f' {m} мин {s} сек')
elif duration > 3600 and duration <= 86400:
    h = (duration // 3600)
    m = (duration // 60) - (h * 60)
    s = duration - ((h * 60 * 60) + (m * 60))
    print(f'{h} час {m} мин {s} сек')
else:
    d = (duration // 3600) // 24
    h = (duration // 3600) - (d * 24)
    m = (duration // 60) - ((d * 24 * 60) + (h * 60))
    s = duration - ((d * 24 * 60 * 60) + (h * 60 * 60) + (m * 60))
    print(f'{d} дн {h} час {m} мин {s} сек')