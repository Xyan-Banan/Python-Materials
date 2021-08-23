from random import randint

print(
    """Выберите фигуру и введите ее номер:
1. Камень
2. Ножницы
3. Бумага"""
)
user = int(input())
computer = randint(1, 3)

if user == 1:
    print("Вы выбрали камень")
    if computer == 1:
        print("Компьютер выбрал камень")
        print("Ничья!")
    elif computer == 2:
        print("Компьютер выбрал ножницы")
        print("Победа!")
    else:
        print("Компьютер выбрал бумагу")
        print("Проигрыш :(")
elif user == 2:
    print("Вы выбрали ножницы")
    if computer == 1:
        print("Компьютер выбрал камень")
        print("Проигрыш :(")
    elif computer == 2:
        print("Ничья!")
        print("Компьютер выбрал ножницы")
    else:
        print("Компьютер выбрал бумагу")
        print("Победа!")
elif user == 3:
    print("Вы выбрали бумагу")
    if computer == 1:
        print("Компьютер выбрал камень")
        print("Победа!")
    elif computer == 2:
        print("Компьютер выбрал ножницы")
        print("Проигрыш :(")
    else:
        print("Компьютер выбрал бумагу")
        print("Ничья!")
else:
    print(
        """Вы ввели неправильно.
Перезапустите игру, чтобы попробовать заново."""
    )
