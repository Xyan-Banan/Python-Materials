from enum import Enum
import random
from tkinter import *
from enum import Enum


class Gesture(Enum):
    ROCK = "Камень"
    PAPER = "Бумага"
    SCISSORS = "Ножницы"


class Main(Frame):
    letter_side = 40
    letter_spacing = 10
    x_y_gap = letter_side + letter_spacing
    words = ["пума", "трактор", "сосна", "арбуз", "барабанщик", "книга", "выключатель"]
    word = ""
    lives = 6
    lives_images = []

    def __init__(self, root):
        super(Main, self).__init__(root)

        x = 10
        y = 20
        for letter in range(ord("а"), ord("я") + 1):
            btn = Button(root, text=chr(letter), font=("Times New Roman", 15))
            btn.configure(command=lambda l=chr(letter), b=btn: self.btn_click(l, b))
            if (letter - 2) % 5 == 0:
                x = 10
                y += self.x_y_gap
            btn.place(
                x=x, y=y, width=self.letter_side, height=self.letter_side
            )  # детям
            x += self.x_y_gap

        x = 280
        y = -40
        self.img = PhotoImage(file="present.png")
        for i in range(self.lives):
            lbl = Label(root, image=self.img, bg="#fff")
            if i % 2 == 0:
                x = 280
                y += 100
            lbl.place(x=x, y=y)
            self.lives_images.append(lbl)
            x += 110

        self.word = random.choice(self.words)
        self.guess = ["#"] * len(self.word)
        self.lbl = Label(
            root,
            text="".join(self.guess),
            bg="#FFF",
            font=("Times New Roman", 15, "bold"),
            justify="center",
        )
        self.lbl.place(x=10, y=10, width=250)

    def btn_click(self, letter, btn):
        btn["state"] = DISABLED
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guess[i] = letter
            self.lbl["text"] = "".join(self.guess)
        else:
            self.lose_live()

    def lose_live(self):
        self.lives -= 1
        self.lives_images[self.lives].configure(image="")


if __name__ == "__main__":
    root = Tk()
    root.geometry("520x430+200+200")
    root.title("Виселица")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()
