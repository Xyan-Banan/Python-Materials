russianSmallLetters = range(ord("а"), ord("я") + 1)
russianBigLetters = range(ord("А"), ord("Я") + 1)
englishSmallLetters = range(ord("a"), ord("z") + 1)
englishBigLetters = range(ord("A"), ord("Z") + 1)

text = input(
    "Введите текст с использованием русских или латинских символов (остальные не будут изменены)\n"
)
shift = int(input("Насколько нужно сделать сдвиг?\n"))

for char in text:
    code = ord(char)
    selectedRange = None

    if code in russianSmallLetters:
        selectedRange = russianSmallLetters
    elif code in russianBigLetters:
        selectedRange = russianBigLetters
    elif code in englishSmallLetters:
        selectedRange = englishSmallLetters
    elif code in englishBigLetters:
        selectedRange = englishBigLetters

    if selectedRange != None:
        shift %= len(selectedRange)
        code += shift
        if code >= selectedRange.stop:  # selectedRange.stop is after the last letter
            code -= len(selectedRange)
        elif code < selectedRange.start:
            code += len(selectedRange)

    print(chr(code), end="")
