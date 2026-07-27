# """ """ ) 여러 줄 문자열

# 작성하는 개발자가 보기 편한 방식으로 출력했을 때 문제
# notice = """설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검"""

# print(notice)
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
# 위와 같이 직접 작성한 줄바꿈이 반영되어 여러 줄로 출력함

# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴
# """ """ (삼중 따옴표를 사용할 시 그 내부의 모든 줄바꿈이 반영되어 출력)

# 탭
# notice = """설비 점검 안내
#     1. 전원 확인
# 2. 센서 점검"""

# print(notice)
# 삼중 따옴표는 탭도 그대로 유지

# ===========
# 이스케이프 문자

# notice 이스케이프 사용해서 개선
# notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
# print(notice)

# tap = "이름\t상태"
# print(tap)
# print("이름 상태")

# backslash = "이름\\상태"
# print(backslash)  # 이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

# quotes = 'It\'s me'  # 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \를 사용
# print(quotes)

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 않았다면 "빈 문자열"
# 빈 문자열은 글자 수 0, 길이 0
# " " 따옴표 안에 공백(스페이스 바)이 있는 경우는 공백 문자열
# 공백(스페이스 바)의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨
# print("" == "  ") # False

# 백슬래쉬 2개 표현하고 싶으면 \\\\ 4개 해야함. >  \ 다음 문자만 해석함

# ============
# print("=== 설비 정보 출력 카드 만들기 ===")
# code = "PUMP_A"
# state = "정상"
# hour = 1200
# date = "2026-07-16"

# card = (
#     "설비 : "
#     + code
#     + "\n"
#     + "상태 : "
#     + state
#     + "\n"
#     + "가동 : "
#     + str(hour)
#     + "\n"
#     + "점검 : "
#     + date
# )
# print(card)

# 예상 출력 결과
# 설비 : PUMP_A
# 상태 : 정상
# 가동 : 1200
# 점검 : 2026-07-16

# + 말고 , 로 하면 이쁘게 안나옴 + 로 하기

# ============
# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열[인덱스번호]
# 문자열의 첫 글자 인덱스는 0
# print("=== 인덱싱 ===")
# word = "PYTHON"
# print(word[0], word[3], word[5]) # P H N

# print(word[100]) # IndexError
# word 변수에 저장된 문자열의 길이보다 큰 인덱스를 호출했기 때문

# abc = "abcdefghijklnmopqrstuvwxyz"
# 자기 이름 출력하기 (성 빼고)
# print(abc[13] + abc[-2])

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항은 음수 인덱스는 가장 마지막 글자가 -1부터 시작

# ====================
# print("=== 슬라이싱 ===")

# 슬라이싱 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함해서 출력
# 끝 인덱스 글자는 제외하고 출력

# word = "PYTHON"
# print("word[3:5]) 결과 :", word[3:5])  # HO
# print("word[3:6] 결과 :", word[3:6])  # HON
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용할 수 있음

# print(word[6]) # 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고 넘치면 Error

# 슬라이싱 - start 생략
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
# print(word[:4]) # print(word[0:4]와 동일한 동작

# 슬라이싱 - end 생략
# 특정 인덱스부터 끝까지 구간을 뽑아내고 싶을 때 사용
# print(word[2:]) # 2번 인덱스부터 끝까지 출력
# print(word[2:6])과 동일한 동작

# 슬라이싱 - 전체 생략
# print(word[:]) # print(word[0:6])와 동일한 동작
# :을 사용하고 start와 end를 모두 생략하면 모든 인덱스의 구간을 뽑아냄

# 슬라이싱 - 음수 인덱스 사용
# print(word[-3:])  # HON
# 음수 인덱스 작성 시 그냥 그 인덱스부터 정방향으로 출력함
# print(word[:-1]) # PYTHO
# 처음부터 -1(5)를 제외한 구간을 뽑아냄
# 역순 아님 주의
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작

# step으로 건너뛰기
# 문자열[시작:끝:간격(step)]
# print(word[0:6:2]) # PTO
# PYTHON에서 첫 번째 글자는 명시했으니 거기서부터 출력
# step이 2이기 때문에 Y 뛰고, T(두번째 점프) 출력
# H 뛰고, O(두번째 점프) 출력
# N 뛰고 끝
# 두 글자를 뛰는게 아니라 두 번 뛰는 것

