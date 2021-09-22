from random import choice, randrange
from os import system

# Вводная часть
system("cls")
print(
    'Привет! Давай сыграем в "виселицу" 😈\nИгра, в которой нужно отгатывать слово по буквам.'
)
print("Хочешь, чтобы я загадал слово или твой друг? \n1. Компьютер \n2. Друг")
answer = input()
# В зависимости от ответа загадываем слово сами или даем ввести другу
if answer == "2":
    system("cls")
    print("Попроси друга ввести слово")
    word = input().lower()
    while not word.isalpha():
        print("Некорректный ввод!")
        print("Введи слово, состоящее только из символов алфавита!")
        word = input().lower()
    print(f"Я запомнил твое слово! ({word})")
    print("Нажми любую кнопку и передай управление обратно")
else:
    print("Я загадаю для тебя слово!")
    words = ["пума", "трактор", "сосна", "арбуз", "барабанщик", "книга", "выключатель"]
    word = words[randrange(len(words))]
    # word = choice(words) # можно использовать как альтернативу

# заполняем слово символлами
guess = ["#"] * len(word)
# список использованных символов
used = []

# lives = 7
while "#" in guess:
    system("pause")
    system("cls")
    print("Загаданное слово: " + "".join(guess))
    print(f"Использованные символы: {used}")
    # print(f"Количество жизней: {lives}")
    print("Введи одну букву:")
    letter = input().lower()
    if len(letter) == 1:
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guess[i] = letter
            print("Такая буква есть в слове! 😄")
        else:
            print("Такой буквы нет в слове ☹")
            # lives-=1
        used.append(letter)
    else:
        print("Ты должен был ввести одну букву! Попробуй еще раз! 😡")
system("cls")
print(
    f'Поздравляю, ты выиграл! 🎉🎉🎉\nТы отгадал слово "{word}". \nПерезапусти игру, чтобы сыграть заново'
)
