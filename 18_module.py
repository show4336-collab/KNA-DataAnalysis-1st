# person_cost = {}

# party_result = [
#     {
#         "attendees": {"정렬", "남곤", "미소", "수민", "형희"},
#         "cost": 160000
#     },
#     {
#         "attendees": {"수민", "형희", "미소"},
#         "cost": 20400
#     }
# ]

# for party in party_result:
#     attendees = party["attendees"]
#     cost = party["cost"]
#     price = cost / len(attendees)

#     for person in attendees:
#         person_cost[person] = person_cost.get(person, 0) + price

# for person, cost in sorted(person_cost.items()):
#     print(f"{person}: {cost:,.0f}원")


# 수학 관련 모듈을 불러옵니다.
# import math

# print(math.sqrt(16))
# 수학 관련 모듈에서 sqrt 기능만 불러옵니다.
# from math import sqrt

# 이젠 sqrt만 불러도 됩니다.
# result = sqrt(16)
# print(result)

# ----------------------------------------------
# math라는 모듈 이름 다 쓰기 귀찮아서 줄여봅시다.
# import math as mt

# 별칭으로 가져온 모듈 이름을 언급해봅시다.
# result = mt.sqrt(16)
# print(result) # 4.0
# print(mt.sqrt(16)) # 4.0

# datetime 모듈을 가져옵니다.

# import datetime

# datetime의 now()는 현재의 지역 날짜와 시간을 반환합니다.

# now = datetime.datetime.now()
# print(now) # 2026-08-05 11:19:47.096690

# import datetime as dt

# now = dt.datetime.now() # 모듈이름을 dt로 바꿔야함
# print(now)  # # 2026-08-05 11:19:47.096690
# print(type(now)) # <class 'datetime.datetime'>

# 실습 1. import 세 방식으로 모듈 가져오기
# import, from import, import as

# import math

# print(math.sqrt(16))

# from math import sqrt

# print(sqrt(16))

# import math as mt

# print(mt.sqrt(16))

# 표준 라이브러리의 math

# math
# import math

# print(math.sqrt(9))  # 3.0
# print(math.ceil(4.2))  # 5
# print(2**3)  # 8

# 표준 라이브러리의 random
# import random

# print(random.randint(1, 10))  # 1~10 중 무작위 정수
# print(random.choice(["정상", "경고", "위험"]))  # 셋 중 무작위(실행마다 다름)

# 표준 라이브러리의 datetime
# import datetime

# now = datetime.datetime.now()
# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
# print(now)  # 2026-08-05 13:04:52.465138

# 실습 2. 표준 라이브러리로 센서값 만들기
# import random
# import math

# sensor_value = random.randint(1, 10)

# print(f"무작위 값 : {sensor_value}, 제곱근 : {math.sqrt(sensor_value)}")

# getcwd
# cwd(current working directory)
# os = operating system
# 운영체제와 대화하는 도구. 표준 라이브러리이므로 import os
# os.getcwd()
# get current working directroy
# 현재 작업 디렉토리를 절대경로 문자열로 돌려줌
# 데이터 작업의 첫 단계로 현재 위치를 출력해 보는 것이 좋은 습관

# 절대경로와 상대경로
# 절대경로의 예

# import os

# cwd = os.getcwd()
# print(
#     cwd
# )  # 현재 폴더의 절대경로 C:\Users\82107\OneDrive\바탕 화면\KNA-DataAnalysis-1st

# os.listdir로 폴더 들여다보기
# 폴더 안 파일, 폴더 이름을 리스트로 반환
# os.listdir(경로) # list[str]
# list directory의 약자
# 경로 생략 시 현재 작업 디렉토리 대상
# 결과가 리스트임.
# 반복문으로 이 목록을 돌면, 폴더 안 모든 파일을 한 번에 처리할 수 있음.

# listdir - 코드 확인
# 폴더 목록을 받아 반복문으로 출력

# import os

# files = os.listdir()
# for name in files:
#     print(name)
# git
# gitignore00

# 파일 존재 확인의 필요성
# 존재 확인
# 읽기 전에 있는지 확인하고, 있으면 읽고 없으면 건너뛴다.

# import os

# if os.path.exists('파일명'):
#  # 경로에 파일이 있으면 True
#  # 경로에 파일이 없으면 False
#     f = open(path)


# 파일이 존재하는지 알아봅시다.
# 운영체제마다 달라서 상황에 맞게 경로문자열을 만들어주는 os의 함수를 사용합시다.

# import os

# path = os.path.join("KNA-DataAnalysis-1st", "08_press.csv")
# print(path)

# if os.path.exists("08_press.csv"):
#     print("있습니다.")

# 실제로 경로문자열을 따라서 찾아가면
# 해당 파일이 있는지 알아봅시다. True 또는 Fasle 반환함.


#
#  실습 3. os로 폴더 목록 살펴보기

# import os

# cwd = os.getcwd()
# current_list = os.listdir(cwd)
# for csv_file in current_list:
#     if csv_file.endswith(".csv"):
#         print(f"{cwd}")
#         print(f"{current_list}")
#         print(f"{csv_file}")
