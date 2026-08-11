# numbers = [1, 2, 3, 4, 5]
# numbers_10 = []


# for number in numbers:
#     # print(number)
#     numbers_10.append(number * 10)

# print(numbers_10)

# 파이썬에서 기본 제공하는 기능들 외에
# 다양한 외부 라이브러리들을 가져오려면
# pypi.org 사이트에서 검색부터 합니다.

# 터미널에서 바로 pip로 설치를 시도하면(pip install numpy)
# 전체 시스템에 영향을 주는 설치로 생각되어 거절당한다.
# 그래서 개별 Working Directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리들을 따로 받아 쓰게 한다
# 이것이 바로 가상환경(venv)

# 1. 현재 경로에 가상환경 생성(터미널에서)
# python -m venv .venv


# 2. 가상환경 활성화
# source .venv/Scripts/activate
# (이후에는 가상환경 안에서 터미널 명령 실행 가능
# python -m pip install numpy

# 3. (작업/실행 끝나고) 가상환경 종료
# deactivate
# 다시 실행할땐 source .venv/Scripts/activate
# python 파일이름.py
# 작업끝 deactivate

import numpy as np

# numbers = [1, 2, 3, 4, 5]
# print(np.array(numbers))  # [1 2 3 4 5]
# print(type(np.array(numbers)))  # <class 'numpy.ndaaray'>

# temp = np.array([70.5, 69.8, 73.7])
# print(temp)  # [70.5 69.8 73.7]
# print(temp + 5)  # [75.5 74.8 78.7]
# print(temp[0])  # 70.5
# print(temp[:1])  # [70.5]
# print(temp[:2])  # [70.5 69.8]


# 실습 1. 센서값 배열 만들기
temp_list = np.array([10, 60.5, 83.2, 90])
print((temp_list * 1.8) + 32)


miles = np.array([100, 50, 95.4, 105.5])
# 속도(km/h) = 속도(mph)x1.60934
print(miles * 1.60934)


