russianSmallLetters = range(ord("а"), ord("я") + 1)
russianBigLetters = range(ord("А"), ord("Я") + 1)
englishSmallLetters = range(ord("a"), ord("z") + 1)
englishBigLetters = range(ord("A"), ord("Z") + 1)

text = input(
    "Введите текст с использованием русских или латинских символов (остальные не будут изменены)\n"
)
shift = int(input("Насколько нужно сделать сдвиг?"))

for char in text:
    code = ord(char)
    if code in russianSmallLetters:
        code += shift
