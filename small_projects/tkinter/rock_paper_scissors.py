from enum import Enum
import random
from tkinter import *
from enum import Enum


class Gesture(Enum):
    ROCK = "Камень"
    PAPER = "Бумага"
    SCISSORS = "Ножницы"


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        rock_btn = Button(
            root,
            text="Камень",
            font=("Times New Roman", 15),
            command=lambda x=Gesture.ROCK: self.btn_click(x),
        )
        scissors_btn = Button(
            root,
            text="Ножницы",
            font=("Times New Roman", 15),
            command=lambda x=Gesture.SCISSORS: self.btn_click(x),
        )
        paper_btn = Button(
            root,
            text="Бумага",
            font=("Times New Roman", 15),
            command=lambda x=Gesture.PAPER: self.btn_click(x),
        )

        rock_btn.place(x=10, y=120, width=120, height=50)  # детям
        scissors_btn.place(x=155, y=120, width=120, height=50)  # детям
        paper_btn.place(x=300, y=120, width=120, height=50)  # детям

        self.info_lbl = Label(
            root,
            text="Начало игры!",
            bg="#FFF",
            font=("Times New Roman", 21, "bold"),
            justify="center",
        )
        self.info_lbl.place(x=150, y=10, width=270)

        self.win = self.draw = self.lose = 0

        self.stats = Label(
            root,
            justify="left",
            font=("Times New Roman", 13),
            text=f"Побед: {self.win}\nПроигрышей:" f" {self.lose}\nНичей: {self.draw}",
            bg="#FFF",
        )
        self.stats.place(x=5, y=5)

    def btn_click(self, choice):
        comp_choise = random.choice(list(Gesture))  # детям 2
        self.info_lbl["text"] = f"Компьютер выбрал:\n{comp_choise.value}"

        if choice == comp_choise:  # детям
            self.draw_game()
        elif choice == Gesture.ROCK:
            if comp_choise == Gesture.SCISSORS:
                self.win_game()
            else:
                self.lose_game()
        elif choice == Gesture.SCISSORS:
            if comp_choise == Gesture.PAPER:
                self.win_game()
            else:
                self.lose_game()
        elif choice == Gesture.PAPER:
            if comp_choise == Gesture.ROCK:
                self.win_game()
            else:
                self.lose_game()

        self.update_stats()
        del comp_choise

    def win_game(self):
        self.win += 1

    def lose_game(self):
        self.lose += 1

    def draw_game(self):
        self.draw += 1

    def update_stats(self):
        self.stats[
            "text"
        ] = f"Побед: {self.win}\nПроигрышей: {self.lose}\nНичей: {self.draw}"


if __name__ == "__main__":
    root = Tk()
    root.geometry("430x180+200+200")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()
