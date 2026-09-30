from turtle import *
# flavor colors
Chocolate = "#7a4104"
Vanilla = "#fffce3"
Mint = "#66ffcc"
Strawberry = "#ff4d4d"
Banana = "#fcf090"
Coffee = "#d2a679"
BubbleGum = "#ffb6c1"
# placeholder selection
selection = ["maroon","maroon","maroon","maroon"]
# validation
movable = [True]
# methods
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
                if y < -65:
                    selection.append(BubbleGum)
                elif y < -40:
                    selection.append(Coffee)
                elif y < -15:
                    selection.append(Banana)
                elif y < 10:
                    selection.append(Strawberry)
                elif y < 35:
                    selection.append(Mint)
                elif y < 60:
                    selection.append(Vanilla)
                else:
                    selection.append(Chocolate)
                selection.pop(0)
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
# setup
speed(0)
setup(500,500)
showturtle()
goto(0,0)
turtlesize(2)
title("Gibby")
pensize(4)
# background
bgcolor("maroon")
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
color("white")
TitleFont = ("Monospace", 20, "bold", "italic")
goto(-150, 150)
write("Gibby's Ice Cream Specal", font=TitleFont)
# menu
goto(-225,100)
seth(-90)
pendown()
color("black")
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
color("Red")
goto(-215,70)
write("Chocolate", font=MenuFont)
goto(-215,45)
write("Vanilla", font=MenuFont)
goto(-215,20)
write("Mint", font=MenuFont)
goto(-215,-5)
write("Strawberry", font=MenuFont)
goto(-215,-30)
write("Banana", font=MenuFont)
goto(-215,-55)
write("Coffee", font=MenuFont)
goto(-215,-80)
write("Bubble Gum", font=MenuFont)

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
onscreenclick(click_handler)
done()