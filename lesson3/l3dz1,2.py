# 1. Написать функцию num_translate(),
# переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию
# num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
#
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(numb):
    trans_numbs = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                   "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if numb.istitle():
        return trans_numbs.get(numb.lower()).title()
    return trans_numbs.get(numb)


print(num_translate_adv('One'))
print(num_translate_adv('one'))
print(num_translate_adv('notakey'))


