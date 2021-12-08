"""
[문제] 뺄셈 퀴즈 프로그램
- 뺄셈 퀴즈를 출제하고 정답 여부를 출력하는 프로그램을 작성하시오.
"""
import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    # number1과 number2의 값 switch
    number1, number2 = number2, number1

answer = eval(input(str(number1) + " - " + str(number2) + \
                    "은/는 얼마입니까? "))

print(str(number1) + " - " + str(number2) + " = " + str(answer) + \
      "은/는", number1 - number2 == answer, "입니다.")







