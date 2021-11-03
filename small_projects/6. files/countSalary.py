import json


def countPoints(services):
    points = {
        "кариес молочный": 4,
        "кариес постоянный": 4,
        "удаление": 3,
        "пульпит": 13,
        "чистка": 4,
        "осмотр": 1.57,
        "анастезия": 0.81,
    }
    summ = 0
    for service, quantity in services.items():
        summ += points.get(service, 0) * quantity
    return summ


print("Введите имя файла с докторами:")
# fileName = input()
fileName = "./small_projects/6. files/doctors.json"
try:
    with open(fileName, encoding="utf-8") as file:
        try:
            doctors = json.load(file)
        except Exception as e:
            print("Невозможно обработать данные из файла")
            print(e)
            exit()
except FileNotFoundError as e:
    print("Невозможно открыть файл с таким именем")
    print(e)
    exit()

res = list()
for doctor in doctors:
    points = countPoints(doctor["услуги"])
    res.append({"имя": doctor["имя"], "зарплата": points * 1000})

outFileName = "result.json"
try:
    with open(outFileName, "w", encoding="utf-8") as output_file:
        json.dump(res, output_file, ensure_ascii=False)
except Exception as e:
    print("ошыбка")
    print(e)
