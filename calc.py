x = int(input("Введите первый аргумент\n"))
y = int(input("Введите второй аргумент\n"))
op = input("Введите операцию. Доступные операции: \n+ \n- \n* \n/ \n")

if op == '+':
	print(x + y)
if op == '-':
	print(x - y)
if op == '*':
	print(x * y)
if op == '/':
	print(x / y)