# print(word[0:6:1]) # PYTHON

# start와 end를 생략하고 step만 입력
# print(word[::2])  # PTO

# 순서 뒤집기
# print(word[::-1]) # NOHTYP
# step은 인덱스가 아니고, 음수 입력 시 문자열의 순서를 뒤집음

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
# print("범위를 벗어난 슬라이싱", word[0:100]) # PYTHON을 정상 출력

# word = "temp_sensor"
# print(word[:4])
# word = "temp_sensor"
# print(word[5:])
# word = "sensor_01"
# print(word[-2:])

# word = "PYTHON"
# print(word[::2])

# word = "PYTHON"
# print(word[::-1])

# ======================
# len() - 문자열의 길이 반환
# len(문자열)

# print("=== len() 활용 ===")
# print(len("Hello World!"))  # 12 (공백도 모두 글자 취급)
# print(len("")) # 0 (빈 문자열은 0 출력)

# var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요!"
# print(len(var))  # 변수에 담긴 문자열의 길이 출력도 가능

# print(len("이것도") - len("가능할까?"))
# # len()은 int를 반환하기 때문에 연산 가능

# print("abc 변수의 길이 :", len("abc"), " / 마지막 인덱스 번호 :", len("abc") - 1)

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때

# Phone_Number = "01000000000"
# print(len(Phone_Number))

# in-포함 여부 확인
# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# 찾을 문자열 in 문자열
# print("고장" in "설비 고장 발생")  # Ture
# print("정상" in "설비 고장 발생")  # False
# print("설비에서 고장" in "설비 고장 발생")  # False
# print("설비에서 고장" in "설비에서 고장이 났습니다.")  # True
# 찾을 문자열 in 문자열

# not in - in의 정반대 동작
# print("고장" not in "설비 고장 발생")  # False
# print("정상" not in "설비 고장 발생")  # True
# print("설비에서 고장" not in "설비 고장 발생")  # True
# print("설비에서 고장" not in "설비에서 고장이 났습니다.")  # False

# print(" " in "설비 고장 발생") # True
# 따옴표로 감싼 공백(스페이스바)는 정말 "한 글자"로 취급

# =============
# print("=== count() ===")
# .count() - 문자열에 특정 글자 수(int)를 반환
# 문자열에 .count("찾을 글자")
# print("banana".count("a"))  # 3
# print("010-1234-1234".count("-"))  # 2
# print("layla@spreatics.com".count("@")) # 1

# print("a,b,c,d".count(","))

# abcd = "a,b,c,d"
# print(abcd.count(","))  # 3
# print(abcd.count(", "))  # 0

# ================
# print("=== find() ===")
# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환

# email = "hong@company.com"
# at = email.find("@")  # @ 위치의 인덱스인 4가 할당
# user_id = email[:at]  # hong 이라는 사용자의 아이디만 추출
# print(user_id)  # hong

# 다다음주 # SQE-00Q8이라는 설비의 SQE만 뽑아내기(find와 슬라이싱 사용)
# sqe = "SQE-00Q8"
# sqe_index = sqe.find("-")
# print(sqe_index)  # 3
# sqe_fin = sqe[:sqe_index]  # sqe[0:3] 반환
# print(sqe_fin) # SQE

# 다다음주 # SQE-00Q8이라는 설비의 SQE만 뽑아내기(index와 슬라이싱 사용)
# sqe = "SQE-00Q8"
# sqe_index = sqe.index("-") # - 있으니 정상 동작 / 만약에 없으면 Error 나고 동작 중단
# print(sqe_index)  # 3
# sqe_fin = sqe[:sqe_index]  # sqe[0:3] 반환
# print(sqe_fin)  # SQE


# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서부터 가장 처음 나오는 인덱스 번호만 반환
# 인덱스는 찾는 문자열이 없으면 Error 발생

# email = "show000@naver.com"
# at = email.index("@")  # 5
# print(email[0:at])  # show000
# print(email[:at])  # 시작 번호가 0이라면 start 생략 가능
# print(email[at:])  # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략
# # 위처럼 시작하면 5번 인덱스부터 출력하기 대문에 @을 포함
# print(email[at + 1 :])  # at + 1을 하면 @을 포함하지 않고 출력

# ===========================
# print("=== count() ===")

# a의 갯수 세기
# str = "a, b, c, d, e, a, a"
# print(str.count("a")) # 3

