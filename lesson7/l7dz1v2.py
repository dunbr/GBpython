import os

in_my_proj = {"my_project": [{"settings": []}, {"mainapp": []}, {"adminapp": []}, {"authapp": []}]}
for key, value in in_my_proj.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
