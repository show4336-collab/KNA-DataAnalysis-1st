# # 가로 = 50
# # 세로 = 60
# # 높이 = 70
# # print((가로 + 세로 + 높이)/3) # 평균 60.0
# # print(가로 * 세로) # 넓이 3000
# # print(가로 * 세로 * 높이) # 부피 210000

# print("=== 비교연산자 ===")
# # <(미만), >(초과), <=(이하), >=(이상), ==(같다), !=(다르다)

# print(7 < 16)  # True
# print(7 > 16)  # False
# print(7 <= 7)  # True
# print(7 >= 16)  # False
# print(7 == 7)  # True
# print(7 != 16)  # True

# print("hello" == "hello")  # True
# print("hello" != "hello")  # False

# # 1. 대소문자 구분
# print("hello" == "Hello")  # False
# # 2. 공백이 있어도 다르다고 판단
# print("정상" == " 정상")  # False
# # 3. 부정연산자 != (not)
# # 두 값이 동일한데 !로 인해서 값이 반대로 출력됨
# print("hello" != "hello")  # False
# print("hello" != " hello")  # True
# print("hello" != " hello")  # True

# # 변수에 문자열을 할당하고, 변수로 문자열 비교
# hello = "hi"
# print(hello == "hi")  # True
# # 위 비교에서 hello는 따옴표로 감싸지지 않았기 때문에 변수로 취급
# # 만약 hello를 "hello"와 같이 따옴표로 감싸면
# # str으로 인식해서 변수 취급을 하지 않음
# # ex) print("hello" == "hi") # False

# NameError(선언하지 않은 이름 호출했을 때)
hi = "안녕"
hello = hi
print(hello)
print(hello == "hi")  # False / hi는 문자가 아니라 변수라서 False임
print(hello == hi)  # True / Hello랑 hi는 같은 변수라서 True임


# 변수로 비교연산자 사용
# num1 = 123
# num2 = 456
# print(num1 >= num2)  # False
# print(num1 >= "num2") # TypeError 발생
# int랑 str은 서로 다른 자료형이므로 비교연산자 사용 불가
