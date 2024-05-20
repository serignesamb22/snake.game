import turtle
import time
import random

# Step1: Setting up the screen:
# set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=300)
            
            
# step2: Create the snake head
head = turtle.Turtle()
# head = turtle.Screen()
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0) #postions the snake on the center
head.direction = "stop"


#step3: control the snake's direction
def go_up():
  if head.direction != "down":
     head.direction = "up"
    
  
def go_down():
  if head.direction != "up":
    head.direction = "down"
    

def go_left():
  if head.direction != "right":
    head.direction = "left"


def go_right():
  if head.direction != "left":
    head.direction = "right"

#step4: Move the snake
def move():
  if head.direction == "up":
    y = head.ycor()  
    head.sety(y + 20)
  elif head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)
  elif head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)
  elif head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)
    

#keybord bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


#step6: Create the food for the snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange") 
food.penup()
#makes the fruit appear inside the game window
food.goto(random.randint(-290, 290), 
          random.randint(-290, 290))

#Step7: Main Game Loop
#Step8: Grow the snake
segments = []


def add_segment():
  new_segment = turtle.Turtle()
  new_segment.speed(0)
  new_segment.shape("circle")
  new_segment.color("green")
  new_segment.penup()
  segments.append(new_segment) # add a new segment to  snake

 #update while loop after step 8 -> step-9


# Main game loop
while True:
  screen.update()
  
  #Step10: Check if contact with wall and display "You Lose" 
  if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

 # hide the segments
  for segment in segments:
      segment.goto(1000, 1000)

   # Clear the segments
      segments.clear()
     # head.write("You Lost" , align="center", font=("Arial", 24,"normal"))

 # Check for collision with food
  if head.distance(food) < 20:  
      # Move the food to a random spot
      food.goto(random.randint(-290, 290), random.randint(-290, 290))
      # Add a segment
      add_segment()

 # Move the end segments first in reverse order
      for index in range(len(segments) - 1, 0, -1):
          x = segments[index - 1].xcor()
          y = segments[index - 1].ycor()
          segments[index].goto(x, y)

   # Move segment 0 to where the head is
      if len(segments) > 0:
          x = head.xcor()
          y = head.ycor()
          segments[0].goto(x, y)

  move()
  time.sleep(0.1)

  
      
  
    