def line():
    print("=" * 40)


import pandas as pd

df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")

line()

print("실습 1. 평균·분산·표준편차 구하기")


# 진동 열 전체의 평균·분산·표준편차를 각각 구하기
print(df["진동"].mean().round(3))  # 0.616
print(df["진동"].var().round(3))  # 0.004
print(df["진동"].std().round(3))  # 0.064
# 표준편차를 제곱하면 분산과 같아지는지 확인
print(0.064 * 0.064)  # 0.004096
# 라인으로 그룹을 나눠 라인별 평균과 표준편차 비교
print(df.groupby("냉각기상태")["진동"].mean().round(3))
print(df.groupby("냉각기상태")["진동"].std().round(3))
# # 전체 통계와 라인별 평균·표준편차 출력 (표준편차²=분산
print(df.groupby("냉각기상태")["진동"].agg(["mean", "std"]).round(3))

print(
    df.groupby("냉각기상태")
    .agg(평균온도=("온도", "mean"), 표준편차=("온도", "std"))
    .round(3)
)

line()


df = pd.read_csv(".venv/14_hydraulic_qc.csv", encoding="utf-8")
print("실습 2. 그룹별 통계 응용")

# print(df.head(2))
# print(df.tail(2))
# 판정 열로 그룹을 나눠 주요 지표들의 평균 집계
print(df.groupby("검사결과")[["지표01", "지표02"]].mean().round(2))

# 같은 그룹 기준으로 표준편차를 구해 흩어짐 비교
print(df.groupby("검사결과")[["지표01", "지표02"]].std().round(2))


# 두 그룹의 통계 차이를 읽어 불량의 특징 관찰
# 합격이 불합격보다 표준편차가 훨씬 작다.


# 합격·불합격별 지표 평균·표준편차 표 출력
print(
    df.groupby("검사결과")
    .agg(평균=("지표01", "mean"), 표준편차=("지표01", "std"))
    .round(2)
)

line()


df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")
print("실습 3. agg로 여러 통계 한 번에")


# 교대로 그룹을 나눠 진동의 평균·표준편차·최댓값을 리스트로 한 번에 -> 운전부하별그룹
print(df.groupby("운전부하")["진동"].agg(["mean", "std", "max"]).round(2))

# 이름 붙이기 방식으로 설비별 평균온도·평균진동·측정수 요약 -> 밸브상태
print(
    df.groupby("밸브상태")
    .agg(평균온도=("온도", "mean"), 평균진동=("진동", "mean"), 측정수=("온도", "count"))
    .round(2)
)

#        평균온도  평균진동  측정수
# 밸브상태
# 경미    44.86  0.62   20
# 심각    46.02  0.63   19
# 정상    45.11  0.61   61
# 지연    45.86  0.62   20

line()


df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")
print("실습 4. agg 진단표 만들기")


# 설비로 그룹을 나눠 측정수·평균온도·온도편차·평균진동·평균압력을 이름 붙여 집계
report = (
    df.groupby("밸브상태")
    .agg(
        측정수=("온도", "count"),
        평균온도=("온도", "mean"),
        온도편차=("온도", "std"),
        평균진동=("진동", "mean"),
        평균압력=("압력", "mean"),
    )
    .round(2)
)

print(report)
# 온도편차를 기준으로 내림차순 정렬
print(report.sort_values("온도편차", ascending=False))


line()


df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")
print("실습 5. 그룹별 통계량 종합")

# 온도 열의 전체 평균과 표준편차로 기준선 파악
print(df["온도"].mean().round(2))  # 45.34
print(df["온도"].std().round(2))  # 8.04
# 라인별 평균과 중앙값을 함께 구해 치우침 확인
print(df.groupby("냉각기상태")["온도"].agg(["mean", "median"]).round(2))
# 냉각기상태
# 고장     54.67   55.45
# 저하     45.46   44.90
# 정상     35.89   35.90


# 설비 진단표를 온도편차 순으로 정렬해 우선 점검 대상 선정
report = (
    df.groupby("밸브상태")
    .agg(평균온도=("온도", "mean"), 온도편차=("온도", "std"), 평균진동=("진동", "mean"))
    .round(2)
)
print(report.sort_values("온도편차", ascending=False))
