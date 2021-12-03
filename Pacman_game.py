#turtle and randomization imports
import turtle as trtl
import turtle as trtl2
import random as rand

#backg
wn = trtl.Screen()
wn.bgpic("pacbackground.gif")

score = 0
font_setup = ("Arial", 20, "normal")
timer = 99
counter_interval = 1000 
timer_up = False

food_balls = trtl.Turtle()
pacman = trtl.Turtle()
redghost = trtl.Turtle()
orangeghost = trtl.Turtle()
blueghost = trtl.Turtle()
pinkghost = trtl.Turtle()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()

all_trtls = [pacman,redghost,orangeghost,blueghost,pinkghost,score_writer,counter,food_balls]
pacman_image = "pacman.gif"
red_image = "redghost.gif"
orange_image = "orangeghost.gif"
blue_image = "blueghost.gif"
pink_image = "pinkghost.gif"

pacman.shape(pacman_image)
redghost.shape(red_image)
orangeghost.shape(orange_image)
blueghost.shape(blue_image)
pinkghost.shape(pink_image)

redghost.penup()
orangeghost.penup()
blueghost.penup()
pinkghost.penup()

#score and counter
score_writer.hideturtle()
score_writer.penup()
score_writer.setposition(160,200)
score_writer.pendown()

counter.hideturtle()
counter.penup()
counter.setposition(-160, 200)
counter.pendown()

# countdown function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    wn.bgpic("gameover.gif")
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# update and display the score
def update_score():
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

#all of the turtle's movements
def draw_food():
  food_balls.circle(1)

def move_up():
  pacman.setheading(90)
  pacman.forward(15)

def move_right():
  pacman.setheading(180)
  pacman.forward(15)

def move_down():
  pacman.setheading(270)
  pacman.forward(15)


def move_left():
  pacman.setheading(360)
  pacman.forward(15)

def red_move():
  redghost.forward(100)
  redghost.right(90)
  redghost.forward(100) 
  redghost.left(90)   
  redghost.forward(100)
  redghost.right(90)
  redghost.forward(100) 
  redghost.left(90)   
  redghost.right(180)
  redghost.forward(100)
  redghost.right(90)
  redghost.forward(100) 
  redghost.left(90)   
  redghost.forward(100)
  redghost.right(90)
  redghost.forward(100) 
  redghost.left(90)  
  redghost.forward(100)
  redghost.right(90)
  redghost.forward(100) 
  redghost.left(90)   
  redghost.forward(100)
  redghost.right(90)
  redghost.forward(100) 
  redghost.left(90)    
  redghost.right(180)

def orange_move():
  orangeghost.setposition(-200,200)
  orangeghost.forward(400)
  orangeghost.right(90)
  orangeghost.forward(400)
  orangeghost.right(90)
  orangeghost.forward(400)
  orangeghost.right(90)
  orangeghost.forward(400)
  orangeghost.right(90)

blueghost.right(180)

def blue_move():
  blueghost.forward(100)
  blueghost.left(90)  
  blueghost.forward(100) 
  blueghost.right(90)   
  blueghost.forward(100)
  blueghost.left(90) 
  blueghost.forward(100) 
  blueghost.right(90)   
  blueghost.right(180)
  blueghost.forward(100)
  blueghost.left(90) 
  blueghost.forward(100) 
  blueghost.right(90)  
  blueghost.forward(100)
  blueghost.left(90) 
  blueghost.forward(100) 
  blueghost.right(90)
  blueghost.forward(100)
  blueghost.left(90) 
  blueghost.forward(100) 
  blueghost.right(90)  
  blueghost.forward(100)
  blueghost.left(90) 
  blueghost.forward(100) 
  blueghost.right(90)  
  blueghost.right(180)

pinkghost.forward(200)

def pink_move():
  pinkghost.right(180)
  pinkghost.forward(400)

for i in range():
  red_move()

for i in range():
  orange_move

for i in range():
  blue_move

for i in range():
  pink_move

for i in range():
  draw_food()
  
#responsive code segment
wn.onkeypress(move_up,"w")
wn.onkeypress(move_down,"s")
wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")
wn.listen()


wn.bgpic("gameover.gif")
wn.exitonclick()
wn.mainloop()
#end