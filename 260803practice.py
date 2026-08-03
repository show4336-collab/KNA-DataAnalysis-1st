print(f"===============================================================")
print(f"실습 3. 딕셔너리로 통계 내기")
sensors = {"온도": 72, "압력": 95, "진동": 50}

value_max = 0
value_sum = 0
for name, value in sensors.items():
    value_sum += value
    if value > value_max:
        value_max = value
        max_name = name
print(f"평균 : {round(value_sum / len(sensors), 1)}")
print(f"최댓값 센서 : {max_name} {value_max}")


print(f"===============================================================")
print(f"실습 4. zip으로 센서명-값 매핑하기")

sensor_name = ["온도", "압력", "진동"]
sensor_value = [10, 20, 30]
sensor = dict(zip(sensor_name, sensor_value))
print(sensor)
for name, value in sensor.items():
    print(name, value)

print(f"===============================================================")
print(f"실습 5. 임계값으로 경고 센서 분류하기")

sensors = {"온도": 15, "압력": 20, "진동": 30}
limits = {"온도": 10, "압력": 30, "진동": 40}

limit_list = []

for name, value in sensors.items():
    if value > limits.get(name, 0):
        limit_list.append(name)
print(f"경고 센서 : {limit_list}")

print(f"===============================================================")
print(f"실습 6. 중첩 딕셔너리로 설비 관리하기")

sensors = {"1번펌프": {"온도": 75, "압력": 60}, "2번펌프": {"온도": 95, "압력": 60}}
print(sensors["1번펌프"]["온도"])  # 95
for name, info in sensors.items():
    for names, value in info.items():
        if value > 90:
            print(f"{name} 점검 필요")

print(f"===============================================================")
print(f"실습 7. 표 데이터를 딕셔너리로 변환하기")

sensors = {}
sensors_list = ["압력, 10", "온도, 20", "진동, 30"]
for name in sensors_list:
    name = name.split(",")
    sensors[name[0]] = float(name[1])

print(sensors)

print(f"===============================================================")
print(f"실습 8. 센서 데이터 통합 정리")

sensors = {"온도": 95, "압력": 90, "진동": 100}
limits = {"온도": 90, "압력": 80, "진동": 120}


sensors_avg = sum(sensors.values()) / len(sensors)
print(round(sensors_avg, 1))


limits_over = set()

for name, value in sensors.items():
    if value > limits.get(name, 0):
        limits_over.add(name)
print(limits_over)
