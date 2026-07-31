# tuple : 값을 묶어주는 역할
# () 소괄호 안에 쉼표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 , 를 붙여야 Python이 튜폴로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

# sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = (
#     "모터온도",
#     78,
# )  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = 78  # 괄호 없고, 끝에 쉼표 없음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'int'>

# sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>

# sensor = ()  # 괄호 있고, 끝에 쉼표 없고, 값도 안담김
# print("sensor: ", sensor)
# print("type(sensor): ", type(sensor))  # <class 'tuple'>
# 빈 튜플도 있음. ()안에 값이 없으면 튜플임.

# 요소 갯수
# 요소 2개 이상 : 쉼표가 있으면 튜플
# 요소 1개 : 쉼표 여부
# 요소 0개(빈 튜플) : () 빈 괄호
# 튜플에서 많이 헷갈려하는 부분
# (1) # int
# (1,) # tuple

# (1, 2, 3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시

# num_tuple = (
#     1,
#     2,
#     3,
# )
# print(type(num_tuple))

# 튜플의 인덱스
# sensor = 10, 15, 20
# print(sensor[0])  # 10
# print(sensor[1])  # 15
# print(sensor[2])  # 20

# s = "a", "b", "c", "d", "e"
# 튜플의 슬라이싱
# print(s[1:4])  # ('b', 'c', 'd')
# 슬라이싱한 결과는 소괄호에 감싸져 있음
# 튜플은
# print(type(s[1:4]))  # <class 'tuple'>

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리
# 복습) 복수의 변수 한 번에 선언
# a, b, c = "a", "b", "c"
# print(a)  # 문자열 a
# print(b)  # 문자열 b
# print(c)  # 문자열 c

# unpacking = (
# 1,  # 변수 one
# 2,  # 변수 two
# 3,  # 변수 three
# )
# unpaking = one, two, three
# one, two, three 라는 알 수 없는 변수를
# unpaking 변수에 할당하겠다는 의미
# 동작 x

# one, two, three = unpacking
# unpaking이라는 변수에 담긴 튜플 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에
# 풀어서 담는다는 뜻
# print("one :", one)
# print("two :", two)
# print("three :", three)

# one, two, three, four = unpaking # Error 발생
# print("one :", one)
# print("two :", two)
# print("three :", three)
# print("four :", four)
# 튜플의 언패킹은 변수의 개수와
# 튜플에 담긴 값의 개수가 동일해야 함

# 리스트 언패킹이 가능할까?
# one, two, three, four = [11, 22, 33, 44]
# print("one :", one)  # 11
# print("two :", two)  # 22
# print("three :", three)  # 33
# print("four :", four)  # 44
# 가능!

# tup = (
#     "normal",
#     "normal",
#     "warning",
#     "normal",
#     "warning",
# )

# # 튜플의 길이
# print(len(tup))  # 5

# # 특정 값의 갯수 세기
# print(tup.count("warning"))  # 2
# print(tup.cound("Warning")) # 0

# # 특정 값이 처음 나온 인덱스 찾기
# print(tup.index("warning"))  # 2
# print(tup.index("Warning")) # ValueError

# sensors = [("모터온도", 78), ("펌프압력", 95)]
# print(type(sensors))
# for name, value in sensors:
#     if value > 90:
#         print(name, "경고")
# =========================================

# 튜플 리스트
# 리스트 안에 복수의 튜플을 담은 것
# for문으로 리스트를 사용해서 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

# hour_13 = [
#     ("모터온도", 77),
#     ("모터진동", 0.2),
#     ("모터압력", 91),
# ]

# now = 0
# for name, value in hour_13:
#     now += 1
#     print(f"{now}번째 반복")
#     print(f"name : {name} value : {value}")

# ========================================

# temps_13 = [
#     ("qox_001", 81),
#     ("qox_002", 88),
#     ("qox_003", 95),
#     ("qox_004", 89),
# ]

# warning = 90
# for name, temp in temps_13:
#     if temp >= warning:
#         print(f"경고 {name} 설비 온도 이상")

# 리스트 안의 튜플 갯수가 늘어나면
# for문에서 변수를 여러 개 작성하면 됨

# tup_list = [("일", "one", 1, "1"), ("이", "two", 2, "2")]

# for kor_str, eng_str, num, num_str in tup_list:
#     print(f"kor_str : {kor_str} eng_str : {eng_str}, num : {num}, num_str : {num_str}")

# for문에서도 언패킹 할 때는 무조건 튜플의 값 갯수와
# for문의 변수 갯수 통일
# 통일하지 않을 경우 Error 발생

# 튜플 리스트 정렬
# sorted()를 사용하여
# 튜플의 특정 값 기준으로 리스트를 정렬

# temps_13 = [
#     (81, "qox_001"),
#     (88, "qox_002"),
#     (95, "qox_003"),
#     (89, "qox_004"),
# ]

# #
# hot = sorted(temps_13, reverse=True)
# print(hot)
# print(f"원본 : {temps_13}")

# 실습 1. 센서를 튜플로 묶고 꺼내기

# sensor = ("모터온도", 78)
# print(sensor)
# print(sensor[0])
# print(sensor[1])
# name, temp = sensor
# print(name, temp)

# 실습 2. 튜플 리스트를 반복 처리하기

# sensors = [("펌프압력", 100), ("회전속도", 150), ("펌프온도", 50)]
# for name, value in sensors:
#     print(name, value)
# warning = 90
# for name, value in sensors:
#     if value > warning:
#         print(f"{name} 경고")

# 실습 3. 중첩 튜플로 센서 위치 관리하기
sensors = [("펌프압력", 100, (5, 3)), ("회전속도", 150, (6, 3))]
for name, value, position in sensors:
    x, y = position
    print(name, x, y)
for name, value, position in sensors:
    x, y = position
    if x <= 5:
        print(f"{name}")
