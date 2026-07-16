# int - 정수형(소수점 없이 딱 떨어지는 수)

count = 3
age = 20

# # 0과 음수도 정수에 포함됨
zero = 0
temp = -30

# =============

# float - 실수형(소수점이 붙은 수)
weight = 70.5
height = 1.79

# =============

# str - 문자열형(따옴표에 감싸져있는 모든 값)
name = "홍길동"
address = "서울시 강남구 역삼동"
emoji = "😀💕"
empty = ""  # 따옴표만 있고, 아무것도 작성되지 않아도 str
illit = "It's me"  # 따옴표 안에 따옴표를 작성하고 싶을 때, 다른 따옴표로 감싸주면 됨

# bool - 불린형(True, False만 있음)
# 첫 글자는 대문자, 따옴표 없이 작성 True, False
ok = True
no = False
# 비교할 경우 bool로 출력
# print(100 < 5)  # False
# print(5 == 5)  # True

# =============

# type() - 데이터 타입 확인 함수
# type(확인하고자 하는 것) > 입력한 것의 자료형을 알려줌
# type(5)  # 터미널에서 확인 불가 > print를 하지 않아서
# print(type(5))  # <class 'int'>라고 출력됨
# print(type("센서"))  # <class 'str'>라고 출력됨
# print(type(True))  # <class 'bool'>라고 출력됨
# print(type(3 > 2))  # <class 'bool'>라고 출력됨
# 1. print 함수의 내부를 확인
# 2. print 함수에 또 함수가 있는 것을 확인하고 type 함수의 내부를 확인
# 3. type 함수의 내부에 연산자가 있는 것을 확인하고 연산 진행
# 4. 3 > 2의 결과값이 True이므로 type(True)로 바뀜
# 5. type(True)의 결과인 <class 'bool'>라고 print로 인해 터미널에 출력됨

# print(3, type(3))  # 3 <class 'int'>

num = 123
fake_num = 123
str = "문자열"
ok = True

# print(num, ">>>", type(num))  # 123 >>> <class 'int'>
# print(num, ":", type(num))  # 123 : <class 'int'>
# print("num >>>", type(num))  # num >>> <class 'int'>
# print("num :", type(num))  # num : <class 'int'>

# print("=== 자료형마다 동작이 다른 것 확인하기 ===")
# print("3 + 5")  # 8 (int) > 숫자끼리 더하기는 계산
# print("3" + "5")  # 35 (str) > 문자열끼리 더하기는 이어붙이기
# print("안녕하" + "세요")  # 안녕하세요

# =============
# print("=== 자주 하는 실수 ===")
# print(
#     0.1 + 0.8
# )  # 0.9로 출력되지만 가끔 컴퓨터 내부 연산 과정에서 아주 작은 오차가 발생하는 경우도 있음
# 작은 오차 해결법
# print(round(0.1 + 0.8, 2))  # 소수 둘째 자리를 반올림해서 0.9로 출력

# str과 int/float는 서로 다른 자료형이므로 연산이 불가
# print('123' + 123) # TypeError 발생

# print(10 / 2)  # 5.0 > 나눗셈은 결과가 딱 떨어져도 항상 float로 출력됨
# print(type(10 / 2))  # <class 'float'> > 나눗셈의 결과는 항상 float