# ,의 갯수 세기
# print(str.count("a")) # 6
# 만약 str = "a, b, c, d, e,a, a"
# print(str.count(", ") # 5 # count로

# =====================================
# print("=== startswith ===")

# 특정 문자열로 시작하는지 검사
# True / False (불리언)

# EQP로 시작하는지 검사하기
# print("EQP-001".startswith("EQP"))

# 변수 활용
# eqp = "EQP"
# print("EQP-001".startswith(eqp))
# 주의사항) 변수명은 따옴표 감싸기 금지!!!

# =====================================
# print("=== endswith ===")
# 특정 문자열로 끝나는지 확인
# True / False로 반환

# str2 = "월요일입니다! 여러분은 할 수 있어요!"

# print(str2.endswith("!"))  # True
# print(str2.endswith("요!"))  # True
# print(str2.endswith("음"))  # False
# print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!"))  # True
# print(str2.endswith("월요일입니다!       여러분은 할 수 있어요!"))  # False
# print(str2.endswith("월요일입니다! 여러분은 할 수 있어요! "))  # False
# print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!"))  # False

# sensor = "sensor_log.csv"
# print(sensor.startswith("sensor"))  # True
# print(sensor.endswith(".csv"))  # True

# 연산, 검색 메서드 정리
# 도구를 결과 형태로 묶어 기억
# 숫자를 주는 것 - len, count, find
# 참 거짓을 주는 것 - in, startswith, endswith, ==
# count는 없으면 0, find는 없으면 -1

# =============================================
# print("=== 값은 객체다 ===")

# print(type("잊어먹으면 안돼!"))  # <class 'str'>
# print(len("이렇게 썼죠??"))
# endswith와 len의 차이는?
# endswith는 .으로 연결
# .으로 연결하는 이런 도구들은 "메서드"
# 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# len은 . 사용 안함
# () -> 함수
# len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수는 "내장함수"
# "str".startswith("s")
# 123.startswith(1)
# .으로 사용하는 메서드들은 특정 자료형(객체 타입) 마다 다름
# int 자료형의 객체에는 startswith라는 메서드가 없음

# print(len(123)) # len 내장함수는 길이를 반환하기 때문에 int 자료형 사용 불가

# =========
# 재할당 복습

# num = 1
# num = num + 1  # 2
# num += 1 # 3
# += 은 복합할당 연산자 원래 내 자신의 값을 적용해서 재할당

# =========
# print("=== .upper() ===")

# str = "abcdefg"
# print(str) # abcdefg

# str.upper # ABCDEFG > 반환은 대문자인데, 값에 재할당을 안했음.
# print(str) # abcdefg > 기존 str의 값인 소문자를 그대로 출력

# 앞으로 계속 대문자로 변환한 값을 사용하고 싶다면
# 변수에 재할당
# 변수 재할당에서 변수 스스로를 부르는 것이 가능
# 재할당에서 변수 스스로 값을 부르려면 무조건 "재할당"이어야 함

# str = str.upper()
# print(str) # ABCDEFG

# abc = "READY"
# cba = abc.lower()
# print(cba)

# ==================
# user_name = "kim chul soo"

# capitalize는 문자열의 첫 글자만 대문자로 변환
# print(user_name.capitalize())  # Kim chul soo
# title은 띄어쓰기 기준으로 각 단어의 첫 글자들을 모두 대문자로 변환
# print(user_name.title())  # Kim Chul Soo

# '를 사용한 경우
# print("i'm full".capitalize())  # I'm full
# print("i'm full".title())  # I'M Full
# print("i'm full".title())  # I'M Full

# print("NORMAL".lower() == "normal".lower())

# 전부 대문자인지 소문자인지 검사하기 is upper, is lower
# print("ABC".isupper())  # True
# print("abc".islower())  # True
# print("Abc".isupper())  # False
# print("Abc".islower())  # False

# abc = "Sensor_LOG.CSV"
# a = abc.upper()
# print(a.startswith("sensor"))
# print(a.endswith(".csv"))

# b = abc.lower()
# print(b.startswith("sensor"))
# print(b.endswith(".csv"))

# ====================================
# print("=== strip() ===")

# 공백 제거
# strip() : 앞과 뒤의 모든 공백 제거(중간 띄어쓰기는 그대로 유지)
# lstrip() : left(왼쪽) 공백만 제거
# rstrip() : right(오른쪽) 공백만 제거

