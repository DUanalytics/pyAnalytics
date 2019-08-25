#Topic:
#-----------------------------
#libraries
#https://stackoverflow.com/questions/29065209/drawing-a-indian-flag-chakra-in-python-turtlee
#method1
import turtle
def drawRectangle (t, l, b, c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(2):
        t.forward(b)
        t.left(90)
        t.forward(l)
        t.left(90)
    t.end_fill()


def main ():
   wn = turtle.Screen()
   india = turtle.Turtle()
   drawRectangle(india,50,200, "orange1")
   india.up()
   india.goto(0,-100)
   india.down()
   drawRectangle(india,50,200, "green")
   india.up()
   india.goto(100,-20)
   india.down()
   india.pencolor("blue3")

   for i in range(24):
    india.forward(20)
    india.backward(20)
    india.left(15)
    india.up()
    india.goto(400,400)

main()





#Method2
#https://www.pythoncircle.com/post/662/python-script-12-drawing-indian-national-flag-tricolor-using-python-turtle/


import turtle
import time

# create a screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("#b3daff")
# set tile of screen
screen.title("Indian Flag - https://www.pythoncircle.com")
# "Yesterday is history, tomorrow is a mystery, 
# but today is a gift. That is why it is called the present.”
# — Oogway to Po, under the peach tree, Kung Fu Panda Movie
oogway = turtle.Turtle()
# set the cursor/turtle speed. Higher value, faster is the turtle
oogway.speed(100)
oogway.penup()
# decide the shape of cursor/turtle
oogway.shape("turtle")

# flag height to width ratio is 2:3
flag_height = 300
flag_width = 450

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -225
start_y = 150

# For saffron, white and green stripes. each strip width will be flag_height/3 = 100
stripe_height = flag_height/3
stripe_width = flag_width

# Radius of Ashok Chakra, half of white stripe 
chakra_radius = stripe_height / 2


def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()


# this function is used to create 3 stripes
def draw_stripes():
    x = start_x
    y = start_y
    # we need to draw total 3 stripes, 1 saffron, 1 white and 1 green
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#FF9933")
    # decrease value of y by stripe_height
    y = y - stripe_height   
    # create middle white stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height               

    # create last green stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#138808')
    y = y - stripe_height


def draw_chakra():
    oogway.speed(1)
    oogway.goto(0,0)
    color = "#000080" # navy blue
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(0, 0 - chakra_radius)
    oogway.pendown()
    oogway.circle(chakra_radius)
    # draw 24 spikes in chakra
    for _ in range(24):
        oogway.penup()
        oogway.goto(0,0)
        oogway.left(15)
        oogway.pendown()
        oogway.forward(chakra_radius)
  
    

# start after 5 seconds.
time.sleep(0)
# draw 3 stripes
draw_stripes()
# draw squares to hold stars
draw_chakra()
# hide the cursor/turtle
oogway.hideturtle()
# keep holding the screen until closed manually
screen.mainloop()