def line():
    print("=" * 40)


import pandas as pd

line()

df = pd.read_csv(".venv/14_hydraulic_qc.csv", encoding="utf-8")

print("실습 1. 상관계수와 상관 행렬 구하기")

# corr로 두 지표의 상관계수를 구해 부호와 절댓값 해석
# 여러 지표 열을 골라 corr로 상관 행렬 생성
# 대각선(항상 1)과 대칭 구조를 확인하고 절댓값 큰 칸 찾기
print(df[["지표01", "지표02", "지표03", "지표04"]].corr().round(3))  # -0.983


line()

df = pd.read_csv(".venv/14_hydraulic_qc.csv", encoding="utf-8")
print("실습 2. 강한 상관 쌍 찾기")

# 여러 지표 열로 상관 행렬을 만들기
feat = ["지표%02d" % i for i in range(1, 11)]
print(feat)
cm = df[feat].corr().round(3)
print(cm)
# 이중 반복으로 대각선을 제외한 각 쌍의 상관계수 확인
# 위 cm 자료에서 0.4 이상의 상관관계가 크다 판단되는 경우를 뽑아보기
for i in range(len(cm.columns)):
    print(f"{i}번째 컬럼 이름 {cm.columns[i]}")

    # i + 1번부터 챙겨 비교해야, 대각선 중심의 반대편을 중복 비교하지 않게 할 수 있다.
    for j in range(i + 1, len(cm.columns)):

        c = cm.iloc[i, j]
        print(f"{i}번째 컬럼 {cm.columns[i]}과 비교할 {cm.columns[j]} : {c}")  #
        # 8번째 컬럼 지표09와 비교할 지표10 : -0.951
        # abs로 - 부호 없는 절대값 만들기
        if abs(c) > 0.4:
            print(
                f"{i}번째 컬럼 {cm.columns[i]}과 비교할 {cm.columns[j]} : {c} -> 강한 상관계수"
            )
#     # 별도의 배열을 만들어 해당 배열에 결과를 추가하고
# 반복문이 끝나면 바깥에서 출력 처리 및 가장 큰 값도 찾고, 강한쌍이 몇개인지도 출력


# 0번째 컬럼 이름 지표01
# 1번째 컬럼 이름 지표02
# 2번째 컬럼 이름 지표03
# 3번째 컬럼 이름 지표04
# 4번째 컬럼 이름 지표05
# 5번째 컬럼 이름 지표06
# 6번째 컬럼 이름 지표07
# 7번째 컬럼 이름 지표08
# 8번째 컬럼 이름 지표09
# 9번째 컬럼 이름 지표10

# 절댓값이 기준 이상인 쌍만 모아 큰 순서로 정렬
# 절댓값 0.4 이상 쌍 3개 출력 (07-08 -0.969 최대)
import pandas as pd

df = pd.read_csv(".venv/14_hydraulic_qc.csv", encoding="utf-8")

r1 = df["지표07"].corr(df["지표08"])

print(r1.round(3))  # -0.969

cols = [
    "지표01",
    "지표02",
    "지표03",
    "지표04",
    "지표05",
    "지표06",
    "지표07",
    "지표08",
    "지표09",
    "지표10",
]
r2 = df[cols].corr()
print(r2.round(2))

line()

print("실습 3. 그룹별 상관 비교")
df = pd.read_csv(".venv/14_hydraulic_qc.csv", encoding="utf-8")

# 판정 열로 합격·불합격 그룹을 나누기 -> '검사결과' 컬럼
# 각 그룹에서 같은 두 지표의 상관계수를 계산
# 전체·합격·불합격 상관을 비교하고 표본 수 주의

# 전체 데이터의 지표07과 08의 상관관계
r_all = df["지표07"].corr(df["지표08"])
print(r_all.round(3))  # -0.969
r_qa = df[df["검사결과"] == "합격"]
r_qb = df[(df["검사결과"] == "불합격")]
print(r_qa["지표07"].corr(r_qa["지표08"]).round(3))  # 0.385
print((r_qb["지표07"]).corr((r_qb["지표08"])).round(3))  # -0.998

# 해석
# 검사결과 합격의 경우 지표07과 지표08사이에 관계성이 약함
# 불합격이면 그 관계성이 강하다.


print("실습 4. 통합 리포트 종합")
df = pd.read_csv(".venv/14_equipment_sensor.csv", encoding="utf-8")

# print(df.columns)
# 라인으로 그룹을 나눠 측정수·평균온도·온도편차 요약
report = (
    df.groupby("line")
    .agg(측정수=("temp", "count"), 평균온도=("temp", "mean"), 온도편차=("temp", "std"))
    .round(2)
)
print(report.sort_values("온도편차", ascending=False))

#       측정수   평균온도   온도편차
# line
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60
# C라인    31  79.88  10.38

# 위 표 안에서도 온도편차가 큰 경우가 심각한 정보라서 우선 나타나게 해주자.
#       측정수   평균온도   온도편차
# line
# C라인    31  79.88  10.38
# A라인    54  76.86  10.18
# B라인    35  77.69   7.60
# 온도(temp)와 진동(vibration)의 상관계수(corr)를 구해 함께 움직임 확인

print(df["temp"].corr(df["vibration"]).round(2))  # 0.34
# 고장 행을 걸러 라인별 고장 건수까지 더해 우선 점검 대상 정리

df_bad = df[df["result"] == "고장"]
print(df_bad)
print(f'라인별 고장 건수 \n{df_bad.groupby("line").size()}')
# 라인별 고장 건수
# line
# A라인    16
# B라인     6
# C라인     6
