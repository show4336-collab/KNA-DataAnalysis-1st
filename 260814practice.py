def line():
    print("=" * 40)


import pandas as pd

line()
print("실습 1. 단일 조건으로 행 추출하기")

df = pd.read_csv(".venv/13_diecasting_small.csv")
# df.info()
df_pressure = df["실린더압력"] >= 230

print(len(df_pressure))  # 30
print(df_pressure.sum())  # 5

line()
print("실습 2. 임계값 넘는 설비 골라내기")
df = pd.read_csv(".venv/13_diecasting_small.csv")

s_limit = df["비스킷두께"] >= 16  # series
# print(df[s_limit])
# 위, 아래는 동일한 코드임.
print(df[df["비스킷두께"] >= 16])

print(len(df[df["비스킷두께"] >= 16]))  # 5


df_sub = df[df["비스킷두께"] >= 16]

print(df_sub[["샷", "비스킷두께"]])
# 위, 아래는 동일한 코드임
print(df[df["비스킷두께"] >= 16][["샷", "비스킷두께"]])

line()

print("실습 3. 두 조건 묶기")
df = pd.read_csv(".venv/13_diecasting_shot.csv")

df_both = df[(df["비스킷두께"] >= 13) & (df["사이클타임"] >= 25)]
print(len(df_both))  # 83

df_either = df[(df["비스킷두께"] >= 13) | (df["사이클타임"] >= 25)]
print(len(df_either))  # 104


line()


line()
print("실습 4. 부정 목록 범위 조건")

df = pd.read_csv(".venv/13_diecasting_shot.csv")
# print(df["품질등급"] == "불량")  # True, False 반환
print(len(df[df["품질등급"] == "불량"]))  # 20

# 불량이 아닌 것들은?
print(len(df[~(df["품질등급"] == "불량")]))  # 180
print(len(df[(df["품질등급"] == "양품") | (df["품질등급"] == "주의")]))  # 180

# print(len(df["품질등급"].isin(["양품", "주의"])))  # True, False로 반환되서 200
print(len(df[df["품질등급"].isin(["양품", "주의"])]))  # 180

# between으로 실린더압력값 지정 범위에 든 행 추출 : 210 ~ 230
print(len(df[df["실린더압력"].between(210, 230)]))  # 89

# 그 외의 것들로

print(len(df[~df["실린더압력"].between(210, 230)]))  # 111
