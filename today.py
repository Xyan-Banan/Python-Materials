a = int(input("Сколько чисел нужно? "))
if a > 0:
    currentNumber = int(input("Введите число от -100 до 100"))
    minN = currentNumber
    maxN = currentNumber

    for i in range(a - 1):
        currentNumber = int(input("Введите число от -100 до 100"))
        if currentNumber > maxN:
            maxN = currentNumber
        if currentNumber < minN:
            minN = currentNumber

    print(f"Min = {minN}")
    print(f"Max = {maxN}")

positive_infnity = float("inf")
print("Positive Infinity: ", positive_infnity)

# Defining a negative infinite integer
negative_infnity = float("-inf")
print("Negative Infinity: ", negative_infnity)