# raw = "           정상   "
# print(raw.strip())  # "정상"
# print(raw.lstrip())  # "정상   "
# print(raw.rstrip())  # "           정상"
# print(raw)  # "           정상   "
# print("   정   상    ".strip())  # "정   상"

# strip("문자")
# a = "###정상###"
# print(a.strip("#"))  # 정상
# 갯수 상관없이 인자로 전달한 문자를 무조건 삭제

# print(a.strip("# "))
# 공백 상관없이 양 끝의 해당 문자열 삭제

# a = "==정==상==="
# print(a.strip("=")) # 정==상
# 글자 중간에 있는 문자열은 건들지 않음


# ====================================
# print("=== 체이닝 ===")
# 메서드 연결해서 쓰기(체이닝)
# a = "   NORMAL  "
# 체이닝 X
# step1 = a.strip()  # "NORMAL"
# step2 = step1.lower()  # "normal"
# print(step2)

# 체이닝 X, 기존 변수에 재할당
# a = a.strip().lower()  # "normal"
# print(a)

# 체이닝 O
# clean = a.strip().lower()  # "normal"
# print(clean)


# ====================================
# print("=== 체이닝 ===")

# a = "  Warning    "
# print("[" + a.lower(), "]")
# a = a.strip().lower()
# print("[" + a + "]")

# strip() 메서드에 인자로 들어가는 문자열은 안전히 동일하지 않아도 전부 삭제됨!
# a = "aaabb 이렇게? cdcd"
# print(a.strip("abcd"))  # 이렇게?
# print(a.strip("bc"))  # aaabb 이렇게? cdcd
# print(a.strip("ab")) # 이렇게? cdcd
# print(a.strip("cd")) # aaabb 이렇게?
# 지금 출력 결과는 "  이렇게?  " 이렇게 나오고 있어
# 내가 생각했을 때 ==처럼 정확하게 "abcd" 순서가 아니면
# strip이 안될줄 알았는데 실행 결과를 확인해보니 순서랑 상관없이
# 인자로 전달한 문자열에 해당하는 글자가 확인하는 문자열 양 끝에
# 하나라도 있으면 동작하는 것 같아
# 내가 이해한게 맞아?
# 그렇다면 왜 이렇게 동작하는거야?

# 대소문자 - upper, lower, capitalize, title, isupper, islower
# 공백 - stirp, lstrip, rstrip, strip(문자)
# 메서드는 점으로 이어붙이기 가능!

# replace
# 특정 문자열을 제거하거나 치환할 때 사용
# .replace("바꾸고싶은문자열", "바꿀문자열")
# 제거할 때는 인자의 두 번째를 (빈문자열)로 작성
# phone = "010-1234-1234".replace("-", "")
# print(phone)
# phone = "010-1234-1234"
# print(phone.replace("-", ""))
# print("정 상 가 동".replace(" ", ""))
# print("   정 상 가 동".replace(" ", ""))
# print("   정 상 가 동".replace("  ", ""))  # 공백이 2칸만 지움 ex) 3칸이면 2칸만 지움, 5칸이면 2*2(4)칸만 지우고 1칸 남음

# 글자 치환
# print("고장".replace("고장", "fault")) # fault
# print("고장".replace("고", "fault")) # fault장
# print("고장".replace("장", "fault")) # 고fault

# 단어 치환
# str = "설비 정상 가동"
# print(str.replace("정상", "점검"))  # 설비 점검 가동
# print(str)

# replace() 체이닝
# num = "   010-1234-1234  "
# num = num.replace(" ","").replace("-","") # 01012341234

# =====================
# print("=== split() ===")
# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에
# 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

# drinks = "에스프레소 아메리카노 카페라떼"
# print(drinks.split())  # 인자를 보내지 않음
# ['에스프레소', '아메리카노', '카페라떼']
# "띄어쓰기"를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 변환

# 구분자를 특정하고 싶은 경우
fruits = "딸기,바나나,키위,사쿠란보"
# print(
# fruits.split(",")  # 문자열 콤마를 기준으로 분할 # ['딸기', '바나나', '키위', '사쿠란보']
# fruits2 = "딸기, 바나나, 키위, 사쿠란보"
# print(fruits2.split(","))  # ['딸기', ' 바나나', ' 키위', ' 사쿠란보']
# print(fruits2.split(", "))  # ['딸기', '바나나', '키위', '사쿠란보']

