from turtle import *
import requests
import json
import csv
import matplotlib.pyplot as plt
import numpy as np


with open("YA_Flavors.csv", mode = "r") as flavorFile:
    # mode "r" = read
    # "as" renames the function to a simple name

    flavors = csv.reader(flavorFile)
    next(flavors)
    # methods
    def findCal(RequestedCal):
        for item in flavors:
            flavor = item[0]
            cal = item[1]
            if flavor == RequestedCal:
                return int(cal)
        return 0 # backup number incase if the requested flavor isnt in the csv
    def calories():
        goto(91,-106)
        seth(0)
        pendown()
        color("black")
        for i in range(2):
            forward(100)
            left(90)
            forward(25)
            left(90)
        goto(90,-105)
        begin_fill()
        for i in range(2):
            forward(100)
            left(90)
            forward(25)
            left(90)
        color("white")
        end_fill()
        penup()
        color("Maroon")
        goto(101,-101)
        write(f"calories: {cal[0]+cal[1]+cal[2]+cal[3]}", font=MenuFont)
        color("Red")
        goto(100,-100)
        write(f"calories: {cal[0]+cal[1]+cal[2]+cal[3]}", font=MenuFont)
    def iceCream(flavor):
        color("black")
        seth(180)
        penup()
        forward(30)
        pendown()
        begin_fill()
        circle(15,270)
        right(180)
        circle(15,180)
        right(180)
        circle(15,270)
        seth(60)
        circle(35,240)
        color(flavor)
        end_fill()
        penup()

    def moveUp():
        seth(90)
        setx(0)
        forward(50)
    def click_handler(x, y):
        if movable[0]:
            movable.append(False)
            movable.pop(0)
            penup()
            if x > -225 and x < -125:
                if y < 100 and y > -100:
                    if y < -60:
                        selection.append(Strawberry)
                        cal.append(StrawberryCal)
                    elif y < -35:
                        selection.append(Smores)
                        cal.append(SmoresCal)
                    elif y < -10:
                        selection.append(Banana)
                        cal.append(BananaCal)
                    elif y < 15:
                        selection.append(Velvet)
                        cal.append(VelvetCal)
                    elif y < 40:
                        selection.append(Mint)
                        cal.append(MintCal)
                    elif y < 65:
                        selection.append(Vanilla)
                        cal.append(VanillaCal)
                    else:
                        selection.append(Chocolate)
                        cal.append(ChocolateCal)
                    selection.pop(0)
                    cal.pop(0)
                    print(cal)
                    calories()
                    goto(0,-80)
                    if selection[0] != "maroon":
                        iceCream(selection[0])
                        moveUp()
                    if selection[1] != "maroon":
                        iceCream(selection[1])
                        moveUp()
                    if selection[2] != "maroon":
                        iceCream(selection[2])
                        moveUp()
                    if selection[3] != "maroon":
                        iceCream(selection[3])
                        moveUp()
        
            goto(x, y)
            color("cyan")
            seth(135)
            movable.append(True)
            movable.pop(0)
    # flavor colors
    Chocolate = "#7a4104"
    Vanilla = "#fffce3"
    Mint = "#66ffcc"
    Velvet = "#ff4d4d"
    Banana = "#fcf090"
    Smores = "#d2a679"
    Strawberry = "#ffb6c1"
    # flavor calories
    ChocolateCal = findCal("Chocolate")
    VanillaCal = findCal("Vanilla")
    MintCal = findCal("Mint Chocolate Cookie")
    VelvetCal = findCal("Red Velvet Cake")
    BananaCal = findCal("Banana Split")
    SmoresCal = findCal("S'mores")
    StrawberryCal = findCal("Strawberry Cheesecake")
    print([ChocolateCal,VanillaCal,MintCal,VelvetCal,BananaCal,SmoresCal,StrawberryCal])
    # placeholder selection
    selection = ["maroon","maroon","maroon","maroon"]
    cal = [0,0,0,0]
    # validation
    movable = [False]
    # setup
    speed(0)
    setup(500,400)
    showturtle()
    goto(0,0)
    turtlesize(2)
    title("Gibby")
    pensize(4)
    # background
    bgcolor("#cc0000")
    bgLines = -275
    while bgLines < 250:
        penup()
        goto(bgLines,-250)
        seth(90)
        pendown()
        forward(500)
        bgLines += 80
        penup()
    # title
    TitleFont = ("Impact", 20, "bold", "italic")
    color("black")
    goto(-148, 148)
    write("Gibby's Ice Cream Specal ", font=TitleFont)
    color("white")
    goto(-152, 152)
    write("Gibby's Ice Cream Specal ", font=TitleFont)
    # menu
    goto(-223,98)
    seth(-90)
    pendown()
    color("black")
    for i in range(2):
        forward(200)
        left(90)
        forward(100)
        left(90)
    goto(-225,100)
    seth(-90)
    begin_fill()
    for i in range(2):
        forward(200)
        left(90)
        forward(100)
        left(90)
    color("white")
    end_fill()
    MenuFont = ("Monospace", 10, "bold",)
    penup()

    color("Maroon")
    goto(-214,69)
    write("Chocolate", font=MenuFont)
    color("Red")
    goto(-215,70)
    write("Chocolate", font=MenuFont)

    color("Maroon")
    goto(-214,44)
    write("Vanilla", font=MenuFont)
    color("Red")
    goto(-215,45)
    write("Vanilla", font=MenuFont)

    color("Maroon")
    goto(-214,19)
    write("Mint", font=MenuFont)
    color("Red")
    goto(-215,20)
    write("Mint", font=MenuFont)

    color("Maroon")
    goto(-214,-5)
    write("Red Velvet", font=MenuFont)
    color("Red")
    goto(-215,-5)
    write("Red Velvet", font=MenuFont)

    color("Maroon")
    goto(-214,-31)
    write("Banana", font=MenuFont)
    color("Red")
    goto(-215,-30)
    write("Banana", font=MenuFont)

    color("Maroon")
    goto(-214,-56)
    write("Smores", font=MenuFont)
    color("Red")
    goto(-215,-55)
    write("Smores", font=MenuFont)

    color("Maroon")
    goto(-214,-81)
    write("Strawberry", font=MenuFont)
    color("Red")
    goto(-215,-80)
    write("Strawberry", font=MenuFont)

    color("black")
    goto(-214,-121)
    write("max of 4", font=MenuFont)
    color("white")
    goto(-215,-120)
    write("max of 4", font=MenuFont)

    # cone
    penup()
    goto(0,-100)
    pendown()
    seth(0)
    color("black")
    begin_fill()
    forward(40)
    right(120)
    forward(80)
    right(120)
    forward(80)
    right(120)
    forward(40)
    color("#d2691e")
    end_fill()
    penup()

    '''
    # test
    goto(0,-80)
    iceCream("green")
    goto(0,-30)
    iceCream("blue")
    goto(0,20)
    iceCream("orange")
    goto(0,70)
    iceCream("purple")
    '''


    # player input
    penup()
    seth(135)
    goto(0,0)
    color("cyan")
    movable = [True]
    onscreenclick(click_handler)
    done()
