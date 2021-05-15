result = []
sum_of_numb = 0
all_sum = 0
for i in range(1, 1001, 2):
    i = i ** 3
    result.append(i)
for x in result:
    c = x
    sum_of_numb = 0
    while x != 0:
        z = x % 10
        x = x // 10
        sum_of_numb += z
    if sum_of_numb % 7 == 0:
        all_sum += c
print(all_sum)
for x in range(0, len(result)):
    result[x] += 17
for x in result:
    c = x
    sum_of_numb = 0
    while x != 0:
        z = x % 10
        x = x // 10
        sum_of_numb += z
    if sum_of_numb % 7 == 0:
        all_sum += c
print(all_sum)

