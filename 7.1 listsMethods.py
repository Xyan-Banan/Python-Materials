a = list(range(1,6))
print(f"list: {a}")
a.append(100500)
print(f"list: {a}")
a.append(int(input("Enter new value for list: "))) #таким лучше не увлекаться
print(f"list: {a}")

animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.index("rabbit")
animals.remove('rabbit')
print(f"animals {animals}")
animals.insert(1,"horse")
#animals[1] = "horse"
print(f"animals {animals}")
animals.count("horse")

x = 5

x in a	#Проверить, содержится ли элемент в списке. Возвращает True или False
x not in a	#То же самое, что not(x in A)
min(a)	#Наименьший элемент списка
max(a)	#Наибольший элемент списка
a.index(x)	#Индекс первого вхождения элемента x в список, при его отсутствии генерирует исключение ValueError
a.count(x)	#Количество вхождений элемента x в список

S = 'Hello'
print(S.find('l'))
# вернёт 2
print(S.rfind('l'))
# вернёт 3
#Если же подстрока не найдена, то метод возвращает значение -1.

