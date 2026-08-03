# =====================================================================
# 종합 실습 3. 교대조 센서 경고 로그 분석
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

morning = ["TZ_11", "TZ_13", "TZ_11", "TZ_15", "TZ_13", "TZ_11", "TZ_11", "TZ_17"]
afternoon = ["TZ_13", "TZ_15", "TZ_13", "TZ_19", "TZ_15", "TZ_21", "TZ_13", "TZ_15"]

morning_set = set(morning)
afternoon_set = set(afternoon)
total_set = sorted(morning_set | afternoon_set)

print(f"==========================교대조 센서 경고 로그 분석==========================")
print(f"오전조 고유 센서 {len(morning_set)}종 : {sorted(morning_set)}")
print(f"오후조 고유 센서 {len(afternoon_set)}종 : {sorted(afternoon_set)}")
print(f"-----------------------------------------------------------------------------")
print(f"양 교대조 공통 경고 센서 : {sorted(morning_set & afternoon_set)}")
print(f"오전조 전용 : {sorted(morning_set - afternoon_set)}")
print(f"오후조 전용 : {sorted(afternoon_set - morning_set)}")
print(f"전체 경고 센서 {len(total_set)}종 : {total_set}")
print(f"-----------------------------------------------------------------------------")

total_count = []

for sensor in total_set:
    total_count.append((morning.count(sensor) + afternoon.count(sensor), sensor))
total_count = sorted(total_count, reverse=True)

print(f"경고 발생 횟수 순위 :")

for rank, (count, sensor) in enumerate(total_count):
    print(f"{rank + 1}위 : {sensor} - {count}회")

print(f"-----------------------------------------------------------------------------")
print(f"최다 경고 센서 : {total_count[0][1]} ({total_count[0][0]}회) → 우선 점검 필요")

danger_list = []
for count, sensor in total_count:
    if count >= 3:
        danger_list.append(sensor)

print(f"집중 관리 대상 센서 : {sorted(danger_list)}")

# TODO 1. 오전조 / 오후조 각각 고유 센서 종류 수 + 정렬된 목록 출력
#         (set 으로 중복 제거 > sorted 로 정렬)


# TODO 2. 교집합 (두 조 모두에서 경고 난 센서) 정렬해서 출력  ( & )


# TODO 3. 차집합 (오전 전용 / 오후 전용) 각각 정렬해서 출력  ( - )
#         방향에 따라 결과 다른 것 유의


# TODO 4. 합집합 (전체 경고 센서) 종류 수 + 정렬된 목록 출력  ( | )


# TODO 5. 센서마다 (오전 횟수 + 오후 횟수) 구해서
#         (횟수, 센서명) 튜플 리스트 만들고 횟수 많은 순 정렬
#         "N위: 센서명 - X회" 형태로 출력
#         힌트) morning.count("TZ_13") / sorted(리스트, reverse=True)


# TODO 6. 가장 경고 많았던 센서 콕 집어서 "우선 점검 필요" 출력


# 도전) 총 3회 이상인 센서만 "집중 관리 대상" 리스트로 만들어 정렬 출력
