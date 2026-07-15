# print(NameError만들기) # NameError 발생
# print(NameError 만들기) # SyntaxError 발생(띄어쓰기가 있어서 변수 2개를 쉼표 없이 작성)
# # 코드는 위에서 아래로 실행되기 때문에 위에서 에러 발생하면 그 이후 코드 실행 x
# print("NameError 만들기")  # 따옴표로 감싸주면 에러 발생 x

# #====================
# print("====SyntaxError 만들기===")

# print("온도") # 따옴표를 안넣음
# print("진동" # 괄호를 안닫음

# print(온도, 75)  # NameError
# print("진동", 2.3  # SyntaxError '(' 가 닫히지 않음
# print("압력": 4.0)  # SynataxError: invalid syntax, 콤마를 안넣음

# print("=====" + " 1번" + " 설비" + " 점검" + " =====")
# print("온도(℃):", "82")
# print("온도 상승량:" + " 11")

x, y, z = 10, 20, 30
print(x) # 10
print(y) # 20
# 갯 수가 같아야 함
