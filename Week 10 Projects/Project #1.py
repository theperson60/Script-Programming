#Define a function drawCricle. This function should expect a Turtle object,
#the coordinates of the circle's center point, and the circle's radius as arguments.
#The function should draw the specified circle. The algorithm should draw the circle's
#circumference by turning 3 degrees and moving a given distance 120 times. Calculate
#the distance moved with the formula 2.0 * pi * radius / 120.0

import turtle
import math

def drawCircle(t, x, y, radius):
    #Calculate distance
    distance = 2.0 * math.pi * radius / 120.0

    #Move pointer to x and y coordinates
    t.penup()
    t.setposition(x, y)

    #Pen back down so it can draw
    t.pendown()

    for k in range(120):
        #Go forward distance and turn 3 degrees each iteration
        t.forward(distance)
        t.right(3)

def main():
    #Get info from user
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    radius = int(input("Enter the radius: "))

    t = turtle.Turtle()

    #Call drawCircle function
    drawCircle(t, x, y, radius)

main()
