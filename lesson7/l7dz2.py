import yaml
import os

with open('config.yaml') as f:
    content = yaml.safe_load(f)
    # {'my_project': {'settings': ['__init__.py', 'dev.py', 'prod.py'],
    #                 'mainapp': ['__init__.py', 'models.py', 'views.py',
    #                             {'templates': [{'mainapp': ['base.html', 'index.html']}]}],
    #                 'authapp': ['__init__.py', 'models.py', 'views.py',
    #                             {'templates': [{'authapp': ['base.html', 'index.html']}]}]}}
def starter(values, prefix=""):
    for key, value in values.items():
        dir_path = os.path.join(prefix, key)
        print(dir_path)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(value, dict):
            starter(value, dir_path)
        else:
            for i in value:
                if isinstance(i, dict):
                    starter(i,dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path,f'{i}'),'w') as _:
                        pass



starter(content)
