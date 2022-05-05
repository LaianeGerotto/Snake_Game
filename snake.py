from turtle import Turtle

#Constantes
STARTING_POSITIONS = [(0,0), (-20, 0), (-40,0)] #primeiras posições
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
      self.segments = []
      self.create_snake()
      self.head = self.segments[0]

    
  #Criar o corpo da Snake
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  #adicionar segmento(corpo)
  def add_segment(self, position):
    new_segment = Turtle(shape="square") # Define o formato 
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)


  #Aumentar o tamanho do corpo conforme encontra a comida
  def extend(self):
    self.add_segment(self.segments[-1].position())


  #Mover a Snake
  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)    
    self.head.forward(MOVE_DISTANCE)
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)



