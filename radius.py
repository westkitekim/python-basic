# 반지름 입력
radius = eval(input("반지름 값을 입력하세요: "))

print("넓이는", radius * radius * 3.141592, "입니다.")

print("둘레는", 2 * radius * 3.141592, "입니다.")


import time
currentTime = time.time()

totalSeconds = int(currentTime)
#현재까지의 초 
currentSecond = totalSeconds % 60
#현재까지의 분(//로 정수 나눗셈) 
totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60
#전체 지난 시간 
totalHours = totalMinutes // 60

currentHour = totalHours % 24

print("현재시간은 : ", currentHour, ":", currentMinute, ":", currentSecond, "입니다.")
