from os import path, walk, listdir
import shutil

project_name = "my_project"
try:
    for root, dirs, files in walk(project_name):
        if 'templates' in dirs and root != project_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(project_name, 'templates', path.basename(root)))
except FileExistsError:
    print("Already worked with these templates!")



                # walk(project_name):
                # [('my_project', ['mainapp', 'settings', 'authapp'], []),
                #  ('my_project/mainapp', ['templates'], ['__init__.py', 'models.py', 'views.py']),
                #  ('my_project/mainapp/templates', ['mainapp'], []),
                #  ('my_project/mainapp/templates/mainapp', [], ['base.html', 'index.html']),
                #  ('my_project/settings', [], ['dev.py', 'prod.py', '__init__.py']),
                #  ('my_project/authapp', ['templates'], ['__init__.py', 'models.py', 'views.py']),
                #  ('my_project/authapp/templates', ['authapp'], []),
                #  ('my_project/authapp/templates/authapp', [], ['base.html', 'index.html'])]
