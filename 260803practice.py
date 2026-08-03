# 실습 2. update로 여러 값 한 번에 갱신하기
print(f"실습 2")
sensors = {"센서명": "모터", "온도": 72}
sensors.update({"압력": 100})
print(sensors)  # {'센서명': '모터', '온도': 72, '압력': 100}
del sensors["온도"]
print(len(sensors))

print(f"===============================================================")
# 실습 3. 딕셔너리로 통계 내기
print(f"실습 3")

sensors = {"압력": [80, 85, 95]}
total = round(sum(sensors["압력"]) / len(sensors["압력"]), 1)
print(f"평균 : {total}")
max = 0
for name, values in sensors.items():
    for index in values:
        if index > max:
            max = index
print(f"최댓값 센서 : {name} {max}")

print(f"===============================================================")
# 실습 6. 중첩 딕셔너리로 설비 관리하기
print(f"실습 6")

sensors = {"1번펌프": {"온도": 75, "압력": 60}, "2번펌프": {"온도": 95, "압력": 60}}
print(sensors["1번펌프"]["온도"])  # 95
for name, info in sensors.items():
    for names, value in info.items():
        if value > 90:
            print(f"{name} 점검 필요")
