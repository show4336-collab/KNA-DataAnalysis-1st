def line():
    print("=" * 50)


import pandas as pd

line()

print("실습 1. 데이터 불러오기와 구조 확인하기")

df = pd.read_csv(".venv/13_diecasting_small.csv")
print(df.shape)  # (30, 7)
print(
    df.columns
)  # Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='str')


line()
print("실습 2. 열 선택하기")

df = pd.read_csv(".venv/13_diecasting_small.csv")
print(df["형체력"])
df["형체력"].info()  # Series

df[["형체력", "실린더압력"]].info()  # DataFrame
print(round(df["형체력"].mean(), 1))  # 267.8
print(round(df["실린더압력"].mean(), 1))  # 219.7
# 밑에는 응용해봤습니다. 데이터프레임도 이렇게 쓸 수 있는군요.
# print(round(df[["실린더압력", "형체력"]].mean(), 1))  # 실린더 압력 219.7  형체력 267.8
# print(df[["실린더압력", "형체력"]].max())
# print(df[["실린더압력", "형체력"]].min())
# print(df[["실린더압력", "형체력"]].std())
# print(df[["실린더압력", "형체력"]].describe())

line()
print("실습 3. 공정 센서 열 골라내기")

df = pd.read_csv(".venv/13_diecasting_shot.csv")

# print(df.columns)

s = df["형체력"]
s.info()  # series

print(df[["형체력", "실린더압력", "주조압력"]].shape)  # (200, 3)


line()

print("실습 4. loc와 iloc로 행 선택하기")

# import pandas as pd

df = pd.read_csv(".venv/13_diecasting_shot.csv")
print(df.loc[0])
print(df.iloc[0])
# 위는 동일

# print(df.loc[0, "품질등급"])  # 양품
# print(df.iloc[0]["품질등급"])  # 양품
# print(len(df.loc))
# print(len(df.iloc[3, 2]))
print(len(df.loc[0:2]))  # 3 loc은 0, 1, 2
print(len(df.iloc[0:2]))  # 2 iloc은 0, 1

line()

print("실습 5 loc iloc로 행 열 동시 선택하기")

print(df.loc[:4, ["형체력", "주조압력"]].shape)  # (5, 2)
print(df.loc[6:10, ["형체력", "주조압력", "사이클타임"]].shape)  # (5, 3)
print(df.iloc[-3:].shape)  # (3, 7)
# 샷  실린더압력   주조압력   사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0  255.0    36.6   27.0  354.0   불량
# 198  199  264.0  595.0    36.1   19.0  372.0   불량
# 199  200  108.0  525.0  6170.0   15.0  237.0   불량

line()

print("실습 6. 특정 구간 추출 종합")
df_shot = pd.read_csv(".venv/13_diecasting_shot.csv")

cols = ["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]
print(df_shot[cols].iloc[0:10].shape)  # 결과는? (10, 5)
print(df_shot.loc[:10, ["주조압력", "사이클타임"]].shape)  # 결과는 ? (11, 2)
print(df_shot.iloc[:10, :6].shape)  # (10, 6)

line()
