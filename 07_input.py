# input - 사용자 입력
# print("출력")
# print(5)
# 어쨌든 터미널에서 보이는 출력된 값은 "글자"와 같이 보임
# input을 사용해서 값을 받는 곳도 터미널
# input을 통해 사용자에게 값을 입력받는 경우는 무조건 "str 타입"

# Python은 1번 줄부터 코드가 실행되다가 input을 만나면
# 사용자가 입력할 때까지 실행을 멈춤
# 사용자가 값을 입력하고 Enter를 입력하면 이후 코드가 실행됨

# input()
# input의 괄호 안에 아무것도 작성하지 않는 경우 그냥 입력창이 보임
# 그럼 사용자는 뭘 입력해야하는지 모르는 상황이 됨
# 이를 해결하기 위해 "가이드 문구"를 출력해줘야 함
# 방법 : input의 괄호 안에 "문자열"로 안내 문구 작성

# 여러 값을 입력받아야 하는 경우

# 시도 1. 매개변수를 여러개 전달
# input("이름 : ", "성별") # TypeError 발생
# input은 하나의 매개변수(아규먼츠, 인자)만 받을 수 있다고 에러 발생

# 시도 2. input() 두 번 작성
# input("이름 : ")
# input("성별 : ")
# input("나이 : ")
# 값을 여러 개 받아야 할 때는 input을 필요한 수 만큼 작성

# 시도 3. 가이드 문구에 규칙과 함께 입력받아야 하는 것들을
# input("이름, 나이를 입력해주세요. (ex. 이문용, 20) : ")

# ========
# input으로 받은 값은 변수에 저장하지 않으면 휘발됨
# 재사용을 위해 변수에 저장하는 것을 아주 강하게 권장
# 이후 재사용하지 않는다며 그 때 수정하기

# 사용자 입력값을 받아 변수에 저장
# name = input("이름(변수 할당 ver) : ")
# age = input("나이(변수 할당 ver) : ")

# # 입력받은 값을 활용(출력)
# print("입력받은 이름은", name, "입니다.")
# print("입력받은 나이는", age, "세 입니다.")

# # input으로 받은 값은 무조건 str으로 저장됨
# print(type(name))
# print(type(age))
# # 사용자가 숫자로 입력했어도
# # 컴퓨터는 입력받은 값이 글자로 쓰고 싶은건지 숫자로 쓰고 싶은건지 알 수 없음
# # ex. 사용자 입력값이 True일 때
# # 우연히 True를 입력했는지
# # bool 타입으로 True를 입력했는지 컴퓨터는 알 수 없음
# # 그래서 input으로 입력받은 값은 무조건 str으로 저장

# # ========

# # 사용자에게 입력받은 값을 한 번에 출력하기
# print("이름 :", name, "나이 :", age)  # 이름 : 이문용, 나이 : 34

# name = input("(입력받은 이름)")
# print("안녕하세요", name + "님!")

# int() - 문자열을 int(정수형)으로 변환
# int(변환하고자 하는 문자열)

# age = int("20")
# 문자열 20을 매개변수로 받은 int 함수를 통해
# int(정수형)으로 자료형이 바뀜
# # 그 다음에 age라는 변수에 값이 할당
# print("int로 변환한 age 변수의 자료형 :", type(age))

# age = int(input("나이(형변환 ver) :"))
# input을 통해 사용자 입력값으로 받은 문자열을
# 매개변수로 받은 int 함수를 통해
# int(정수형)으로 자료형이 바뀜
# # 그 다음에 age라는 변수에 값이 할당
# print("사용자 입력값을 int로 변환한 age 변수의 자료형 :", "int")
# print("당신은 곧", age + 1, "세가 됩니다.")

# print(int("123")) # 123
# print(int("010-1101-0010")) # ValueError
# -는 숫자가 아니기 때문에 int로 변환할 수 없음

# 번외) input의 입력값으로 그냥 Enter만 친 경우
# "" > 공백 문자열이 들어감

# 태어난 해 받아 나이 구하기
# birth_year = int(input("태어난 연도는? :"))
# age = 2026 - birth_year
# print("당신의 현재 나이는? :", age, "세 입니다.")

# =========
# flloat() - 실수로 작성된 문자열을 float으로 변환
print("=== 형변환 - float ===")

# print(float("12.5"))  # float()에 실수를 입력해도 동작됨
# print(float("12.5"))  # 12.5
# print(float(12))  # 12.0
# 사용자 입력값 float으로 변환
# tall = float(input("키 :"))
# # print("tall", tall, ", tall의 자료형 :", type(tall))

# # ==============
# print("=== 문자열로 변환 ===")

# year = int(input("태어난 연도 : "))
# print("당신의 현재 나이는", str(int))
# # int와 str은 +(더하기 연산자)를 사용할 수 없음

# # ===============
# # 질문) 진동값을 입력받았을 때 출력하는 경우
# a = input("진동값: ")
# print("현재 입력받은 진동값은 " + a)
# 값의 형태가 int나 float이어도 input으로 입력받은 경우 자료형은 무조건 str
# 출력에서 +연산자 사용은 형변환 없이 가능
# 하지만 실제로는 int나 float으로 입력받은 값을 str으로 변환해서 출력하는 경우가 많음

# =============

# int, float, bool은 str으로 변환 가능
# b = str(123)  # "123"
# c = str(123.4)  # "123.4"
# d = str(True)  # "True"
# e = int("str")  # ValueError / float도 동일
# e = int(False)  # ValueError / float도 동일
# f = int(false)  # ValueError / f가 소문자면 "변수"라고 인지를 하기 때문에 false라는 변수가 없어서 불가

# nation = input("거주 국가는? :")
# city = input("도시는? :")
# print(nation + "의 " + city + "에서 거주하시는군요!")

# a = int(input("a?"))
# b = int(input("b?"))
# print("합 =", a + b)
# print("곱하기 =", a * b)

# temp = int(input("온도는?"))
# print("80 초과", 80 < temp)
# print("0도 이상", 0 <= temp)

# a = int(input("a = ?"))
# b = int(input("b = ?"))
# c = int(input("c = ?"))
# avg = (a + b + c) / 3
# print("60 이상?", avg >= 60)

