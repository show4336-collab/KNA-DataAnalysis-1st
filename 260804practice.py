def line():
    print("=================================")


# 실습 2. 다중 매개변수로 센서값 계산하기

print("실습 2")


def counting(name, temp):
    print(f"{name} {temp}도")


counting("모터", 78)
counting("펌프", 92)

line()


# 실습 3. 키워드 인자로 함수 호출하기
print("실습 3")


def sensor(name, value):
    print(f"{name} {value}")


sensor(value=78, name="모터")
sensor("펌프", value=92)

line()
# 실습 4. 반환값으로 간단 계산기 만들기
print("실습 4")


def value(value1, value2):
    return (value1 + value2) / 2


avg1 = value(80, 90)
avg2 = value(85, 95)

print(avg1)
print(avg2)

line()


# 실습 5. 센서 통계 함수 만들기
print("실습 5")


def sensor(value):
    return min(value), max(value), sum(value) / len(value)


sensor_list = [78, 92, 86, 90]
minimum, maximum, avg = sensor(sensor_list)
print(minimum, maximum, avg)

line()

# 실습 3. 처리 흐름 만들기
print("실습 3")


def judge(temp1, temp2):
    return temp1 + temp2


temp_sum = judge(80, 90)


def judge2(status="정상", avg=temp_sum / 2, avg_limit=90):
    if avg < avg_limit:
        return print(f"평균 {avg} → {status}")
    else:
        status = "경고"
        return print(f"평균 {avg} → {status}")


judge2()

line()


# 실습 4. 센서 분석 함수 세트 만들기
print("실습 4")
temp_list = [80, 85, 90]


def sensors(sensor):
    return sum(temp_list) / len(temp_list)


avg = sensors(temp_list)


def judge(temp_avg=avg, limit=90):
    if temp_avg < limit:
        return print(f"{avg} 정상")
    return print(f"{avg} 경고")


judge()
