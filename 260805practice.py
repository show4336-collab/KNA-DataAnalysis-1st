import random
import math
import os
import datetime


def line():
    print("=" * 40)


line()

print("실습 1. import 세 방식으로 모듈 가져오기")


print(math.sqrt(16))

from math import sqrt

print(sqrt(16))

import math as mt

print(mt.sqrt(16))

line()

print("실습 2. 표준 라이브러리로 센서값 만들기")


sensor_value = random.randint(1, 10)

print(f"무작위 값 : {sensor_value}, 제곱근 : {math.sqrt(sensor_value)}")

line()


print("실습 4. os로 파일 존재 확인하기")

path = os.path.join("KNA-DataAnalysis-1st", "17_function.py")

print(os.path.exists("17_function.py"))

if os.path.exists("17_function.py"):
    print("파일 있음.")
else:
    print("없습니다.")


line()

print("실습 5. datetime으로 점검 기록 남기기")

files_count = len(os.listdir())
now_time = datetime.datetime.now()

print(f"파일 {files_count}개, 점검 시각 {now_time}")


print("====================심화문제====================")

print("실습 3. os로 폴더 목록 살펴보기")

cwd = os.getcwd()
current_list = os.listdir(cwd)

print(f"{cwd}")
print(f"{current_list}")

for csv_file in current_list:
    if csv_file.endswith(".csv"):
        print(f"{csv_file}")


line()
print("실습 6. 폴더에서 csv 파일만 골라내기")

dict_list = os.listdir()
csv_list = []
for file in dict_list:
    if file.endswith(".csv"):
        csv_list.append(file)

for csv_dict in csv_list:
    path = os.getcwd()
    print(f"({path} 목록 {csv_dict}")

# 실습 5. csv.writer로 csv 쓰기

import os
import csv

cwd = os.getcwd()

csv_path = os.path.join(cwd, "result.csv")

with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["설비이름", "온도"])
    writer.writerow(["PUMP-1", 89])
