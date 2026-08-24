def line():
    print("=" * 40)


import pandas as pd

df = pd.read_csv(".venv/16_diecasting.csv", encoding="utf-8")

line()
print("실습 1. 주조 데이터 구조 분포 살펴보기")

print(df.head(2))
#    샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력  상태
# 0  1  214.0  1037.0   20.7   10.0  258.0   0
# 1  2  217.0  1052.0   20.7   11.0  257.0   0
print(df.shape)  # (202, 7)
print(df.columns)
# df.info()
print(df[["실린더압력", "사이클타임"]])

line()
print("실습 2. 한 컬럼의 최소 최대 범위")
print(df["실린더압력"].min())  # 108
print(df["실린더압력"].max())  # 265
print(df["실린더압력"].max() - df["실린더압력"].min())  # 157

line()
print("실습 3. 정렬해서 이상치 후보 찾기")

s_sorted = df.sort_values("사이클타임", ascending=False)
print(s_sorted.head(4))  # 주조압력 6170.0, 652.3 발견!


line()
print("실습 4. 평균 중앙값으로 이상치 영향 확인")

print(df["사이클타임"].agg(["mean", "median"]))  # mean 64.75 median 22.60
print(df[df["상태"] == 0])
print(df[df["상태"] == 0].agg(["mean", "median"]).round(2))  # 평균 27.67

line()
print("실습 5. quantile로 Q1, Q2, Q3")
print(df["실린더압력"].quantile(0.25))  # 215.75
print(df["실린더압력"].quantile(0.50))  # 218.0
print(df["실린더압력"].median())  # 218.0
print(df["실린더압력"].quantile(0.75))  # 265.0

line()
print("실습 6. describe로 격차 큰 컬럼 찾기")
print(df.describe())
report = (
    df[["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]].describe().T
)
# .T는 axis를 바꿔서 보여줌!!!
print(report)

# 격차가 큰 순으로 정렬해 이상치 의심 컬럼 확인
# 격차라는 새로운 컬럼을 추가해서 계산 결과들을 담기
# 그 다음에 격차 결과순서로 정렬
report["격차"] = (report["mean"] - report["50%"]).abs()
print(report.head())
print(
    report.sort_values("격차", ascending=False)[["mean", "50%", "max", "격차"]].head(3)
)
# .T를 했던 이유는 격차라는 열을 넣기위해 쉬운 코드를 쓰려다 보니 쓴 이유도 있음!!


line()
print("실습 7. 여러 컬럼의 가운데 절반 폭 비교")
df_q = df[["실린더압력", "사이클타임", "비스킷두께"]].quantile([0.25, 0.5, 0.75])
print(df_q)
print(df_q.loc[0.75])
# 실린더압력    265.000
# 사이클타임     35.925
# 비스킷두께     17.000
# Name: 0.75, dtype: float64
print(df_q.loc[0.75] - df_q.loc[0.25])
# 실린더압력    49.250
# 사이클타임    15.125
# 비스킷두께     6.000
# dtype: float64
