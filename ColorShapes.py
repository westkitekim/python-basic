import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
"""
steps 라는 것은 몇 개의 점으로 원을 그리라는 것
삼각형 그릴때도 circle 사용한다
steps = 3은 3개의 점으로 원을 그리라는 것인데, 

"""
turtle.circle(40, steps=3) # 삼각형을 그린다.
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps=4) # 사각형을 그린다

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.pendown()
turtle.circle(40, steps = 5) # 오각형을 그린다

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.pendown()
turtle.circle(40, steps = 6) # 육각형을 그린다

# 원 그릴 때는 steps 값 없음
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.pendown()
turtle.circle(40) # 원을 그린다









