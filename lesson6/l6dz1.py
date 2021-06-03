with open('nginx_logs.txt', 'r') as pars:
    x = ((i.replace('"', ' ').split(' ')[0], i.replace('"', ' ').split(' ')[6], i.replace('"', ' ').split(' ')[7]) for i
         in pars)
    print(list(x))
