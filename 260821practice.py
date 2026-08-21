def line():
    print("=" * 40)


import pandas as pd

# line()

# df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")
# print("실습 1. dropna로 행 열 삭제")

# 원본 크기를 shape로 확인
# print(df.shape)  # (250, 22)

# dropna로 결측 있는 행을 모두 삭제
# print(df.dropna().shape)  # (76, 20)

# 방향을 열로 바꿔 결측 있는 열을 삭제
# print(df.dropna(axis=1).shape)  # (250, 10)


# line()
# print("실습 2. dropna 옵션 조절")

# how로 완전히 빈 행만 삭제하는 기준 적용 # how = 'all'
# print(df.dropna(how="all").shape)  # (250, 22) -> 완전히 빈 행은 없음

# thresh로 값이 일정(예, 20개) 개수 '이상'인 행만 남기기 -> thresh = 20
# print(df.dropna(thresh=20).shape)  # (162, 22)
# -> 250 - 162 = 88개 row는 NaN이 3(22개 열에서 20개열) 개 이상이라는 뜻

# subset으로 특정 컬럼이 빈 행만 삭제
# print(df.dropna(subset=["불량여부"]).shape)  # (250, 22)
# '불량여부' 컬럼에는 NaN이 하나도 없다고 판단 가능


# line()
# print("실습 3. 결측 비율 기준컬럼 제거")
# df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")


# 컬럼별 결측 비율을 계산
# df_rate = df.isna().sum() / len(df)
# print(df_rate)

# 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기

# df_40 = df_rate[df_rate > 0.4]
# print(df_40)
# 최대사출속도    0.436
# 감압시간      0.436

# list_df_40 = df_rate[df_rate > 0.4].index.tolist()
# print(list_df_40)  # ['최대사출속도', '감압시간']
# 그 컬럼들을 drop으로 제거하고 크기 확인
# df_final = df.drop(columns=list_df_40)
# print(df_final.columns)


# line()
# print("실습 4. 삭제 손실 비교")
# df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")

# print(df.shape)

# df_compare = pd.DataFrame(
#     {
#         "방식": ["원본", "행삭제", "thresh20"],
#         "행": [len(df), len(df.dropna()), len(df.dropna(thresh=20))],
#     }
# )

#          방식    행
# 0        원본  250
# 1       행삭제   76
# 2  thresh20  162
# df_compare["손실률"] = ((1 - (df_compare["행"] / len(df))) * 100).round(2)
# print(df_compare)
#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2


# line()
# print("실습 5. fillna 평균·중앙값 대체")
# df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")

# print(df["최대사출압"].isna().sum())  # 60개 NaN

# 대상 컬럼의 평균과 중앙값을 각각 구해 비교
# fillna로 평균을 채운 결과 만들기
# df_mean = df["최대사출압"].mean()
# print(f"최대사출압의 평균 : {df_mean.round(2)}")
# 최대사출압의 평균 : 1241.67

# s_fillmean = df["최대사출압"].fillna(df_mean)
# print(s_fillmean)
# df["최대사출압"] = s_fillmean
# print(df["최대사출압"].isna().sum())  # 최대사출압 컬럼의 NaN 0개

# fillna로 중앙값을 채운 결과 만들기(이상치에 강함)
# df_median = df["최대사출압"].median()
# print(f"최대사출압의 중앙값 : {df_median}")
# 최대사출압의 중앙값 : 1240.84

# s_fillmedian = df["최대사출압"].fillna(df_median)
# print(s_fillmedian)
# df["최대사출압"] = s_fillmedian
# print(df["최대사출압"].isna().sum())  # 최대사출압 컬럼의 NaN 0개

# 예상 결과
# 센서17 평균 466.26·중앙값 465.9로 대체, 남은 결측 0

# line()
# print("실습 6. 최빈값·앞뒤 값 대체")
# df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")
# 범주형은 최빈값, 시계열은 앞뒤 값으로 채우기

# 범주형 열의 최빈값을 구해 채우기
# 사출기 컬럼은 1~3호기 범주형으로 판단
# print(df["사출기"].isna().sum())  # 0
# print(df["사출기"].mode()[0])  # 1호기

# df["사출기"] = df["사출기"].fillna(df["사출기"].mode()[0])
# print(df["사출기"].isna().sum())  # 0개!

# 측정시각 순으로 정렬해 시계열 순서 만들기
# df = df.sort_values("측정시각")

# ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기
# print(df["전환압력"].isna().sum())  # 68개 NaN
# df["전환압력"] = df["전환압력"].ffill().bfill()  # 자주 볼 시계열 채우기 패턴
# print(df["전환압력"].isna().sum())  # 0개 NaN

# 예상 결과
# 설비명은 최빈값(절삭기A), 온도는 앞뒤 값으로 대체

# line()
# print("실습 7. 그룹별 대체")
# df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")
# 그룹별 평균으로 채워 집단 특성 반영

# · 제품유형으로 그룹을 나누기
# print(df.groupby("사출기")["감압시간"].mean())
# 1호기    0.322179
# 2호기    0.322368
# 3호기    0.322400

# 각 그룹의 평균으로 그 그룹의 결측을 채우기

# 사출기별로 그룹을 나누고
# 그룹마다 갑압시간의 시리즈를 뽑아서
# 그 시리즈의 NaN들을 그 시리즈의 평균들로 채운다
# df["감압시간"] = df.groupby("사출기")["감압시간"].transform(
#     lambda x: x.fillna(x.mean())
# )

# print(df["감압시간"].isna().sum())  # 0

# df_numbers = df.select_dtypes("number")
# df[df_numbers.columns] = df_numbers.fillna(df_numbers.median())

# print(df.isna().sum())
# print(df.isna().sum().sum())

# 예상 결과
# 토크를 유형별 평균으로 대체, 남은 결측 0


print("실습 8. 제거 vs 대체 비교")
df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")

# 같은 데이터에 제거와 대체를 적용해 결과 비교

# 결측 심한 컬럼을 먼저 뺀 기준 데이터 만들기
print(df.isna().sum())
# 최대사출속도    109
# 감압시간      109
standard = df.drop(columns=["최대사출속도", "감압시간"])
standard.info()  # 최대사출속도, 감압시간 컬럼 제거 확인
print(standard.shape)  # (250, 20)

# 기준 데이터에서 결측 행을 삭제한 제거 버전 만들기
remover = standard.dropna()
print(remover.shape)  # (110, 20)

# 기준 데이터의 결측을 중앙값으로 채운 대체 버전 만들기
replaced = standard.fillna(standard.median(numeric_only=True))
print(replaced.shape)  # (250, 20)

# 예상 결과
# 제거 버전 110행, 대체 버전 250행(모두 유지)


# print("실습 9. SECOM·AI4I 종합 처리")
df = pd.read_csv(".venv/15_02_사출성형_공정.csv", encoding="utf-8")

# 제거와 대체를 조합해 전체 결측을 처리하고 저장

# 결측 비율 높은 컬럼을 제거하고 나머지는 중앙값으로 채우기
# 앞서 처리한 대체판 재사용!

# 처리 후 남은 결측과 크기를 확인하고 파일로 저장
print(replaced.isna().sum().sum())  # 0
replaced.to_csv(".venv/15_02_사출성형_공정_clean.csv", index=False, encoding="utf-8")

# 같은 절차를 AI4I 데이터에도 반복해 결측 0 확인

# 예상 결과
# SECOM 결측 0·저장, AI4I 결측 0
