import turtle as trtl
import turtle as trtl2
import random as rand
wn = trtl.Screen()
wn.bgpic("pacbackground.gif")


food_balls = trtl2.Turtle()

pacman = trtl.Turtle()
redghost = trtl.Turtle()
orangeghost = trtl.Turtle()
blueghost = trtl.Turtle()
pinkghost = trtl.Turtle()

all_trtls = [pacman,redghost,orangeghost,blueghost,pinkghost]

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
    redghost.forward(15)
    redghost.right(90)
    redghost.forward(15) 
    redghost.left(90)   
    redghost.right(180)
    redghost.forward(15)
    redghost.left(90)
    redghost.forward(15) 
    redghost.right(90)   
    redghost.right(180)

for i in range():
  draw_food()
  

wn.onkeypress(move_up,"w")
wn.onkeypress(move_down,"s")
wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")


wn.bgpic("gameover.gif")

wn.mainloop()