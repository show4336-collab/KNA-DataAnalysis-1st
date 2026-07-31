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

print("========================================")
print("       설비 종합 모니터링 리포트         ")
print("========================================")

temps_1 = 0
temps_2 = 0
temps_3 = 0
n = 0
for name, temp, vibe in sensors:
    if temp > 90 or vibe > 5.0:
        temps_1 += 1
        n += 1
        print(f" {n}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 위험 🚨")
    elif temp >= 80 or vibe >= 3.0:
        temps_2 += 1
        n += 1
        print(f" {n}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 주의 ❗")
    else:
        temps_3 += 1
        n += 1
        print(f" {n}. {name} | 온도 {temp}℃ | 진동 {vibe}mm/s | 정상 ✅")
print("========================================")
print(f"총 설비 : {len(sensors)}대")
print(f"정상 : {temps_3} / 주의 : {temps_2} / 위험 : {temps_1}")
temp_1 = 0
temp_2 = 0
for name, temp, vibe in sensors:
    if temp > 90 or vibe > 5.0:
        temp_1 += 1
    elif temp >= 80 or vibe >= 3.0:
        temp_2 += 1
print(f"이상설비 비율 : {round(((temp_1 + temp_2)/len(sensors)), 1)*100}%")

total = 0
for name, temp, vibe in sensors:
    total += temp
    print(f"평균 온도 : {round((total/len(temp)), 1)}")

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)


# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)


# TODO 4. 전체 평균 온도 출력 (round)


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)


# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
