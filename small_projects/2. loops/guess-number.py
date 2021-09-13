from random import randint

repeat = True
while repeat:
    secretNumber = randint(0, 100)
    userGuess = -1

    print(
        "Я загадал число от 0 до 100. Попробуй отгадать, а я буду давать тебе подсказки :)"
    )
    while userGuess != secretNumber:
        userGuess = int(input("Какое число я загадал?\t"))
        if userGuess > secretNumber:
            print("Твое число больше загаданного")
        elif userGuess < secretNumber:
            print("Твое число меньше загаданного")
    print("Правильно! Как ты угадал???")
    answer = input("Хочешь повторить? \n1. Да \n2. Нет\n")
    repeat = True if (answer == "1" or answer.lower() == "да") else False
print("До встречи!")
