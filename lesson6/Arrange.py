"""
[문제] 세 수 정렬
- 세 수를 입력받고 오름차순으로 정렬된 수를 출력하는 프로그램을 작성하시오
- 앞 두 수를 비교해서 앞 수가 크면 비교, 그리고 세 번째 수, 두 번째와 세 번째 수 비교
if문 3개 필요
"""

# 세 수를 입력받는다.

number1, number2, number3 = eval(input("세 수를 입력하세요: "))

if number1 > number2:
    number1, number2 = number2, number1

if number2 > number3:
    number2, number3 = number3, number2
# 나머지 2개인 number1 과 number2를 다시 비교,
# 현재 number2의 값은 원래의 number3값
if number1 > number2:
    number1, number2 = number2, number1

# ,로 분리됐을 때는 여러가지 타입을 써도 알아서 문자로 변환하여 출력
print("정렬된 수는", number1, number2, number3, "입니다.")

