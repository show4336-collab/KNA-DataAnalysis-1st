# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기모드(r)로 utf-8 형식의 변환을 거쳐 읽기로 한다.
# 가져언 정보(파인 접근 열쇠/참조값)를 f에 담는다
# f = open("sample.txt", "r", encoding="utf-8")

# print(type(f))  # <class '_io.TextIOWrapper'>
# print(type(f).__name__)  # TextIOWrapper

# 텍스트파일 파일 한줄씩 문자열을 만들기

# lines = f.readlines()
# print(lines)  # ['Hello World!\n', '어서오세요 반갑습니다.\n', '만나서 정말 좋아요.']


# f.close()  # 열었다면 언제가는 꼭 닫아줍시다.


# 만약 신경써서 파일 닫기(close) 해주기 귀찮다면
# with open .... as 문법을 쓰는 것도 좋다

# with open("sample.txt", "r", encoding="utf-8") as f:
# 앞으로 이렇게 들여쓰기 된 코드가 끝나면
# 파일 접근을 닫습니다(close)

# 텍스트파일 파일 한줄씩 문자열을 만들기

# lines = f.readlines()
# 조건문처럼 들여쓰기 해야함.

# print(lines)

# 실습 1. open으로 파일읽기

# f = open("sample.txt", "r", encoding="utf-8")
# print(f.read())
# f.close()

# with open("sample.txt", "r", encoding="utf-8") as f:
#     print(f.readlines())
# ================제출===============
# 위 또는 아래
# lines = f.readlines()

# print(lines)
# ==================================


# ==================================
# with open("hello.txt", "w", encoding="utf-8") as f:
# 없는 파일이면 만들어버림.
# f.write("안녕하세요")
# f.write("반갑습니다")
# hello.txt에 안녕하세요반갑습니다
# 라고 이어서 적힘.
# 줄바꾸려면 \n 해야함.
# # f.write("안녕하세요.\n반갑습니다.")
# # f.write("안녕하세요.\n\t반갑습니다.")
# # \t는 탭임.


# 실습 2. with open으로 파일에 쓰기
# with open("hello.txt", "w", encoding="utf-8") as f:
#     f.write("안녕하세요.\n반갑습니다.")


# with open("hello.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# =========================================

# 실습 3. 모드로 기록 이어붙이기

# with open("hello.txt", "a", encoding="utf-8") as f:
#     f.write("\n내 이름은 \n\t000입니다.")

# with open("hello.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# ==============================


# import os
# import sys

# csv_path = os.path.join("data", "08_press.csv")

# if os.path.exists(csv_path):
#     print("파일을 찾았습니다.")

# 위 경로의 파일을 찾지 못하면 강제종료시키기
# if not os.path.exists(csv_path):
#     print("파일이 없습니다.")
#     sys.exit(1)  # 비정상 종료시 0이 아닌 1을 전달

# with open(csv_path, "r", encoding="utf-8") as f:
#     print(f.readlines())

# import csv

# with open(csv_path, "r", encoding="utf-8") as f:
#     #    # print(f.readlines()) # 이제 csv에게 맡깁시다.
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)  # 각 행(row)마다 리스트로 출력됨

# ===============================================

# csv.reader - 코드로 확인
# import csv

# with open("08_press.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# 각 행이 리스트로 출력됨

# 실습 4. csv.reader로 CSV 읽기
# import csv

# with open("08_press.csv", 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# csv.writer - 코드로 확인

# import os
# import csv

# path = os.getcwd()

# csv_path = os.path.join(path, "result.csv")

# with open("result.csv", "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["시각", "설비"])
#     writer.writerow(["09:00", "PUMP-01"])

# 실습 5. csv.writer로 csv 쓰기

# import os
# import csv

# cwd = os.getcwd()

# csv_path = os.path.join(cwd, "result.csv")

# with open(csv_path, "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["설비이름", "온도"])
#     writer.writerow(["PUMP-1", 89])

# ============================
# csv.Dictreader()
# Dictreader는 첫줄은 컬럼 이름으로 판단하고
# 각 row를 해당 컬럼이름들을 key로 하는 딕셔너리로 만들어줌

# import os
# import csv

# cwd = os.getcwd()

# csv_path = os.path.join(cwd, "08_press.csv")

# with open(csv_path, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(row["설비ID"], row.get("시각", 0))


# 실습 6. CSV 읽어 조건 저장하기
# import csv
# import os

# cwd = os.getcwd()

# cwd_path = os.path.join(cwd, "08_press.csv")

# over_row = []

# with open(cwd_path, "r", encoding="utf-8") as f:
# reader = csv.DictReader(f) # DictReader가 아닌 그냥 reader를 쓴다면
# 보통 csv파일의 첫줄인 헤더줄도 읽어버린다.
# reader에게 첫줄은 건너뛰라고 말하는 방법이 필요하다
# next(reader)는 한줄뛰고 reader가 반응하게 한다.
# 방법 1. header = next(reader)
# header를 하고 나면 커서가 첫줄을 넘어가서
# reader는 두번째 줄부터 나옴
# pirnt(header)는 첫줄만 리스트로 나옴
# 방법 2. for 문 in reader[1:] 로 해도 되는데 방법 1을 주로 씀
#     reader = csv.reader(f)
#     header = next(reader)
#     for rows in reader:
#         if float(rows[4]) > 90:
#             over_row.append(rows)
# with open("over_row_list.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     for row in over_row:
#         writer.writerow(row)

# ===========================================

# 실습 1. 트레이스백으로 에러 읽기

# int("하이")  # ValueError
# 9 / 0 # ZeroDivisionError
# max(hi) # NameError

# 실습 2. try-except로 오류 넘기기

# origin = input("온도 : ")

# print(f"입력한 온도는 {origin}")

# temp = 0

# try:
#     temp = int(origin)
# except ValueError:
#     # ValueError인 상황이였다면 여기로 예외처리
#     print("숫자 아니면 왜 저를 부르셨어요?")

# next_temp = temp + 10
# print(f"10도만 더 높으면 {next_temp}")

# 실습 3. 구체적 예외로 입력 검증하기

press_1st = input("압력 : ")

print(f"입력한 압력은 {press_1st}")

try:
    press = int(press_1st)
except ValueError:
    print("숫자를 입력해야해요.")
except ZeroDivisionError:
    print("0으로 나눴나요?")
