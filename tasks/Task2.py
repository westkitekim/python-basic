# 202034-154529 컴퓨터과학과 김서연
import math

total = eval(input("총액을 입력하세요(예, 111573): "))
print("입력하신 금액 ", total, "원 은")
green = total // 10000
green_remainder = total % 10000
yellow = green_remainder // 5000
yellow_remainder = green_remainder % 5000
blue = yellow_remainder // 1000
blue_remainder = yellow_remainder % 1000
coin500 = blue_remainder // 500
coin500_remainder = blue_remainder % 500
coin100 = coin500_remainder // 100
coin10 = (coin500_remainder % 100) // 10

print(" 만 원 ", str(green), " 장")
print(" 오천 원", yellow, " 장")
print(" 천 원", blue, " 장")
print(" 오백 원", coin500, " 개")
print(" 백 원", coin100, " 개")
print(" 십 원", coin10, " 개")



