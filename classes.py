from random import random, randint
from turtle import Turtle, Screen
from tkinter import Tk, Button, Label, Entry
# from tkinter import messagebox as mb


class Window:
    """Window for game"""
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def __init__(self):
        self.canvas = Screen()
        self.canvas.title('Street game')
        self.canvas.setup(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.canvas.onkey(self.canvas.bye, 'Escape')
        self.canvas.tracer(0)
        self.canvas.bgpic('tetris1.png')


class Figure(Turtle):
    """Cars for game"""
    def __init__(self):
        super().__init__(shape='square')
        self.up()
        self.shapesize(1.3, 3.5)
        self.color(self.generate_color())
        self.hideturtle()
        self.goto(self.get_random_position())
        self.delta_x = -20

    @staticmethod
    def generate_color():
        color_sq = (random(), random(), random())
        return color_sq

    @staticmethod
    def get_random_position():
        x = randint(-400, 1500)
        y = randint(-270, 330)
        return x, y

    def move(self):
        self.showturtle()
        self.goto(self.xcor() + self.delta_x, self.ycor())

    def lets_start(self):
        self.goto(randint(900, 1500), randint(-270, 330))


class Walker(Turtle):
    """Pedestrian for game"""
    def __init__(self):
        super().__init__(shape='turtle')
        self.up()
        self.seth(90)
        self.shapesize(2.5, 2.5)
        self.color('green')
        self.hideturtle()
        self.goto(0, -380)
        self.showturtle()

    def move_up(self):
        coord0 = self.position()
        self.setposition(coord0[0], coord0[1] + 25)

    def move_down(self):
        coord0 = self.position()
        self.setposition(coord0[0], coord0[1] - 25)

    def move_left(self):
        coord0 = self.position()
        self.setposition(coord0[0] - 25, coord0[1])

    def move_right(self):
        coord0 = self.position()
        self.setposition(coord0[0] + 25, coord0[1])

    def change_color(self):
        self.color(random(), random(), random())


class Inscription:
    """Label with name and level"""
    def __init__(self, name: str, level: int):
        self.inscription = Turtle()
        self.inscription.up()
        self.inscription.goto(-650, 330)
        self.inscription.color('white')
        self.text = f'Name: {name}\nLevel: {level}'
        self.inscription.write(self.text, align="left", font=("Arial", 28, "normal"))
        self.inscription.hideturtle()


class NameAnswer:
    """Ask name before game"""
    def __init__(self):
        self.name = Tk()
        self.name.geometry('400x100+400+200')
        self.name.title('Player name')
        self.entry = Entry(self.name, font=("Arial", 14))
        self.button = Button(self.name, text='Enter', command=self.ask_name, font=("Arial", 14))
        self.label = Label(self.name, text='Enter your name', font=("Arial", 14))
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.player_name = ''
        self.name.mainloop()

    def ask_name(self):
        self.player_name = self.entry.get()
        self.name.destroy()


class EndGame:
    """Announce the end of the game"""
    def __init__(self, level: int):
        self.level = level
        self.endgame = Tk()
        self.endgame.geometry('400x100+400+200')
        self.endgame.title('The end')
        self.label = Label(self.endgame, text=f'The end!\nYour level is {level}', font=("Arial", 14))
        self.label.pack()
        self.endgame.mainloop()




