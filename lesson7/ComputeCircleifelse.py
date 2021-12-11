# 반지름값 입력
radius = eval(input("반지름을 입력하세요:"))

if(radius > 0): #반지름이 0보다 클 때만 계산
    #넓이 출력
    print("넓이는", radius * radius * 3.141592, "입니다.")
    #둘레 출력
    print("둘레는", 2 * radius * 3.141592, "입니다.")
else:
    print("잘못된 입력입니다.")