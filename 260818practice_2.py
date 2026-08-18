def line():
    print("=" * 40)


import pandas as pd

df = pd.read_csv(".venv/students_groupby_practice.csv", encoding="utf-8")

line()
print("[문제 1] 이 학교의 전체 학생 수를 구하세요.")

print(len(df))  # 60


line()
print("[문제 2] 학년별 학생 수를 구하세요.")
print(df.groupby("학년").size())
print(df["학년"].value_counts())  # 1 20 2 20 3 20

line()
print("[문제 3] 학년 내 각 반별 학생 수를 구하세요.")
print((df.groupby(["학년", "반"]).size()))
print(df[["학년", "반"]].value_counts())

line()
print("[문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.")
print(df.groupby(["학년", "반"])["국어"].mean().round(2))

line()
print("[문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요.")
print(df.groupby("학년")["영어"].mean().round(2))

line()
print("[문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.")
print(df["수학"].mean().round(2))

line()
