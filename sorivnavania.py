import turtle
import random



turtle_blue = random.randint(-25, 25)
turtle_red = random.randint(-25, 25)
turtle_green = random.randint(-25, 25)
turtle_yellow = random.randint(-25, 25)
turtle_grey = random.randint(-25, 25)

helper_turtle = turtle.Turtle()  
helper_turtle.color("#8291b8")
helper_turtle.up()
helper_turtle.goto(0,208)
helper_turtle.down()

t1 = turtle.Turtle()
t1.shape("turtle")  
t1.color("blue")
t2 = turtle.Turtle()
t2.shape("turtle")  
t2.color("red")
t2.up()
t2.goto(0,-45)
t2.down()

t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("green")
t3.up()
t3.goto(0,30)
t3.down()

t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("#696969")
t4.up()
t4.goto(0,-80)
t4.down()

t5 = turtle.Turtle()
t5.shape("turtle")
t5.color("#ffc400")
t5.up()
t5.goto(0,-120)
t5.down()
for i in range(30):
 t1.forward(turtle_blue)
 t2.forward(turtle_red )
 t1.speed(turtle_blue)
 t2.speed(turtle_red )
 t3.forward(turtle_green)
 t3.speed(turtle_green)
 t4.forward(turtle_grey)
 t4.speed(turtle_grey)
 t5.forward(turtle_yellow)
 t5.speed(turtle_yellow)
 

# list_for_podion = [turtle_blue, turtle_red, turtle_green, turtle_grey, turtle_yellow]
list_for_number = [1, 2, 3, 4, 5]

print(list_for_number[0], '\n', list_for_number[1], "\n",list_for_number[2], "\n",list_for_number[3], "\n",list_for_number[4])

if turtle_blue > turtle_red and turtle_blue > turtle_green and turtle_blue > turtle_grey and turtle_blue > turtle_yellow:
     print("Поздровляю синия черепашка победила 🥳🐢")
     helper_turtle.color("blue")
     helper_turtle.write("Поздровляю синия черепашка победила 🥳🐢", move=False, align="center", font=("Arial", 30, "normal")) 
   # helper_turtle.begin_fill("white")
   # helper_turtle.end_fill()

elif turtle_red > turtle_blue and turtle_red > turtle_green and turtle_red > turtle_grey and turtle_red > turtle_yellow:
    helper_turtle.color("red")
    helper_turtle.write("Поздровляю крастная черепашка победила 🥳🐢", move=False, align="center", font=("Arial", 45, "normal"))
    
elif turtle_green > turtle_red and turtle_blue < turtle_green and turtle_green > turtle_grey and turtle_green > turtle_yellow:
     helper_turtle.color("green")
     helper_turtle.write("Поздровляю зелённая черепашка победила 🥳🐢", move=False, align="center", font=("Arial", 45, "normal"))
     

elif turtle_grey > turtle_red and turtle_grey > turtle_green and turtle_green < turtle_grey and turtle_grey > turtle_yellow:
     helper_turtle.color("#696969")
     helper_turtle.write("Поздровляю серая черепашка победила 🥳🐢", move=False, align="center", font=("Arial", 45, "normal"))
     

elif turtle_yellow > turtle_red and turtle_yellow > turtle_green and turtle_green < turtle_yellow and turtle_grey < turtle_yellow:
    helper_turtle.color("#ffc400")
    helper_turtle.write("Поздровляю жёлтая черепашка победила 🥳🐢", move=False, align="center", font=("Arial", 45, "normal"))
   

    


turtle.done()