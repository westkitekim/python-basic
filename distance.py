# [문제] 대권거리
"""
두 도시의 위치를 (x1, y1), (x2, y2) 라고 할 때,
두 도시의 대권거리(d)를 구하시오.

d = radius X arccos(sin(x1) x sin(x2) + cos(x1) X cos(x2) X cos(y1 - y2))

"""
# 수학함수 사용하기
import math

# 경도 위도 입력
x1, y1 = eval(input("첫 번째 도시의 위도와 경도를 입력하세요: "))
x2, y2 = eval(input("두 번째 도시의 위도와 경도를 입력하세요: "))

# acos : 코사인 역함수
# radians : 일반 각도를 컴퓨터가 radian 각도로 변경하는 함수
# \ : 역슬래쉬, 하나의 긴 명령문을 여러개로 끊어줄 때 사용한다
d = 6400 * math.acos(math.sin(math.radians(x1)) * \
    math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * \
    math.cos(math.radians(x2)) * math.cos(math.radians(y1-y2)))

print("두 도시의 대권거리는", d, "km 입니다.")








