print("Введите два операнда и операцию")
a = float(input("Введите первый операнд: "))
b = float(input("Введите второй операнд: "))
print("""Выберите операцию (введите символ или номер):
1. +
2. -
3. *
4. /""")
op = input()

if(op == '+' or op == '1'):
    op = '+'
    res = a + b
elif(op == '-' or op == '2'):
    op = '-'
    res = a - b
elif(op == '*' or op == '3'):
    op = '*'
    res = a * b
elif(op == '/' or op == '4'):
    if(b == 0):
        print("Делить на ноль нельзя!!!")
        exit()
    op = '/'
    res = a / b
else:
    print("Операция введена неправильно!")
    exit()
print(f"Результат: {a} {op} {b} = {res}")

