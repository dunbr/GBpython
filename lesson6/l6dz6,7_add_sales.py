from sys import argv

with open('sum_of_sales.csv', 'a', encoding='utf-8') as r_sum:
    print(f'{argv[1]}', file=r_sum)
