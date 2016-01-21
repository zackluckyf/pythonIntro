import turtle
#update numsides to change drawing parameters
numsides = 8
for steps in range(numsides):
    turtle.forward(100)
    turtle.right(360/numsides)
    for mosteps in range(numsides):
        turtle.forward(50)
        turtle.right(360/numsides)

turtle.exitonclick()

