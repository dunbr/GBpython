import itertools
import json

with open('hobby.csv', 'r', encoding='utf-8') as h:
    hobby = [i.rstrip() for i in h]
    with open('users.csv', 'r', encoding='utf-8') as u:
        usrs = [i.rstrip().replace(',', ' ') for i in u]
        if len(usrs) >= len(hobby):
            with open('users_hobby.json', 'w', encoding='utf-8') as d:
                c = (itertools.zip_longest(usrs, hobby))
                u_h_dict = {str(us[0]).strip(): str(us[1]).strip() for us in c}
                print(u_h_dict)
                json.dump(u_h_dict, d, ensure_ascii=False, indent=4)
        else:
            exit(1)
