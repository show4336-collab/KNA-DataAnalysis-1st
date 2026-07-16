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
# hi = "안녕"
# hello = hi
# print(hello)
# print(hello == "hi")  # False / hi는 문자가 아니라 변수라서 False임
# print(hello == hi)  # True / Hello랑 hi는 같은 변수라서 True임


# 변수로 비교연산자 사용
# num1 = 123
# num2 = 456
# print(num1 >= num2)  # False
# print(num1 >= "num2") # TypeError 발생
# int랑 str은 서로 다른 자료형이므로 비교연산자 사용 불가

# ===========
# and / or / not - 논리연산자
# and : 둘 다 True여야 True를 반환
# print(5 == 5 and 7 == 7)  # True
# print(5 == 7 and 7 == 7)  # False + True = False
# # and는 첫 번째 조건이 False라면 뒤에 조건은 확인 안함
# print(5 == 5 and 7 != 7)  # True + False = False
# # 위 코드는 가능하다면 7 != 7 and 5 == 5 순서로 작성

# # or : 하나라도 True라면 True 반환
# print(5 == 5 or 7 == 7)  # True
# print(5 == 7 or 7 == 7)  # False + True = True
# print(5 == 5 or 7 != 7)
# or는 첫 번째 조건이 True라면 뒤에 조건 확인 안함

# not : 값을 반대로 뒤집음
# print(not True) # False
# print(not 5 == 5) # False
# 5 == 5를 연산하여 True를 변환
# not True로 작성해서 True를 뒤집어 False로 반환
# 반환받은 False라는 값을 print가 터미널로 출력

# print(5 == 5)  # True
# print(5 != 6)  # True
# print(3 > 5)  # false
# print(3 < 5)  # True
# print(6 >= 5)  # True
# print(6 <= 5)  # False

# 온도, 압력 = 85, 5
# 온도정상 = 60 <= 온도 and 90 >= 온도
# 압력정상 = 7 >= 압력 and 3 <= 압력
# print(압력정상 and 온도정상)

# 재고 = 100
# 입고 = 50
# 출고 = 30
# 반품 = 5
# print(재고 + 입고)
# print(재고 - 출고)
# print(재고 + 반품)

# 재고 = 100
# 재고 += 50  # 입고
# print(재고)
# 재고 -= 30 # 출고
# print(재고)
# 재고 += 5 # 반품
# print(재고)

# total = 500
# defect = 23
# print("불량율", defect / total * 100, "%")  # 불량율 %
# run = 21
# all = 24
# print("가동율", run / 24 * 100, "%")  # 가동율 %
# minute = 500
# print(minute // 60, "시간", minute % 60, "분")
