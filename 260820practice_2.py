def line():
    print("=" * 40)


import pandas as pd

line()

df = pd.read_csv(".venv/15_사출성형_로그.csv", encoding="utf-8")
print("실습 1. 눈으로 결측 찾기")

# print(df.head(3))
# print(df.describe())


# 설비 센서 데이터를 불러와 isna로 컬럼별 NaN 개수 세기
print(df.isna().sum())  # True = 1, False = 0 합산
# 조건 필터링으로 압력 0, 진동 -999 같은 위장 결측 개수 세기
print((df["사출압력"] == 0).sum())  # 2
print((df["스크루속도"] == -999).sum())  # 2

# 진짜 결측과 위장 결측을 나눠 비교


line()
print("실습 2. SECOM 첫 탐색")
df = pd.read_csv(".venv/15_01_사출성형_공정.csv", encoding="utf-8")


print(df.head(2))
print(df.shape)  # (250, 22)
# df.info()

print(df.describe())

line()
print("실습 3. 위장 결측 사냥")

df = pd.read_csv(".venv/15_사출성형_로그.csv", encoding="utf-8")

# 위장 결측이 있는 열을 조건 필터링으로 추출해 확인
print((df["배럴온도"] == 999).sum())  # 1
print((df["스크루속도"] == -999).sum())  # 2

# na_values로 위장값을 결측으로 인식해 다시 불러오기
df = pd.read_csv(".venv/15_사출성형_로그.csv", encoding="utf-8", na_values=(-999, 999))

# 변환 전후 결측 개수를 비교
print((df["배럴온도"] == 999).sum())  # 0
print((df["스크루속도"] == -999).sum())  # 0

line()
print("실습 4. 컬럼별 결측 개수와 비율")

df = pd.read_csv(".venv/15_01_사출성형_공정.csv", encoding="utf-8")

counts = df.isna().sum()
print(counts)
# 측정시각        0
# 불량여부        0
# 사이클시간       0
# 성형사이클       0
# 배럴온도1       0
# 배럴온도2       0
# 배럴온도3       0
# 배럴온도4       0
# 호퍼온도        0
# 최대사출속도      0
# 사출압력        1
# 스크루위치       3
# 전환위치        5
# 계량시간        9
# 계량시작점       9
# 최대사출압      34
# 전환압력       34
# 계량시작위치     34
# 스크루속도      60
# 최소쿠션       68
# 계량종료점     109
# 감압시간      109

ratio = (counts / len(df) * 100).round(1)
print(ratio)
# 측정시각       0.0
# 불량여부       0.0
# 사이클시간      0.0
# 성형사이클      0.0
# 배럴온도1      0.0
# 배럴온도2      0.0
# 배럴온도3      0.0
# 배럴온도4      0.0
# 호퍼온도       0.0
# 최대사출속도     0.0
# 사출압력       0.4
# 스크루위치      1.2
# 전환위치       2.0
# 계량시간       3.6
# 계량시작점      3.6
# 최대사출압     13.6
# 전환압력      13.6
# 계량시작위치    13.6
# 스크루속도     24.0
# 최소쿠션      27.2
# 계량종료점     43.6
# 감압시간      43.6


# 결측이 있는 컬럼만 골라 개수와 비율을 나란히 정리
table = pd.DataFrame({"개수": counts, "비율": ratio})
print(table[table["개수"] > 0])


line()
print("실습 5. 결측 순위와 행별 분석")


# 결측 비율을 내림차순 정렬해 가장 심한 컬럼 확인
print(ratio.sort_values(ascending=False).head(3))
# 계량종료점    43.6
# 감압시간     43.6
# 최소쿠션     27.2
# 방향을 가로(행)로 바꿔 행마다 결측 개수 세기
# NaN 합산대상을 y축 방향별로 컬럼별로 하는게 아니라
# x축방향별로 각 row마다 처리하기
df_axis = df.isna().sum(axis=1)
print(f"결측없는 행 {(df_axis == 0).sum()}개")  # 결측없는 행 76개
print(f"결측있는 행 {(df_axis > 0).sum()}개")  # 결측있는 행 174개
# 결측이 많은 부실 행만 조건으로 골라내기
print(f"결측 5개 이상있는 행 {(df_axis >= 5).sum()}개")  # 결측 5개 이상있는 행 27개


line()
