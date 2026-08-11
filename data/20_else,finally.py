# except들의 연속과 finally 코드

# text = "24.5"

# print(text * 2) # 24.524.5
# 텍스트 형변환해야함!!

# temp = float(text)
# print(temp * 2)  # 49.0
# try:
# tempt = float(text)

# text = "24.5"

# try:  # try문은 except 또는 finally 중에 하나이상은 반드시 나와야함.
# temp = float(text)
# print(temp * 2)

# except ValueError:
# print("ValueError 문제가 발생했습니다.")
# temp = 0
# except NameError:
# print("NameError 문제가 발생했습니다.")
# finally:
# 오류가 있건 없건 finally의 코드를 실행해 마무리
# print('종료')

# 실습 1. finally로 파일 안전하게 닫기

# import os
# import csv

# cwd = os.getcwd()
# print(cwd)

# cwd_path = os.path.join(cwd, "08_press.csv")

# try:
#     f = open(cwd_path, "r", encoding="utf-8")
#     print(f.readline())
# except:
#     print("오류 확인바랍니다.")
# finally:
#     f.close
#     print("종료되었습니다.")

# ======================================================
# 반복문 예외처리 코드

# my_list = ["123", "22", "영크크", "141"]

# 문제 발생을 세어봅시다.
# problems = 0

# for text in my_list:
#     # 반복을 하더라도 문제가 생긴 경우만 건너뛰고
#     # 계속 반복을 이어서 진행시키기
#     try:
#         my_number = int(text)
#         print(my_number * 2)
#     except ValueError:
#         print(f"오류값 : {text}")
#         # 갈 때 가더라도 문제상황 카운팅 정도는 괜찮잖아
#         problems += 1
#         continue
# print(f"{problems}개는 문제가 있어서 건너뜀")


# 실습 2. 반복문에서 불량 줄 건너뛰기
# row_temp = [
#     10.3,
#     35.1,
#     "십오",
#     100.3,
#     50.1,
#     10.3,
#     60.2,
#     "삼십",
#     50.3,
#     "영크크",
#     "늙크크",
#     "ㅋㅋㅋ",
#     "ㅎㅎㅎ",
#     10.3,
#     5.1,
#     6.8,
# ]
# temp_sum = 0
# Error_list = []
# for temp in row_temp:
#     try:
#         temp_sum += float(temp)
#     except ValueError:
#         Error_list.append(temp)
#         continue
# print(f"온도 합계 : {round(temp_sum, 1)}")
# print(f"에러 리스트 : {Error_list}")


# 실습 3. 여러 파일 묶어 처리하기

# import csv

# file_list = ["08_press.csv", "11_if.csv", "10_if.csv"]
# file_count = 0

# for file_name in file_list:
#     try:
#         with open(file_name, "r", encoding="utf-8") as f:
#             print(f"실행 파일 이름은 {file_name}이고 \n첫 줄은 {f.readline()}입니다.")
#             file_count += 1
#     except FileNotFoundError:
#         print(f"{file_name} 파일은 없습니다.")
# print(f"실행 가능한 파일 개수는 {file_count} 입니다.")


# 실습 4. 함수 안에서 입력값 검증하기

temp = input("온도를 입력하시오.")

try:
    if temp <- 50 or temp > 100:
        raise ValueError("측정 온도를 벗어났습니다.")
except ValueError as e:
    