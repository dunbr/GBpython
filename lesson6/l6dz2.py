with open('nginx_logs.txt', 'r') as pars:
    all_of_ip = [(i.replace('"', ' ').split(' ')[0]) for i in pars]
set_of_ip = set(all_of_ip)
d = ((z, all_of_ip.count(z)) for z in set_of_ip)  # ip : кол-во запросов
spamer = max(d, key=lambda i: i[1])
print('Найден спамер: С адреса {} было отправлено {} запросов '.format(*spamer))
