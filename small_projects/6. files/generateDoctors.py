import json
from os import read

doctors = list()

ivanov = {
    "имя": "Иванов И.И.",
    "услуги": {
        "кариес молочный": 10,
        "удаление": 5,
        "пульпит": 2,
        "чистка": 5,
        "осмотр": 27,
        "анастезия": 30,
    },
}

doctors.append(ivanov)

petrov = {
    "имя": "Петров П.П.",
    "услуги": {
        "кариес молочный": 20,
        "кариес постоянный": 20,
        "удаление": 1,
        "пульпит": 3,
        "анастезия": 50,
    },
}

doctors.append(petrov)

fileName = "doctors.json"
with open(fileName, "w", encoding="utf-8") as output_file:
    # output_file.write(json.dumps(doctors, ensure_ascii=False))
    json.dump(doctors, output_file, ensure_ascii=False, indent=4)


with open(fileName, "r", encoding="utf-8") as read_file:
    # doctors2 = json.loads(read_file.read())
    doctors2 = json.load(read_file)
    for doctor in doctors2:
        print(doctor)
