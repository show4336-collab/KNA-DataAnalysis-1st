def line():
    print("=" * 40)


import pandas as pd

df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")

line()

print("실습 4. groupby로 그룹 집계")

# 냉각기상태별 압력 평균

print(df.groupby("냉각기상태")["압력"].mean().round(2))
# 고장    163.68
# 저하    158.49
# 정상    160.84

# 집계 함수를 바꿔 설비별 최고 온도 확인 - max, min
print(df.groupby("밸브상태").size())
# 경미    20
# 심각    19
# 정상    61
# 지연    20
print(df.groupby("result")["온도"].max())
# 고장    57.8
# 정상    57.2

# 운전부하별로 size로 갯수 세기 (결측 - null값 갯수도 포함)
print(df.groupby("운전부하").size())
# 고부하    60
# 저부하    60

line()

print("실습 5. 그룹별 평균 비교와 정렬")


# 설비로 그룹을 나눠 진동 평균 집계
print(df.groupby("밸브상태")["진동"].mean().round(3))
# 집계 결과에 정렬을 이어 붙여 내림차순으로 정렬
print(df.groupby("밸브상태")["진동"].mean().round(3).sort_values(ascending=False))
# 심각    0.629
# 지연    0.621
# 경미    0.617
# 정상    0.609


line()

print("실습 6.여러 기준 조합 그룹")

# 냉각기상태, 운전부하 기준순서를 잡아 각 그룹별 진동평균

# 라인과 교대 두 기준을 묶어 진동 평균 집계
print(df.groupby(["냉각기상태", "운전부하"])["진동"].mean().round(3))
# 고장     고부하     0.726
#        저부하     0.660
# 저하     고부하     0.616
#        저부하     0.610
# 정상     고부하     0.549

# 같은 두 기준으로 size를 구해 조합별 측정 건수 확인
print(df.groupby(["냉각기상태", "운전부하"]).size())
# 고장     고부하     17
#        저부하     23
# 저하     고부하      3
#        저부하     37
# 정상     고부하     40

line()

print("실습 7.빈도와 그룹 집계 종합")

# value_counts로 설비 구성과 정상·고장 비율 파악
print(df["밸브상태"].value_counts())  # count니까 null값은 무시
# 정상    61
# 지연    20
# 경미    20
# 심각    19
print(df["밸브상태"].value_counts(normalize=True).round(3))
# 정상    0.508
# 지연    0.167
# 경미    0.167
# 심각    0.158
# 고장 행만 걸러 라인별 고장 건수 집계
print(len(df[df["result"] == "고장"]))  # 53
# print(df.groupby("result").size())  # 고장 53 정상 67
# print(df["result"].value_counts())  # 정상 67 고장 53
# groupby로 설비별 온도·진동 평균까지 비교
print(df.groupby("냉각기상태")[["온도", "진동"]].mean().round(2))
