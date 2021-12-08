import turtle

turtle.pensize(3) # 펜의 굵기를 3필셀로 설정한다.
turtle.penup() # 펜을 들어 올린다.
turtle.goto(-200, -50)
turtle.pendown() # 펜을 내려 놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작한다.
turtle.color("red")
turtle.setheading(60) # 회전한다
turtle.circle(40, steps=3) # 삼각형을 그린다.
turtle.end_fill() # 도형을 채운다.

turtle.penup() # 펜을 들어 올린다.
turtle.goto(-100, -50)
turtle.pendown() # 펜을 내려 놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작한다.
turtle.color("blue")
turtle.setheading(45) # 회전한다
turtle.circle(40, steps=4) # 사각형을 그린다.
turtle.end_fill() # 도형을 채운다.

turtle.penup() # 펜을 들어 올린다.
turtle.goto(0, -50)
turtle.pendown() # 펜을 내려 놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작한다.
turtle.color("green")
turtle.setheading(35) # 회전한다
turtle.circle(40, steps=5) # 사각형을 그린다.
turtle.end_fill() # 도형을 채운다.

turtle.penup() # 펜을 들어 올린다.
turtle.goto(100, -50)
turtle.pendown() # 펜을 내려 놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작한다.
turtle.color("yellow")
turtle.setheading(30) # 회전한다
turtle.circle(40, steps=6) # 육각형을 그린다.
turtle.end_fill() # 도형을 채운다.

turtle.penup() # 펜을 들어 올린다.
turtle.goto(200, -50)
turtle.pendown() # 펜을 내려 놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작한다.
turtle.color("purple")
turtle.setheading(25) # 회전한다
turtle.circle(40, steps=8) # 원을 그린다.
turtle.end_fill() # 도형을 채운다.











