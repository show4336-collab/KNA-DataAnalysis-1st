# print 함수를 생각해봅시다
# print("안녕하세요")

# first_name = "Ned"
# last_name = "Park"
# print(first_name)
# print(last_name)
# print(first_name, last_name)
# print(f"{first_name} {last_name}")

# 위와 같이 똑같은 print를 호출해도
# 다양한 방법의 호출이 가능
# 그 원리를 알려면
# 우리가 직접 함수들을 만들 수 있어야 합니다.

# 에러(Error)의 종류
# 1. 실행 중에 오류 (Runtime Error) - 작동 중단됨
# 2. 논리적 오류 - 동작은 잘 되는데, 결과적으로 문제가 있어 고쳐야함

# def greet():
#     print(f"점검을 시작합니다.")

# greet()

# def print_line():
#     print("=" * 20)

# print_line()
# print_line()

# 함수는 호출되기 전에 만들어져야 합니다.

# show_title() # NameError 발생


# def show_title():
#    print("함수 배우기")


# show_title()

# 실습 2. 반복 코드를 함수로 정리하기

# def sensors_check():
#     print(f'{"=" * 30}')
# print(f"센서 점검을 시작합니다.")
# print(f'{"=" * 30}')

# 함수가 호출되면 그 안의 코드는 매번 새롭게 시작된다.
# def show_counter():
# count = count + 1 # 기존 count라는 존재는 모른다고 Error
# count = 0
#    print(count)
# 이 함수가 종료되면 count를 포함한 이 함수 안의 데이터는 모두 사라짐


# def show_students():
#     print("학생1 : 짱구")
#     print("학생2 : 철수")
#     print("학생3 : 훈이")


# def show_teacher():
#     print("선생님 : 채송화")


# def show_classroom():
#     show_teacher()
#     show_students()


# show_classroom()

# print("------------------")

# [상식] 사이드이펙트
# 특정 부분의 코드가 문제 없지만
# 다른 부분과 예상치 못한 영향을 주고 받는다면?

# 코드 중복과 함수화

# print("압축기A 온도 확인 중")
# print("결과를 기록합니다.")
# print("펌프1 온도 확인 중")
# print("결과를 기록합니다.")

# 위와 같은 식의 코드를 여기저기 복사-붙여넣기 하면
# 언젠가 사람의 실수로 사고가 발생할 수 있다.

# def start_check():
#     print("점검을 시작합니다.")
#     print("안전 장비를 확인하세요.")
#     print("기록을 준비하세요.")

# start_check()

# 실습 1.

# def check(name):
#     print(f"{name} 점검 시작")


# check("압축기A")  # 압축기A 점검 시작
# check("펌프1")  # 펌프1 점검 시작


# def report(name, temp):
#     print(f"{name}의 온도 : {temp}도")


# report("압축기A", 75.3)

# 실습 2. 다중 매개변수로 센서값 계산하기


# def counting(name, temp):
#     print(f"{name} {temp}도")


# counting("모터", 78)
# counting("펌프", 92)


# # 실습 3. 키워드 인자로 함수 호출하기
# def sensor(name, value):
#     print(f"{name} {value}")


# sensor(value=78, name="모터")
# sensor("펌프", value=92)
# sensor(name="펌프", 78) # Error
# # 키워드 인자 나오면 그 뒤도 키워드 인자여야 함.
# 위치인자 뒤에는 키워드 인자 가능함
# 위치, 위치 또는 키워드, 키워드를 쓰는게 좋음.
# 실무에선 키워드, 키워드를 많이 씀(실수를 줄이기 위해)

# 실습 4. 반환값으로 간단 계산기 만들기

# def value(value1, value2):
#     return (value1 + value2) / 2


# avg1 = value(80, 90)
# avg2 = value(85, 95)

# print(avg1)
# print(avg2)

# ==================================


# 반환값
# def add(a, b):
#     total = a + b
#     return total

# 위랑 같은거임.
# def add(a, b):
# return a + b


# result = add(1, 2)
# print(result + 1)  # 4
# print(result + 2) # 5
# print(result + 3) # 6

# 여러번 같은 결과 호출해야한다면
# 차라리 변수에 담아서 쓰세요


# print(f"1 + 2 = {result}") # 같은 거임
# print(f"1 + 2 = {add(1, 2)}") # 같은 거임


# 여러 값을 한 번에 반환하기
# def min_max(values):
#     return min(values), max(values)


