#nastakhdmo maktabat turtul li rai fi python
import turtle
#dpk nakhadmo screen ta3 el lo3ba ta3na
#Screen jaya fi turtul tmadalna windows ta3 joue
wind=turtle.Screen()
#dok nmado titre ll jue ta3na nastakhadmo title li fi turtule
wind.title("ping pong by fati")
#dok nmado color ll screen ta3na
wind.bgcolor("black")
# dok tol and 3ard ta3 screen ta3na
wind.setup(width=800,height=600)
# dok ha nhaddo bli hna li nathakmo fi update ta3 screen ta3na
wind.tracer(0)

# madrab 1
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")#el chakl ta3 madrab1
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5,stretch_len=1)
madrab1.penup()#bah matkhalich nkat motakati3a moraha
madrab1.goto(-350,0)#i7dathaite
#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")#el chakl ta3 madrab1
madrab2.color("RED")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()#bah matkhalich nkat motakati3a moraha
madrab2.goto(350,0)#i7dathaite
#BALL
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2
#function
def madrab1_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)
    #################
def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)

# fonction 2
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


#kybord seting
wind.listen()#bli i7timal daght 3ala al azrar
wind.onkeypress(madrab1_up,"w")# lama nadaghto 3la azrar tatla3 llfo9
wind.onkeypress(madrab1_down,"s")#lama nadaghto 3la azrar tahbat lta7t

wind.onkeypress(madrab2_up,"Up")# lama nadaghto 3la azrar tatla3 llfo9
wind.onkeypress(madrab2_down,"Down")# lama nadaghto 3la azrar tatla3 llfo9


#main game  loops
while True:
# klma while ykhdam chcha ha thadath ro7ha tbda mn jdid
     wind.update()
     ball.setx(ball.xcor()+ball.dx)
     ball.sety(ball.ycor() + ball.dy)

