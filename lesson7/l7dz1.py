# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os

in_my_proj = ["settings", "mainapp", "adminapp", "authapp"]
for f in in_my_proj:
    path_to_dir = os.path.join("my_project", f)
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)

