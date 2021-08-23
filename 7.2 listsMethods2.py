s = input("Введите несколько чисел через пробел: ")
a = s.split()
print(a)
for i in range(len(a)):
    a[i] = int(a[i])

print(f"list: {a}")

msg = "Введите несколько чисел через пробел еще раз: "
a = [int(i) for i in input(msg).split()]
print(f"list: {a}")
# s = input("Введите несколько чисел через пробел еще раз: ")
# a = [int(i) for i in s.split()]

# a = [0,1,4,9,16]
a = [i*i for i in range(10)]
print(a)

a = [i for i in a if i % 2 == 0]
print(a)

a = '192.168.0.1'.split('.')
print(f"list: {a}")
ip = ".".join(a)
print(f"ip: {ip}")


a = [int(i) for i in ip.split('.')]
print(f"list: {a}")
# ip = ".".join(a) - вызовет ошибку
ip2 = '.'.join([str(i) for i in a])
print(f"ip: {ip2}")