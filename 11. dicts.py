# Создадим пустой словать Capitals
Capitals = dict()

# Заполним его несколькими значениями
Capitals["Russia"] = "Moscow"
Capitals["Ukraine"] = "Kiev"
Capitals["USA"] = "Washington"

Countries = ["Russia", "France", "USA", "Ukraine"]

for country in Countries:
    # Для каждой страны из списка проверим, есть ли она в словаре Capitals
    if country in Capitals:
        print("Столица страны " + country + ": " + Capitals[country])
    else:
        print("В словаре нет страны c названием " + country)

##############################################################################
Capitals = {"Russia": "Moscow", "Ukraine": "Kiev", "USA": "Washington"}
Capitals = dict(Russia="Moscow", Ukraine="Kiev", USA="Washington")
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
print(Capitals)

for country in Capitals:
    print(country, Capitals[country])

print("@@@@@@@@@@")
for country, capital in Capitals.items():
    print(country, capital)

print("@@@@@@@@@@")
print("Keys")
for key in Capitals.keys():
    print(key)

print("Values")
for value in Capitals.values():
    print(value)

print("@@@@@@@@@@")
# print(Capitals["Italy"])
print(Capitals.get("Italy"))
print(Capitals.get("Italy", "@@@"))
