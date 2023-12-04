from turtle import Turtle, Screen, onkey, listen

bia = Turtle()
tela = Screen()
bia.pensize(3)
Screen().bgcolor('gray')

# função para pular.
def pular(x, y):
    bia.penup()
    bia.goto(x, y)
    bia.pendown()

# função do tabuleiro.
def jdv():
    bia.pencolor('white')
    bia.forward(300)
    pular(300, 100)
    bia.backward(300)
    pular(100, 200)
    bia.goto(100, -100)
    pular(200, 200)
    bia.goto(200, -100)
jdv()

# Função para centralizar.
def centralizar():
    x_atual = bia.xcor()
    novo_x = x_atual - (x_atual % 100) + 50
    y_atual = bia.ycor()    
    novo_y = y_atual - (y_atual % 100) + 50
    bia.goto(novo_x, novo_y)

# função do X.
def xis():
    centralizar()
    bia.pencolor('blue')
    bia.pendown()
    bia.left(45)
    bia.forward(45)
    bia.backward(90)
    bia.forward(45)
    bia.right(90)
    bia.forward(45)
    bia.backward(90)
    bia.forward(45)
    bia.setheading(360)

# função do O:    
def circulo():
    centralizar()
    bia.pencolor('purple')
    bia.setheading(90)
    bia.forward(-40)
    bia.pendown()
    bia.setheading(360)
    bia.circle(40) 
   
# Funções para movimentar usando as teclas cima, baixo, esquerda, direita.
def up():
    bia.penup()
    y_atual = bia.ycor()
    novo_y = y_atual + 40
    bia.sety(novo_y)

def down():
    bia.penup()
    y_atual = bia.ycor()
    novo_y = y_atual - 40
    bia.sety(novo_y)

def left():
    bia.penup()
    x_atual = bia.xcor()
    novo_x = x_atual - 40
    bia.setx(novo_x)

def right():
    bia.penup()
    x_atual = bia.xcor()
    novo_x = x_atual + 40
    bia.setx(novo_x)

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')
onkey(xis, 'x')
onkey(circulo, 'o')
listen()
tela.mainloop()