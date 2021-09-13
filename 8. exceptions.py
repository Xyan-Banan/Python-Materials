animals = ["cat", "dog", "rabbit", "guinea pig"]

print(f"animals {animals}")
animals.insert(1, "horse")
print(f"animals {animals}")
animals.count("horse")

try:
    print(animals.index("frog"))
    animals.remove("rabbit")
except ValueError:
    print("some errors")

try:
    print(animals.index("frog"))
    animals.remove("rabbit")
except ValueError as err:
    print(err)

if "frog" in animals:
    print(animals.index("frog"))
    animals.remove("frog")
else:
    print("frog is not in animals list")

print("--------------------------")


def divide(x, y):
    try:  # пробуем сделать что-то
        result = x / y
    except ZeroDivisionError:  # ожидаем конкретную ошибку
        print("division by zero!")
    else:  # выполняем действия, если ничего плохого не случилось
        print("result is", result)
        return result
    finally:  # выполняем обязательные действия, независимо от результата команд
        print("executing finally clause")
        # return 0


print(divide(22, 7))
print(divide(333, 106))
print(divide(3, 0))

print("--------------------------")
try:
    print(animals.index("frog"))
    animals.remove("rabbit")
except (ValueError) as err:
    print("Value error")
    print(err)
except (Exception) as err:
    print("basic exception")
    print(err)

print("--------------------------")
try:
    print(animals.index("frog"))
    animals.remove("rabbit")
    print(animals[100])
except (ValueError, IndexError) as err:
    print("All possible errors come here")
    print(type(err))
    print(err)
except (Exception) as err:
    print("Any exception")
    print(type(err))
    print(err)