# 리스트의 인덱스
# fruits_list = fruits.split(",")
# print(fruits_list)  # ['딸기', '바나나', '키위', '사쿠란보']

# 바나나만 출력하기
# 출력하고자 하는 요소의 인덱스를 대괄호로 감싸서 호출
# print(fruits_list[1]) # 바나나
# 사쿠란보 출력하기
# print(fruits_list[3]) # 사쿠란보
# print(fruits_list[-1]) # 사쿠란보

# split 횟수 제한
# num = "010-1234-1234"
# ["010", "1234-1234"]로 만들고 싶다
# print(num.split("-", 1)) # 숫자는 횟수

# str = "a,b,c,d"
# print(str.split(","))

# str = "a, b, c, d"
# print(str.split(", "))

# str = "a-b-c-d"
# print(str.split("-"))  # ['a', 'b', 'c', 'd']
# print(str.split("-", 1))  # ['a', 'b-c-d']
# print(str.split("-", 3))  # ['a', 'b', 'c', 'd']

# =============================================
# print("=== join() ===")
# 리스트를 하나의 문자열로 합침
# "구분자".join(리스트)

# fruits_list = ["딸기", "바나나", "키위", "사쿠란보"]
# print("-".join(fruits_list))  # 딸기-바나나-키위-사쿠란보
# print(",".join(fruits_list))  # 딸기,바나나,키위,사쿠란보
# print(", ".join(fruits_list)) # 딸기, 바나나, 키위, 사쿠란보

# date = ["2025", "01", "15"]
# print("-".join(date))

# a = "python"  # pyThon 으로 표현하는 방법
# # 방법 1. replace 사용
# print(a.replace("t", "T"))
# # 방법 2. 슬라이싱, 인덱스 + T만 upper 사용
# print(a[:2] + a[2].upper() + a[3:])
# # 방법 3. strip + capitalize
# print(a[:2] + a.strip("py").capitalize())
# # 방법 4. 인덱싱 + strip + title
# print(a[:2] + a.strip("py").title())
# # 방법 5. split + join
# print(a.split("t"))  # ["py" + "hon"]
# print("T".join(a.split("t")))  # pyThon
# print(a[2].upper().join(a.split("t")))  # pyThon
# print((a[2].upper()).join(a.split("t")))  # pyThon

# =============================================
# print("=== print 함수의 sep, end ===")
# print의 sep, end로 구분자 넣기
# print("2026", "07", "27", sep="-")  # 2026-07-27
# sep 속성을 사용하면 구분을 공백이 아닌 특정 문자열로 가능
# print("2026", "07", "27", sep="사랑해")  # 2026사랑해07사랑해27
# 공백 대신 sep 속성에 전달한 문자열이 삽입되어 이어짐

# print("안녕", "하세")  # 안녕 하세
# print("안녕", "하세", end="요")  # 안녕 하세요
# print("안녕", "하세", end="요", "ㅎㅎ")  # end 속성 뒤에 인자 넘기기 불가 Error
# end 속성 사용 시 출력문 마지막에 해당 문자열이 붙어 삽입

# print 함수 + 사용 시 sep과 end

# 실습 7. 구분자 통째로 바꾸기
# date = "2026/07/26"
# date = date.split("/")
# print(date) # ['2026', '07', '26']
# print("-".join(date)) # 2026-07-26

# replace vs split 선택 기준
# 언제 replace : 바꾸거나 지울 때(결과는 하나의 문자열)
# 언제 split : 나눠서 일부를 골라 쓸 때(결과는 리스트)
# 고르는 기준은? : 바꿔 하나로 둘지, 나눠 따로 쓸지

# strip + split 함께 쓰기
# strip 먼저, spli 나중 순으로 깔끔하게 나누기
# text.strip().split(',') 형태로 체이닝
# 앞뒤 공백·줄바꿈을 떼고 나눠 첫·끝조각이 깔끔
# 파일에서 읽은 줄을 다룰 때 거의 항상 이 순서

# 실습 8. CSV 한 줄에서 값 꺼내 정리하기
# a = "1, NORMAL,25.3"
# a = a.split(",")
# print(a[1].strip().lower())

name = "PUMP_A"
temp = 87
print(f"설비 {name}, 온도 {temp}도")
