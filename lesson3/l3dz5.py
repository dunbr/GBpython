# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных
# слов, взятых из трёх списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
# повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

def get_jokes(n=4, f=False):
    """

    :param n: количество шуток
    :param f: флаг. отвечающий за уникальность
    :return:
    """
    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    while n > 0:
        joke = [random.choice(nouns), random.choice(adverbs), random.choice(adjectives)]
        if f == False:
            fin_joke = [random.choice(joke), random.choice(joke)]
        else:
            fin_joke = [joke.pop(random.randrange(0, len(joke))), joke.pop(random.randrange(0, len(joke)))]

        jokes.append(' '.join(fin_joke))
        n = n - 1
    return jokes


print(get_jokes(n=3, f=True))
