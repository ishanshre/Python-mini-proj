import turtle # a built in 2d graphics module in python
import time
import random
WIDTH, HEIGHT = 500, 500 # define a constant height and width for the screen
COLOR = ["red","black","green","cyan","purple","blue","orange","yellow","pink","brown"]
def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1) 
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) # by default the arrow are pointed to the right. So to move upward we need to change the difection to left by 90 degrees
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)* spacingx, -HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                time.sleep(3)
                return colors[turtles.index(racer)]


def init_turtle():
    screen = turtle.Screen() # initialize a Screen object from tutle module
    screen.setup(WIDTH, HEIGHT) # setup a screen with height and width
    screen.title("Python Turtle Racing Game") # change the name in the title bar of the windows screen


def get_no_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter the number of racers in integers from 2 to 10")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Please the racers must be between 2 to 10")

racers = get_no_of_racers()
init_turtle() # initialize the turtle function or turtle screen
random.shuffle(COLOR)
colors = COLOR[:racers]
winner = race(colors)
print("Winner is turtle with color: ", winner)
# racer = turtle.Turtle()
# racer.speed(1)
# racer.shape("turtle")
# racer.color("purple")
# racer.forward(100) # forward the turtle by 100 pxels
# racer.left(90)
# racer.forward(100)# 90 , 100 are the angle we turn the line 
# racer.left(90)
# racer.backward(100)
# time.sleep(5)