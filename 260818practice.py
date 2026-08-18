def line():
    print("=" * 40)


import pandas as pd

line()

print("실습 5. 위험 순으로 정렬하기")

df = pd.read_csv(".venv/13_diecasting_shot.csv", encoding="utf-8")

print(df.sort_values("비스킷두께", ascending=False).head(5))

print(
    df.sort_values(
        ["비스킷두께", "형체력"],
        ascending=[False, True],
    ).head(5)
)

# 직접 해당 값들만 뽑아서 list로 출력해보려면? 일단 series 추출하고 .tolist() 호출
# print(df.sort_values("비스킷두께", ascending=False).head(5))
# print(df.sort_values("비스킷두께", ascending=False)["비스킷두께"].head(5))
# print(df.sort_values("비스킷두께", ascending=False)["비스킷두께"].head(5).tolist())


line()
print("실습 6. 필터링과 정렬 연결")

df = pd.read_csv(".venv/13_diecasting_shot.csv", encoding="utf-8")
df_filtered = df[df["품질등급"] == "불량"]
print(df_filtered.head(5))

df_filtered_after = (
    df[df["품질등급"] == "불량"].sort_values("비스킷두께", ascending=False).head(5)
)

print(df_filtered_after)


# line()
# # print("실습 7. 이상 의심 설비 리포트")


# 워크플로우 5단계 맞춰가기

# 1. 불러오기
df = pd.read_csv(".venv/13_diecasting_shot.csv", encoding="utf-8")


# 2. 확인하기
df.info()

# 3. 필터링
df_warning = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 100)]
print(len(df_warning))  # 76

# 4. 정렬(내림차순)

df_report = df_warning.sort_values("형체력", ascending=False)[
    ["샷", "품질등급", "형체력", "사이클타임"]
]

print(len(df_report))

# 5. 선택

very_danger = df_report.head(1)
sid = int((very_danger["샷"]).tolist()[0])
force = very_danger["형체력"].tolist()[0]
print(f"가장 시급한 샷 : {sid}, 형체력 {force}, 우선 점검")
# 가장 시급한 샷 : 172, 형체력 384.0, 우선 점검

불량 = df[df["품질등급"] == "불량"].sort_values("형체력", ascending=False)
print(불량[["샷", "형체력"]].head)
