# # 변수 선언 방법
# # 변수이름 = 값
# # 오른쪽 값을 왼쪽 이름에 "저장" 하라는 코드
# temp = 36  # 숫자로 저장하고 싶다면 따옴표 금지
# name = "센서 A"  # 글자는 무조건 따옴표로 감싸기

# # print(temp) # 36
# # print("temp") # temp
# # print(name) # 센서 A
# # = 은 "같다"가 아니라 "저장"하는 것
# # 비교는 == 을 사용

# # ==============
# # print("==== 변수 사용 활용 ====")

# x = 5
# x = x + 5
# # 변수를 "재할당"할 때 변수 기존 자신의 값을 활용할 수 있음
# # 오른쪽 계산을 먼저 한 뒤 재할당 하는 것임
# # y = y + 5 # 오류 발생, y가 선언되지 않았기 때문
# # print(x)
# # print("재할당하기 전 temp:", temp)
# temp = 15  # 위에서 할당했던 36이라는 값을 15로 재할당(수정)
# Temp = 150  # temp와 다른 변수로 동작
# # print("temp:", temp)
# # print("Temp:", Temp)
# # 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불려옴
# # print(score) # NameError 발생
# score = 10
# # print(score)  # 10
# score = 20
# score = 30
# # print(score)  # 30

# ============================
# print("== 값 복사 ==")
# a = 10
# b = a  # b 변수에는 10이 저장 (저장할 때의 그 순간의 a 값을 b에 복사)
# a = 100  # a 변수를 재할당해도
# print(b)  # 10 b 변수의 값은 10이 그대로 유지됨

# print("= 여러 변수 한 번에 선언 및 할당 =")

# width, height = 10, 20  # width는 10, height는 20이 할당
# print("width=", width, "height:", height)

# 형식: 변수1, 변수2, ... = 값1, 값2, ... > 변수와 값이 갯수가 같아야 함'

# x, y, z = 10, 20 # 변수 3개, 값 2개 > ValueError 발생

# print("== 주석으로 변수 설명 ==")


# count = 3  # 센서 개수
# temp = 10000000 # 주석처리된 코드는 동작하지 않음

# temp = 25  # 온도(섭씨)
# print(temp)  # 25
# name = "센서A"
# print(name)

# temp = 30
# print(temp)  # 30
# temperature = temp  # 변수 이름 temp를 temperature로 변경
# print(temperature)

# my_number = 2
# print(my_number)
# mood = "so good"
# print(mood)

# age = 34
# label = "나이"
# print(label)
# print(age)

# x = 10
# print(x) # 10
# x = x + 5
# print(x) # 15
# x = x * 2
# print(x) # 30

# a = 100
# b = a
# a = 999
# print(a) # 999
# print(b) # 100

# print(temp) # NameError
# score = 90
# print(Score) # 대소문자 다름


# temp = 25
# print(temp) # 25
# score = 90
# print(score) # 90

# temp = 25  # 온도(섭씨)
# count = 3  # 센서 개수
# # temp = 100 # 실행안함
# print(temp) # 25

# x = 5
# x = 10
# x = x + 1
# print(x) # 11

# name = "Lee Mun Yong"
# age = 34
# print("자기소개")
# print(name)
# print(age)

# a = 25
# b = 3
# device_temp = a
# sensor_count = b
# print(device_temp) # 25
# print(sensor_count) # 3

# x, y, z = 1, 2, 3
# width, height = 4, 3
# print(width)
# print(height)

