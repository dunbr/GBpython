# ---------------------------5е Задание-------------------------------------
from requests import get
import datetime
from sys import argv

def currency_rates(val):
    val = val.upper()
    curs = get('http://www.cbr.ru/scripts/XML_daily.asp')
    curs_l = curs.text.split('</Valute>')

    for i in curs_l:
        if val in i:
            rub = i.split('<Value>')[1].strip('</Value>')
            print(f'1 {val} составляет {rub} рублей')
    x = curs.text.split('Date=')
    x = x[1].split('"')[1]
    x = x.split('.')
    z = datetime.date(int(x[2]), int(x[1]), int(x[0]))
    print(z)
if __name__ == '__main__':
    currency_rates(argv[1])