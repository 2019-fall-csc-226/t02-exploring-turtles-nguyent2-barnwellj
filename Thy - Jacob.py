import turtle
# Citation: https://docs.python.org/3/library/turtle.html
# Get color(), pensize(), write() from this website.
#Citation: https://www.w3schools.com/colors/colors_picker.asp
# Get background color from the website

wn = turtle.Screen()
thy = turtle.Turtle()
jacob = turtle.Turtle()

wn.bgcolor("#99ffff")
thy.color("red")
jacob.color("green")
jimmy = turtle.Turtle()
jimmy2 = turtle.Turtle()

jacob.pensize(3)
thy.pensize(3)
jacob.right(90)
jacob.forward(70)
for i in range(4):
    jacob.left(-45)
    jacob.forward(10)

jacob.penup()
jacob.right(90)
jacob.forward(50)
jacob.right(90)
jacob.forward(15)
jacob.stamp()
jacob.left(90)
jacob.forward(30)
jacob.pendown()
jacob.left(90)
jacob.forward(70)
jacob.right(90)
for i in range (5):
    jacob.right(30)
    jacob.forward(10)
jacob.right(210)
for j in range (5):
    jacob.right(30)
    jacob.forward(10)

jacob.penup()
jacob.right(30)
jacob.right(180)
jacob.forward(50)
thy.penup()
thy.forward(100)
thy.pendown()
thy.forward(100)
thy.forward(-50)
thy.right(90)
thy.forward(80)
thy.penup()
thy.left(90)
thy.forward(50)
thy.stamp()
thy.forward(30)
thy.pendown()
thy.left(90)
thy.forward(80)
thy.right(135)
thy.forward(100)
thy.left(135)
thy.forward(80)
jimmy.penup()
jimmy.left(90)
jimmy.forward(200)
jimmy.write("Jacob was born in the year of Rabbit.", move=False, align="left", font=("Arial", 14, "normal"))
jimmy2.penup()
jimmy2.left(90)
jimmy2.forward(80)
jimmy2.write("Thy was born in 2000,\n but in the Chinese calendar, \nThy was born in 1999, \nwhich was the year of Rabbit.",
             move = False, align = "left", font = ("TimesNewRoman", 14, "normal"))
wn.exitonclick()