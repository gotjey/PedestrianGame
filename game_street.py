from classes import Figure, Walker, Window, Inscription, NameAnswer, EndGame
from playsound import playsound #pip install playsound==1.2.2


class Game:
    """Main class of game"""
    def __init__(self, name: str):
        self.name = name
        self.window = Window()
        self.figures = [Figure() for _ in range(50)]
        self.walker = Walker()
        self.level = 1
        self.inscription = Inscription(self.name, self.level)

    def move_walker(self):
        self.window.canvas.onkey(self.walker.move_up, 'Up')
        self.window.canvas.onkey(self.walker.move_down, 'Down')
        self.window.canvas.onkey(self.walker.move_left, 'Left')
        self.window.canvas.onkey(self.walker.move_right, 'Right')
        self.window.canvas.onkey(self.walker.change_color, 'space')

    def run_rectangle(self):
        # self.name = self.name_answer.get_name()
        # self.inscription = Inscription(self.name, self.level)
        while True:
            self.move_walker()
            self.window.canvas.listen()
            for figure in self.figures:
                figure.move()
                if figure.xcor() < -900:
                    figure.lets_start()
                if self.walker.distance(figure) < 40:
                    self.walker.color('red')
                    self.walker.shapesize(200, 200)
                    EndGame(self.level)
                self.new_level()
                self.window.canvas.update()

    def new_level(self):
        if self.walker.ycor() > 380:
            playsound('pisk.mp3')
            self.level += 1
            self.inscription.inscription.clear()
            self.walker.hideturtle()
            self.walker.goto(0, -380)
            self.walker.showturtle()
            self.inscription = Inscription(self.name, self.level)
            for figure in self.figures:
                figure.delta_x -= 20


name = NameAnswer()
game = Game(name.player_name)
game.run_rectangle()
