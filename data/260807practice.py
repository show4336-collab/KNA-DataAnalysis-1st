def line():
    print("=" * 60)


import os
import csv

line()

print("실습 1. finally로 파일 안전하게 닫기")

cwd = os.getcwd()

cwd_path = os.path.join(cwd, "data", "08_press.csv")

f = None

try:
    f = open(cwd_path, "r", encoding="utf-8")

except FileNotFoundError:
    print("오류확인")

finally:
    if f is not None:
        f.close()


line()
print("실습 2. 반복문에서 불량 줄 건너뛰기")

row_temp = [
    10.3,
    35.1,
    "십오",
    100.3,
    50.1,
    10.3,
    60.2,
    "삼십",
    50.3,
    "영크크",
    "늙크크",
    "ㅋㅋㅋ",
    "ㅎㅎㅎ",
    10.3,
    5.1,
    6.8,
]

temp_sum = 0
Error_list = []

for temp in row_temp:
    try:
        temp_sum += float(temp)

    except ValueError:
        Error_list.append(temp)
        continue

print(f"온도 합계 : {round(temp_sum, 1)}")
print(f"에러 리스트 : {Error_list}")


line()
print("실습 3. 여러 파일 묶어 처리하기")

file_list = ["08_press.csv", "11_if.csv", "10_if.csv"]
file_count = 0

for file_name in file_list:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            print(f"실행 파일 이름은 {file_name}이고 \n첫 줄은 {f.readline()}입니다.")
            file_count += 1

    except FileNotFoundError:
        print(f"{file_name} 파일이 없습니다.")

print(f"실행 가능한 파일 개수는 {file_count} 입니다.")


line()


print("종합실습")
print("실습 - 1단계 CSV 읽기")

cwd = os.getcwd()

cwd_path = os.path.join(cwd, "data", "09_ict_inspection.csv")


def len_rows():
    print(f"행의 수는 {len(rows)}")


f = None
header = []
rows = []

try:
    f = open(cwd_path, "r", encoding="utf-8")

    reader = csv.reader(f)

    header = f.readline()

    rows = f.readlines()

except FileNotFoundError:
    print("파일이 없습니다.")

finally:
    if f is not None:
        f.close()

print(f"{header}, {rows}")
len_rows()


line()


print("실습 - 2단계 조건 분류")

name_list = []
values = {}
E2_count = 0
F2_count = 0
B2_count = 0
A2_count = 0
D2_count = 0
Error_count = 0

with open(cwd_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    header = f.readline()

    for value in reader:
        sensor_name = value[1]

        values = {sensor_name: value[2:]}

        name_list.append(sensor_name)

        for counts in values.keys():

            if counts == "E2":
                E2_count += 1

            elif counts == "F2":
                F2_count += 1

            elif counts == "B2":
                B2_count += 1

            elif counts == "A2":
                A2_count += 1

            elif counts == "D2":
                D2_count += 1

            else:
                Error_count += 1


print(
    f"E2는 {E2_count}개, F2는 {F2_count}개, "
    f"B2는 {B2_count}, A2는 {A2_count}, "
    f"D2는 {D2_count}, 그 외 {Error_count}개"
)


line()


print("실습 - 3단계 통계 함수")

cwd = os.getcwd()

cwd_path = os.path.join(cwd, "data", "student_scores.csv")

avg_all = 0
students_count = 0
max_student = 0
min_student = 101

with open(cwd_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", "이름없음")

        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))

        avg = (kor + eng + math) / 3

        students_count += 1
        avg_all += avg

        if avg > max_student:
            max_student, max_student_name = avg, name

        if avg < min_student:
            min_student, min_student_name = avg, name


print(f"전체 평균은 {round(avg_all / students_count, 1)}")
print(f"최고점 학생의 이름은 {max_student_name}, " f"점수는 {round(max_student, 1)}")
print(f"최저점 학생의 이름은 {min_student_name}, " f"점수는 {round(min_student, 1)}")


line()


print("실습 - 4단계 불량 방어")

temp_list = [10, 20, 50, 80, "열", "십", "삼십", 100, 150]

error_list = []
normal_list = []

row_number = 1

for value in temp_list:
    try:
        temp = float(value)

        if temp < -50 or temp > 100:
            raise ValueError("측정 온도를 벗어났습니다.")

        normal_list.append(temp)

    except ValueError as e:
        error_list.append([row_number, value, str(e)])
        continue

    finally:
        row_number += 1


print(f"정상 값 : {normal_list}")
print(f"불량 데이터 : {error_list}")


line()


print("실습 - 5단계 리포트 저장")

report = [
    "종합실습 결과",
    "=" * 60,
    "실습 - 1단계 CSV 읽기",
    f"행의 수는 {len(rows)}",
    "=" * 60,
    "실습 - 2단계 조건 분류",
    f"E2는 {E2_count}개, F2는 {F2_count}개, "
    f"B2는 {B2_count}개, A2는 {A2_count}개, "
    f"D2는 {D2_count}개, 그 외 {Error_count}개",
    "=" * 60,
    "실습 - 3단계 통계 함수",
    f"전체 평균은 {round(avg_all / students_count, 1)}",
    f"최고점 학생의 이름은 {max_student_name}, " f"점수는 {round(max_student, 1)}",
    f"최저점 학생의 이름은 {min_student_name}, " f"점수는 {round(min_student, 1)}",
    "=" * 60,
    "실습 - 4단계 불량 방어",
    f"정상 값 : {normal_list}",
    f"불량 데이터 : {error_list}",
]


with open("report_result.txt", "w", encoding="utf-8") as f:
    for text in report:
        f.write(text + "\n")


# 저장된 파일 다시 열어서 확인
f = None

try:
    f = open("report_result.txt", "r", encoding="utf-8")
    print(f.read())

except FileNotFoundError:
    print("리포트 파일이 없습니다.")

finally:
    if f is not None:
        f.close()


line()


print("실습 - 6단계 통계 검증")

sensor_count_sum = E2_count + F2_count + B2_count + A2_count + D2_count + Error_count

print(f"설비별 데이터 개수 합 : {sensor_count_sum}")
print(f"전체 데이터 개수 : {len(rows)}")

print(f"검증 결과 : {sensor_count_sum == len(rows)}")


line()


print("선택문제")
print("실습 4. 함수 안에서 입력값 검증하기")


def check_sensor(value, min_value, max_value):
    try:
        value = float(value)

        if value < min_value or value > max_value:
            raise ValueError("정상 범위를 벗어났습니다.")

        return value

    except ValueError as e:
        print(f"오류 : {e}")
        return 0


print(check_sensor(50, 0, 100))
print(check_sensor("십", 0, 100))
print(check_sensor(150, 0, 100))
