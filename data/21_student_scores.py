# 학생들의 점수를 가져와서
# 각 학생별 합계와
# 모든 학생들의 평균 점수를 내는 코드

import os
import csv
import sys

# 1. 파일을 연다.

cwd = os.getcwd()

cwd_path = os.path.join(cwd, "data", "student_scores.csv")

if not os.path.exists(cwd_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)


# 미리 전체 합산 점수 낼 준비를 한다.
avg_all = 0
students_count = 0
max_student = 0
min_student = 101
avg_kor = 0
avg_eng = 0
avg_math = 0

with open(cwd_path, "r", encoding="utf-8") as f:
    # 2. 파일 내용으로부터 리스트 데이터를 읽는다.
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", "이름없음")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))
        avg = (kor + eng + math) / 3
        print(f"{name} | {kor} | {eng} | {math} | {round(avg, 1)}")
        # 3. 점수 계산(합계, 평균)
        students_count += 1
        avg_all += avg
        if avg > max_student:
            max_student, max_student_name = avg, name
        if avg < min_student:
            min_student, min_student_name = avg, name
        avg_kor += kor
        avg_eng += eng
        avg_math += math


# 4. 결과를 화면에 보여주기
print(f"전체 평균은 {round(avg_all / students_count, 1)}")
print(f"최고점 학생의 이름은 {max_student_name}, 점수는 {round(max_student, 1)}")
print(f"최저점 학생의 이름은 {min_student_name}, 점수는 {round(min_student, 1)}")
print(f"국어 평균은 {round(avg_kor / students_count, 1)}")
print(f"영어 평균은 {round(avg_eng / students_count, 1)}")
print(f"수학 평균은 {round(avg_math / students_count, 1)}")

# 제출 안하는 실습
# 1. 실행 끝날 때 최고점 학생, 최저점 학생도 찾아서 출력해보세요.
# 2. 실행 끝날 때 각 과목별 평균도 출력해보세요.
