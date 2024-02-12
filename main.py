from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

MAX_RANGE_X = 300
MIN_RANGE_X = -300
MIN_RANGE_Y = -300
MAX_RANGE_Y = 300
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to XD")
screen.tracer(0)
snake_game = Snake()
score = Score()
food = Food()
screen.listen()
screen.onkey(snake_game.right, "Right")
screen.onkey(snake_game.left, "Left")
screen.onkey(snake_game.up, "Up")
screen.onkey(snake_game.down, "Down")
game_status = True

while game_status:

    screen.update()
    time.sleep(0.1)
    snake_game.moving_snake()

    # Detecta la colision con la comida, incremente el punta, actualiza el puntaje, aumenta de tamaño la serpiente

    if snake_game.head.distance(food) < 15:
        score.inscrease_score()
        score.update_score()
        snake_game.add_tail()
        food.refresh()

    # Detecta la colision entre la cabeza y las paredes/limites del juego

    if (snake_game.head.xcor() >= MAX_RANGE_X or snake_game.head.xcor() <= MIN_RANGE_X
            or snake_game.head.ycor() >= MAX_RANGE_Y or snake_game.head.ycor() <= MIN_RANGE_Y):
            score.reset()
            snake_game.reset()

    # Detectamos si hay colision entre la cabeza y la cola

    for tail in snake_game.segments[1::]:
        if snake_game.head.distance(tail) < 10:
            score.reset()
            snake_game.reset()

screen.exitonclick()