# result = min_max([75.3, 88.0, 49.1])
# print(result) # (49.1, 88.0)
# print(type(result)) # tuple

# 반환값 언패킹으로 받기
# 함수의 결과를 받는 순간에
# 결과 튜플의 내용을 풀어서
# 개별 변수에 담아 사용하기

# def min_max(values):
#     return min(values), max(values)


# low, high = min_max([10, 20, 30])

# print(f"최솟값 : {low}, 최댓값 : {high}")


# 반환값이 없는 함수와 None
# def greet(name):
#     print(name + "님 환영합니다.")


# greet("하이")  # 하이님 환영합니다.
# print(greet("하이"))  # 하이님 환영합니다.
# print(type(greet("이문용")))  # NoneType
# result = greet("하이") # return이 없는 함수로 None을 돌려준다.
# print(result) # None

# 선택문제


# def sensor(value):
#     return min(value), max(value), sum(value) / len(value)


# sensor_list = [78, 92, 86, 90]
# minimum, maximum, avg = sensor(sensor_list)
# print(minimum, maximum, avg)


# def grade(temp, limit=80):
#     if temp > limit:
#         return "점검필요"
#     return "정상"


# print(grade(95, limit=90))

# 게임
# 가봤거나, 가보고 싶은 여행지 정보를 모아봅시다.(5개)
# 함수를 호출하면 랜덤으로 해당 여행지의 국가이름과 수도
# "환영합니다! 000 나라의 수도는 000 입니다!" 출력

# import random


# def get_random_country():
#     country = [
#         {"국가": "일본", "수도": "도쿄"},
#         {"국가": "미국", "수도": "워싱턴"},
#         {"국가": "중국", "수도": "베이징"},
#         {"국가": "스위스", "수도": "베른"},
#         {"국가": "이탈리아", "수도": "로마"},
#     ]

#     my_country = random.choice(country)

#     return my_country.get("국가"), my_country.get("수도")


# country_name, country_sudo = get_random_country()
# print(f"환영합니다! {country_name} 나라의 수도는 {country_sudo}입니다.")


# 기본값 인자
# name과 value는 호출할 때 꼭 매개변수를 지정해줘야하지만
# unit은 지정/언급 안해주면 "도(℃)" 기본값으로


# def report(name, value, unit="도(℃)"):
#     print(f"{name} : {value}{unit}")

# report()

# 실습 1. 기본값 인자 함수 만들기

# def report(temp, limit=80):
#     if temp > limit:
#         return print(f"{temp} → 경고")
#     return print(f"{temp} → 정상")


# report(78)
# report(95)
# report(50, limit=40)

# 기본값 덮어쓰기
# 결과가 boolen 타입을 return하는 함수는
# 이름이 보통 "is"로 시작한다.

# def is_over_limit(value, limit):
#     if value > limit:
#         # 위험 맞음
#         return True

#     # 그 밖에는 위험 아님
#     return False

# 실습 2. 지역변수 관찰하기

# def report(temp1, temp2):
#     temp_sum = temp1 + temp2
#     return print(temp_sum)

# report(10, 20)
# print(temp1, temp2) # 오류

# 실습 3. 처리 흐름 만들기


# def judge(temp1, temp2):
#     return temp1 + temp2


# temp_sum = judge(80, 90)


# def judge2(status="정상", avg=temp_sum / 2, avg_limit=90):
#     if avg < avg_limit:
#         return print(f"평균 {avg} → {status}")
#     else:
#         status = "경고"
#         return print(f"평균 {avg} → {status}")


# judge2()


# 실습 4. 센서 분석 함수 세트 만들기
# function_review
# 함수의 기본 예제
# def say_hello():
# pass  # 아무일도 안하는 코드


# def say_hi():
# print("안녕하세요")


# 함수는 선언된(def) 후에 호출되야 한다.
# say_hi()


# 매개변수를 사용하면 더 다양한 일을 할 수 있습니다.
# def show_hello(name):
# print(f"안녕하세요, {name}")


# show_hello("Ned")

# 매개변수는 여러 값을 받을 수 있고
# def show_hi(name, message):
# message = "반갑습니다"
# print(f'{message}, {name}')

# show_hi("Ned", "안녕하세요")


# 매개변수에는 따로 안알려주면 기본값을 적용할 수도 있습니다.
# def show_greeting(name, message="안녕하세요"):
#     print(f"{message}, {name}")


# show_greeting("Layla")
# show_greeting("Jack", message="Hello")
