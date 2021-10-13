# ┌───┬───┬───┐
# │   │   │   │
# ├───┼───┼───┤
# │   │   │   │
# ├───┼───┼───┤
# │   │   │   │
# └───┴───┴───┘

from os import system
from random import choice


def drawField(field):
    print("    1   2   3  ")
    print("  ┌───┬───┬───┐")
    print(f"1 │ {field[0]} │ {field[1]} │ {field[2]} │")
    print("  ├───┼───┼───┤")
    print(f"2 │ {field[3]} │ {field[4]} │ {field[5]} │")
    print("  ├───┼───┼───┤")
    print(f"3 │ {field[6]} │ {field[7]} │ {field[8]} │")
    print("  └───┴───┴───┘")


#     print(
#         f"""
#     1   2   3
#   ┌───┬───┬───┐
# 1 │ {field[0]} │ {field[1]} │ {field[2]} │
#   ├───┼───┼───┤
# 2 │ {field[3]} │ {field[4]} │ {field[5]} │
#   ├───┼───┼───┤
# 3 │ {field[6]} │ {field[7]} │ {field[8]} │
#   └───┴───┴───┘
# """
#     )


def humanMove(available):
    print(
        "Выбери поле для хода. Введи его координаты через пробел: сначала строка, затем столбец."
    )
    answer = input().split()
    if len(answer) != 2:
        raise Exception("Неверный формат ввода. Попробуй еще раз.")

    try:
        answer = [int(i) for i in answer]
    except ValueError:
        raise Exception("Невозможно привести введенное к координатам. Попробуй еще раз")

    row, col = answer
    if row < 1 or row > 3 or col < 1 or col > 3:
        raise Exception("Номер строки и столбца должен быть от 1 до 3 включительно.")

    row -= 1
    col -= 1
    res = row * 3 + col
    if res not in available:
        raise Exception("Поле уже занято. Попробуй еще раз.")
    return res


def computerMove(available):
    if len(available) > 0:
        return choice(available)


def allEqual(lst):
    first = lst[0]
    for i in lst:
        if i != first:
            return False
    return True


def findGameOver(field):
    winLists = [
        [field[0], field[1], field[2]],  # top line
        [field[3], field[4], field[5]],  # center line
        [field[6], field[7], field[8]],  # bottom line
        [field[0], field[3], field[6]],  # left side
        [field[1], field[4], field[7]],  # mid side
        [field[2], field[5], field[8]],  # right side
        [field[0], field[4], field[8]],  # left diagonal
        [field[2], field[4], field[6]],  # right diagonal
    ]

    for lst in winLists:
        if lst[0] != " " and allEqual(lst):
            return lst[0]
    return None


def checkGameOver(field, available):
    winner = findGameOver(field)
    if winner != None:
        system("cls")
        drawField(field)
        print(f"Победили {winner}!")
        return True
    elif len(available) == 0:
        system("cls")
        drawField(field)
        print("Ничья!")
        return True
    return False


field = [" "] * 9
available = [i for i in range(9)]

player = "X"
computer = "O"
gameOver = False
while not gameOver:
    system("cls")
    drawField(field)
    try:
        index = humanMove(available)
    except Exception as e:
        print(e)
        system("pause")
    else:
        field[index] = player
        available.remove(index)
        gameOver = checkGameOver(field, available)

        if not gameOver:
            index = computerMove(available)
            field[index] = computer
            available.remove(index)
            gameOver = checkGameOver(field, available)
