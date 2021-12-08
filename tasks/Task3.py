import math
a, b, c = eval(input("a, b, c의 값을 입력하세요: "))
if ((b * b) - 4 * a * c) > 0:
    value1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
    value2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
    print("실수 해는 ", value1, "과/와 ", value2, "입니다.")
elif ((b * b) - 4 * a * c) == 0:
    value1 = -b / 2 * a
    print("실수 해는 ", value1, "입니다.")
else:
    print("이 방정식의 실수 해 존재하지 않습니다.")

