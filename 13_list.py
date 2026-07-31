# 기존 배열의 모든 요소에 3을 곱한 값을 가진 새 리스트 생성
# temps = [1, 5, 2, 7, 4, 8, 10, 3]
# doubled = []

# for t in temps:
#     doubled.append(t * 3)
# print(doubled)

# 조건에 맞는 값으로 새 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3]
# high = []
# low = []
# for t in temps:
#     if t < 5:
#         low.append(t)
#     else:
#         high.append(t)
# print(low)
# print(high)


# 복습) sort() : 원본 배열을 오름차순으로 정렬해줌
# 하지만 반환해주지 않기 때문에 print로 바로 찍으면 None

# 정렬된 배열을 출력하고 싶다면
# low.sort()
# high.sort()

# print(low)
# print(high)

# temps = [20, 21, 24, 29, 32, 31, 35, 33]
# lists = []
# for t in temps:
#     if t > 30:
#         lists.append(t)
# lists.sort()
# print(f"{lists} / 개수 {len(lists)}")

# temps = [30.1, 40.2, 50.3, 60.4, 70.5]
# lists = []
# for t in temps:
#     lists.append(round(((t * 1.8) + 32), 1))
# print(lists)

# 리스트 안의 리스트
# sensors = [[5, 6], [7, 8]]
# print(sensors[0][1])
# 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터
# 바깥 대괄호를 "행", 안쪽 인덱스 리스트를 "열"

rows = [["펌프", 25], ["모터", 32], ["냉각기", 15]]

# print(rows[0]) # ['펌프', 25]
# print(type(rows[0])) # <class 'list'>
# print(type(rows)) # <class 'list'>
# 중첩된 리스트 안의 값에 접근
# print(rows[1][1])
# 1. rows[1]을 찾음 -> ["모터", 32]
# 2. print(["모터", 32[1]]) -> [1] 앞의 리스트에서 1번 인덱스 값에 접근
# 3. print(32) -> 32 출력
# 중첩된 리스트 내부의 값은 대괄호를 여러번 이어서 접근

# for row in rows:
# print(row[0], "온도", row[1])  # 펌프 온도 25
# rows는 리스트를 담고 있는 큰 리스트
# row는 rows 안에 있는 작은 리스트 ex) ["펌프", 25] 하나

# 실습 6. 센서 데이터 종합 분석하기
# 첫 번째 작성
# temps = [10, 15, 30, 40, 50, 60, 70, 80]
# total = []
# for t in temps:
#     if t > 30:
#         total.append(t)
# tempss = len(temps)
# temps = sum(temps)
# totals = len(total)
# total = sum(total)
# print(
#     f"전체 평균 : {round(temps / tempss, 1)} / 고온 개수 : {totals} / 고온 평균 : {round(total / totals)}"
# )

# 두 번째 작성 / 훨씬 단순하고 보기 좋음
# temps = [10, 20, 30, 40, 50, 60, 70]
# high_temps = []
# for t in temps:
#     if t > 30:
#         high_temps.append(t)
# print(
#     f"전체 평균 : {sum(temps) / len(temps)} / 고온 개수 : {len(high_temps)} / 고온 평균 : {sum(high_temps) / len(high_temps)}"
# )
