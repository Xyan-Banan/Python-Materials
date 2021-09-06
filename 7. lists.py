# 0    1    2       3                   4
lst = [1, 2.5, True, "hello", ["this", "is", "inner", "list"]]

n1 = [1, 2, 3]
n2 = [4, 5, 6]
n3 = n1 + n2

# Вывести весь список
print(f"list: {lst}")
# Вывести длину списка
print(f"list length: {len(lst)}")
# Вывести первый элемент списка
print(lst[0])
# Задать первому элементу списка другое значение
lst[0] = -100500
# Вывести первый элемент списка с конца
print(lst[-1])
# Три способа достучаться до предпосленднего элемента внутреннего списка
#   0       1       2       3       Прямая нумерация
#  -4      -3      -2      -1       Обратная нумерация
# ["this", "is", "inner", "list"]
print(lst[4][2], lst[-1][2], lst[-1][-2])

print("\nPrinting list")
# для каждого i из списка lst
# i будет принимать по очереди значения из списка lst
for i in lst:
    print(i, end=" ")
print()

print("\nPrinting list with indexes")
# для каждого i из диапазона от 0 до (len(lst) - 1)
# i будет принимать по очереди значения из диапазона от 0 до (len(lst) - 1)
for i in range(len(lst)):
    print(i, lst[i])
print()

print(lst[:2], lst[2:])
print(lst[:])

a = [1, 2, 3, 4, 5]
print(a)
a = a[:3] + a[4:]
print(a)

print(f"even elements: {lst[::2]}")
print(f"odd elements: {lst[1::2]}")
print(f"reverse list: {lst[::-1]}")

print(lst[::2], lst[1::2])

lst = list(range(10))
for i in lst:
    print(i, end=" ")
print()

# сходства
string = "Hello world!"
print(f"string: {string} length {len(string)}")
for i in string:
    print(i, end=" ")
print()

print(f"even string elements: \t{string[::2]}")
print(f"odd string elements: \t{string[1::2]}")
print(f"reverse string: {string[::-1]}")
