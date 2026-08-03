# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

print("===================================================")
print("             설비 종합 모니터링 리포트              ")
print("===================================================")

status_1 = 0
status_2 = 0
status_3 = 0
n = 0
for name, temp, vibe in sensors:
    if temp > 90 or vibe > 5.0:
        status_1 += 1
        n += 1
        print(f" {n}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 위험 🚨")
    elif temp >= 80 or vibe >= 3.0:
        status_2 += 1
        n += 1
        print(f" {n}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 주의 ❗")
    else:
        status_3 += 1
        n += 1
        print(f" {n}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 정상 ✅")

print("===================================================")
print(f"총 설비 : {len(sensors)}대")
print(f"정상 : {status_3} / 주의 : {status_2} / 위험 : {status_1}")
print(f"이상 설비 비율 : {round(((((status_2 + status_1) / len(sensors)) * 100)), 1)}%")

total = 0
total_index = 0

for name, temp, vibe in sensors:
    total += temp
    total_index += 1
print(f"평균 온도 : {round((total / total_index), 1)}℃")

temp_high = 0
name_high = "설비이름"
for name, temp, vibe in sensors:
    if temp_high < temp:
        temp_high = temp
        name_high = name
print(f"최고 온도 설비 : {name_high} ({temp_high}℃)")

danger_list = []

for name, temp, vibe in sensors:
    if temp > 90 or vibe > 5.0:
        danger_list.append(name)
print(f"위험 설비 목록 : {sorted(danger_list)}")
print("===================================================")

if len(danger_list) > 0:
    print("⚠  즉시 점검 요망")
else:
    print("✅ 전 설비 안정")

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)


# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)


# TODO 4. 전체 평균 온도 출력 (round)


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)


# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
