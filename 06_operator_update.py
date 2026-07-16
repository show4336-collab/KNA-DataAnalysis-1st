# 가로 = 50
# 세로 = 60
# 높이 = 70
# print((가로 + 세로 + 높이)/3) # 평균 60.0
# print(가로 * 세로) # 넓이 3000
# print(가로 * 세로 * 높이) # 부피 210000

print(=== 비교연산자 ===)
# <(미만), >(초과), <=(이하), >=(이상), ==(같다), !=(다르다)

print(7 < 16) # True
print(7 > 16) # False
print(7 <= 7) # True
print(7 >= 16) # False
print(7 == 7) # True
print(7 != 16) # True

print("hello" == "hello") # True
print("hello" != "hello") # False

# 1. 대소문자 구분
print("hello" == "Hello") # False
# 2. 공백이 있어도 다르다고 판단
print("정상" == " 정상") # False
# 3. 부정연산자 != (not)
# 두 값이 동일한데 !로 인해서 값이 반대로 출력됨
print("hello" != "hello") # False
print("hello" != " hello") # True
print("hello" != " hello") # True
