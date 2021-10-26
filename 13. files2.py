import json
from os import read

human = dict()
human["first_name"] = "Ivan"
human["last_name"] = "Petrov"
human["age"] = 13
human["grades"] = {"math": [5, 4, 3, 5, 2], "russian": [5, 5, 5], "physics": [5, 4, 5]}

print(human)  # выводим информацию из словаря
print(json.dumps(human))  # выводим строку в json формате

fileName = "data_example.json"

# варианты записи информации из словаря в файл
with open(fileName, "w") as output_file:
    # output_file.write(str(human))             # 1. записать словарь как строку (самый плохой вариант, потом очень сложно распознать словарь)
    # output_file.write(json.dumps(human))      # 2. запивать в файл строку в формате json
    json.dump(human, output_file, indent=4)               # 3. записать информацию об объекте в указанный файл

# варианты чтения информации из файла
with open(fileName, "r") as read_file:
    # filetxt = read_file.read()        # 1. прочитать просто строку
    # human2 = json.loads(filetxt)      #    попробовать преобразовать строку из json в словарь
    # print(human2, type(human2))       #    вывод информацию из полученного словаря
    # print(human2["grades"])

    human2 = json.load(read_file)       # 2. прочитать json строку из файла и сразу преобразовать
    print(human)                        #    вывести полученный словарь
