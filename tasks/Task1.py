import math
population = 51761891
year = eval(input("년 수를 입력하세요: "))

"""
출생(+) : 17초 
사망(-) : 12초
입국이민자(+) : 87초 (1분 27초)
출국이민자(-) : 231초 (3분 51초) 
"""
timeSecond = year * 365 * 24 * 60 * 60
birth = timeSecond // 17
death = timeSecond // 12
immigration = timeSecond // 87
emigration = timeSecond // 231

currentPopulation = population + birth - death + immigration - emigration
print("7 년 후의 인구는  ", currentPopulation, "입니다.")
