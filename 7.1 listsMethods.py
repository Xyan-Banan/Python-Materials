a = list(range(1, 6))
print(f"list: {a}")
a.append(100500)
print(f"list: {a}")
# a.append(int(input("Enter new value for list: ")))  # таким лучше не увлекаться
print(f"list: {a}")

animals = ["cat", "dog", "guinea pig"]
if "rabbit" in animals:
    animals.index("rabbit")
    animals.remove("rabbit")
else:
    print("There is no such rabbit in animals list")

# animals.pop()
print(f"animals {animals}")
animals.insert(1, "horse")  # animals[:1] + ["horse"] + animals[1:]
print(f"animals {animals}")
animals.count("horse")

# Как можно посчитать количество вхождений символа в текст
text = "Hello"
ch = "l"
counter = 0

for char in text:
    if char == ch:
        counter += 1

# Как это сделать с помощью методов списков
# 1. Превратить текст в список символов
# 2. Проверить, сколько раз в списке встречается символ
counter = list(text).count(ch)

number = 555
number = str(number)
number.count("5")

x = 5
print(f"\nList 'a': {a}")
print(
    f"{x} in a = {x in a}"
)  # Проверить, содержится ли элемент в списке. Возвращает True или False
print(f"{x} not in a = {x not in a}")  # То же самое, что not(x in a)
print(f"min(a) = {min(a)}")  # Наименьший элемент списка
print(f"max(a) = {max(a)}")  # Наибольший элемент списка
print(
    f"a.index({x}) = {a.index(x)}"
)  # Индекс первого вхождения элемента x в список, при его отсутствии генерирует исключение ValueError
print(f"a.count({x}) = {a.count(x)}")  # Количество вхождений элемента x в список

S = "Hello"
print("Hello wolrd 1 2 3 4 5 6".split())
print(f'S.find("l") = {S.find("l")}')  # вернёт 2
print(f'S.rfind("l") = {S.rfind("l")}')  # вернёт 3
# Если же подстрока не найдена, то метод возвращает значение -1.
