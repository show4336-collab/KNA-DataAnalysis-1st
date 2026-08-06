def line():
    print("=" * 60)


line()

print("실습 2. with open으로 파일에 쓰기")


with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요.\n반갑습니다.")


with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())

line()

print("실습 3. 모드로 기록 이어붙이기")

with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("\n내 이름은 \n\t000입니다.")

with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())

line()

print("실습 4. csv.reader로 CSV 읽기")

import csv

with open("08_press.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

line()

print("실습 6. CSV 읽어 조건 저장하기")


import csv
import os

cwd = os.getcwd()

cwd_path = os.path.join(cwd, "08_press.csv")

over_row = []

with open(cwd_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for rows in reader:
        if float(rows[4]) > 90:
            over_row.append(rows)
with open("over_row_list.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in over_row:
        writer.writerow(row)

line()

print("실습 3. 구체적 예외로 입력 검증하기")


press_1st = input("압력 : ")

print(f"입력한 압력은 {press_1st}")

try:
    press = int(press_1st)
except ValueError:
    print("숫자를 입력해야해요.")
except ZeroDivisionError:
    print("0으로 나눴나요?")

line()
