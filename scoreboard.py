from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
puntaje = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.puntaje = 0
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.write(f"Puntos: {self.puntaje} ", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Puntos: {self.puntaje} Mayor Puntaje: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.puntaje > self.highscore:
            self.highscore = self.puntaje
        self.score = 0
        self.update_score()

    def inscrease_score(self):
        self.puntaje += 1
        self.clear()
        self.update_score()

