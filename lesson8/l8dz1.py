# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?
import re


def email_parse(email):
    re_email = re.compile(r"\w*[@]\w*[\.]\w*")
    x, y = re_email.match(email).group(0).split('@')
    if not re_email.match(email):
        raise ValueError(f'wrong email:{email}')
    return {'username': x, 'domian': y}

for i in ['someone@geekbrains.ru', 'someonegeekbrains.ru', 'someone@geekbrainsru']:
    try:
        print(email_parse(i))
    except AttributeError:
        print(f'{i} - неверный формат')
