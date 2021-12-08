import math

x1, y1, x2, y2, x3, y3 = eval(input("세 점을 입력하시오"))

a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y2) * (y1 - y2))
# 파이썬의 삼각함수는 radius를 사용하기 때문에 사람이 사용하는 각도로 바꿔주는 degrees
# 함수를 사용한다
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

# 콤마 , 는 한칸 띄워주고 문자를 연속해서 출력한다 
print("세 내각은 ", round(A * 100) / 100.0, round(B * 100) / 100.0, round(C * 100) / 100.0, "입니다. ")




























