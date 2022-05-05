import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen() # para exibir a janela
screen.setup(width=600, height=600) # tamanho da janela
screen.bgcolor("black") # color de fundo da janela
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

#Detectar colisão com a comida
  if snake.head.distance(food) < 15: #Snake possui 20 e a comida 10  
    food.refresh()
    snake.extend() #aumentar o corpo
    scoreboard.increase_score()

#Detectar a colisão com a parede
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

#Detectar a colisão com o próprio corpo
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick() # para janela não fechar automáticamente, só quando o usuário clicar.