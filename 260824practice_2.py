def line():
    print("=" * 40)


import pandas as pd

df = pd.read_csv(".venv/16_diecasting.csv", encoding="utf-8")

line()
print("실습 1. IQR과 이상치 경계 구하기")

q1 = df["사이클타임"].quantile(0.25)
q3 = df["사이클타임"].quantile(0.75)
iqr = (q3 - q1).round(2)
print(iqr)  # 15.12
lower = q1 - (iqr * 1.5)
upper = q3 + (iqr * 1.5)
print(f"사이클타임 IQR {iqr}, 하한 {lower.round(1)} 상한 {upper.round(1)}")
# 사이클타임 IQR 15.12, 하한 -1.9 상한 58.6


line()
print("실습 2. 조건 필터로 이상치 골라내고 개수·비율")

df_mask = (df["사이클타임"] < lower) | (df["사이클타임"] > upper)
print(df[df_mask][["샷", "사이클타임", "상태"]])

print(df_mask.sum(), round(df_mask.mean() * 100, 1))  # 6 3.0


line()
print("실습 4. 이상치 제거 후 크기 비교")

normal = df[~df_mask]
print(f"이상치 {len(df_mask)}, 정상 {len(normal)}")
# 이상치 202, 정상 196

print(
    f"정상값 평균 {df[df_mask]['사이클타임'].mean().round(2)}, 이상치 평균 {normal['사이클타임'].mean().round(2)}"
)
# 정상값 평균 1201.47, 이상치 평균 27.28

line()
print("실습 5. 경계값 보정 clipping")

df_clip = df["사이클타임"].clip(lower=lower, upper=upper)
print(df_clip.agg(최댓값="max", 최솟값="min", 평균값="mean").round(2))
# 최댓값    58.60
# 최솟값    20.60
# 평균값    28.28

line()
print("실습 6. 처리 전후 통계 비교")

q1 = df["실린더압력"].quantile(0.25)
q3 = df["실린더압력"].quantile(0.75)
iqr = q3 - q1
L = q1 - (iqr * 1.5)
U = q3 + (iqr * 1.5)

M = (df["실린더압력"] < L) | (df["실린더압력"] > U)
MM = df["실린더압력"].mask(M).fillna(df["실린더압력"].mask(M).median())

print(df["실린더압력"].mean().round(2))  # 234.31
print(df[~M]["실린더압력"].mean().round(2))  # 238.39
print(df["실린더압력"].clip(L, U).mean().round(2))  # 235.31


line()
print("실습 7. duplicated로 중복 찾기와 개수")

print(df.duplicated().sum())  # 완전 중복 2건
print(df.duplicated(keep=False).sum())  # 총 4개 행


line()
print("실습 8. drop_duplicates")

print(len(df))  # 202
print(len(df.drop_duplicates()))  # 200
print(len(df.drop_duplicates(subset="샷", keep="last")))  # 200
print(len(df.drop_duplicates(subset=["샷"], keep="last")))  # 200

line()
print("실습 9. reset_index로 인덱스 정리")

df_clean = df.drop_duplicates()
print(df_clean.index.min(), df_clean.index.max())  # 0 199
print(len(df_clean))  # 200

df_clean_idxreset = df_clean.reset_index(drop=True)
print(df_clean_idxreset.index.min(), df_clean_idxreset.index.max())  # 0 199
print(len(df_clean_idxreset))  # 200


line()
print("실습 10. reset_index로 인덱스 정리")
df = pd.read_csv(".venv/16_welding.csv", encoding="utf-8")
# print(df.describe())

q1_current, q3_current = df["통전전류"].quantile(0.25), df["통전전류"].quantile(0.75)
iqr_current = q3_current - q1_current
print(iqr_current)  # 106.0
low_current, up_current = q1_current - (iqr_current * 1.5), q3_current + (
    iqr_current * 1.5
)
mask_current = (df["통전전류"] > up_current) | (df["통전전류"] < low_current)
print(f"{mask_current.sum()} {round(mask_current.mean() * 100, 1)}%")  # 24 14.8%

df["통전전류"] = df["통전전류"].clip(lower=low_current, upper=up_current)
print(df["통전전류"].isna().sum())  # 0
df = df.drop_duplicates().reset_index(drop=True)

df.to_csv(".venv/16_welding_clean.csv", index=False, encoding="utf-8")
