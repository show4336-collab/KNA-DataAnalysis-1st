# set

# 자동 중복 제거
# 순서가 없음
# 형태는 중괄호 감싸서 작성

# 빈 set 만들기

# empty_list = []  # 빈 리스트
# empty_tuple = ()  # 빈 튜플
# print(type(empty_list))  # <class 'list'>
# print(type(empty_tuple))  # <class 'tuple'>


# empty_set = {}
# print(type(empty_set))  # <class 'dict'>
# 빈 중괄호는 딕셔너리라는 다른 자료형으로 생성

# 빈 셋은 무조건 set() 내장함수를 사용
# real_empty_set = set()
# print(type(real_empty_set))  # <class 'set'>

# 값을 포함한 셋 만들기
# logs = ["s01", "s02", "s01", "s03", "s01"]

# 리스트를 {}에 감쌀 경우
# TypeError : cannot use 'list' as a set element
# unique = {logs}

# 복수의 값을 중괄호에 감싸 작성
# unique = {"s01", "s02", "s01", "s03", "s01"}
# print(type(unique)) # <class 'set'>
# print(unique) # {"s01", "s02", "s03"}

# set() 사용
# unique = set(logs)
# print(type(unique))  # <class 'set'>
# print(unique)  # {'s02', 's03', 's01'}
# unique 셋에는 기존 중복되었떤 s01이 한 번만 들어감
# 지금은 길이가 짧아서 순서대로 정렬된 것처럼 보이지만
# 셋은 순서가 없는 값의 묶음
# print(unique[0]) # TypeError : 'set' object is not subscriptable
# set에서 인덱스 사용 시 Error 발생

# set에 바로 여러 값을 작성
# unique = set(["s01", "s02", "s01", "s03", "s01"])
# set()안에 리스트 또는 리스트가 있는 변수가 들어가야함
# print(type(unique)) # <class 'set'>
# print(unique) # {'s01', 's02', 's03'}

# set을 사용해서
# 리스트에 들어있는 유니크한 값의 종류 수를 알 수 있음
# print(len(unique)) # 3

# add 코드로 확인
# ===================
# 셋에 값 추가하기
# 셋.add(추가할 값)
# 이미 있는 값을 추가할 경우 무시

# alerts = {"s01", "s02"}
# alerts.add("s03")
# print(alerts)  # {"s01", "s03", "s02"} 순서는 모름
# alerts.add("s01")
# print(alerts)  # {"s01", "s02"}

# s01에서 또 경고가 발생
# 이미 s01은 경고가 발생한 적이 있고
# alerts라는 셋에는 경고가 발생한 센서만 저장하고 싶음
# 횟수 상관없이 이럴 때 set을 쓰면 편리함
# alerts.add("s01")
# print(alerts)  # {"s01", "s02"}
# s01이라는 값을 또 넣어도 무시하고 한 번만 저장
# 그래서 독립적인 값을 저장하기에는 아주 편리함

# ================
# set에 특정 값 포함 여부 확인
# unique = {"s01", "s02", "s01", "s03", "s01"}
# unique = {"s01", "s02", "s03"}
# 리스트와 셋을 비교해보면
# set이 길이가 짧음 (중복을 제거하기 때문에)
# set은 인덱스가 없음
# 순회 속도가 리스트보다 빠름

# print("s01" in unique)  # True
# 이렇게 출력하기보단 조건문을 활용해서
# 포함 여부 확인 후 특정 동작 실행시킴

# if "s01" in unique:
#     print(f"s01 정비 필요")

# 질문) set을 정렬한다면?
# unique = {"s01", "s02", "s01", "s03", "s01"}
# sorted = sorted(unique)
# print(unique) # ['s01', 's02', 's03']
# print(type(sorted)) # <class 'list'>

# 실습 4. 셋으로 중복 센서 제거하기
# list = ["WQR_01", "WQR_01", "WQR_01", "WQR_01", "WQR_06", "WQR_06", "WQR_03", "WQR_05"]
# sensor_list = set(list)
# print(sorted(sensor_list))
# print(f"종류 수 : {len(sensor_list)}")

# =====================================
# 집합 연산
hour_14 = {"WQR_01", "WQR_06", "WQR_07", "WQR_02"}
hour_15 = {"WQR_01", "WQR_07", "WQR_03", "WQR_09", "WQR_11"}

# 합 집합
# print(sorted(hour_14.union(hour_15)))
# ['WQR_01', 'WQR_02', 'WQR_03', 'WQR_06', 'WQR_07', 'WQR_09', 'WQR_11']
# print(hour_14)
# .union은 원본 셋에 변화 x
# print(sorted(hour_15.union(hour_14)))
# ['WQR_01', 'WQR_02', 'WQR_03', 'WQR_06', 'WQR_07', 'WQR_09', 'WQR_11']
# print(hour_15)
# .union은 원본 셋에 변화 x
# print(sorted(hour_14 | hour_15))
# | 연산자를 활용해 짧게 작성 가능
# ['WQR_01', 'WQR_02', 'WQR_03', 'WQR_06', 'WQR_07', 'WQR_09', 'WQR_11']

# 교집합
# union이랑 동일하게 두 코드는 똑같은 결과를 출력
# 앞, 뒤 순서가 결과에 영향을 미치지 않음
# print(sorted(hour_14 | hour_15))
# print(sorted(hour_14.intersection(hour_15)))
# print(sorted(hour_15.intersection(hour_14)))
# & 연산자 사용 교집합
# print(sorted(hour_14 & hour_15))
# 위 3개의 print문은 공통으로 ['WQR_01', 'WQR_07'] 출력

# 차집합
# 순서에 따라 결과가 다름
# 앞에 작성된 셋에서
# difference의 인자로 전달된 셋에 있는 값들을
# 제외한 결과를 출력
# print(hour_14.difference(hour_15))  # {'WQR_02', 'WQR_06'}
# print(hour_15.difference(hour_14))  # {'WQR_11', 'WQR_03', 'WQR_09'}
# & 연산자 사용 차집합
# print(hour_14 - hour_15)  # {'WQR_02', 'WQR_06'}
# print(hour_15 - hour_14)  # {'WQR_11', 'WQR_03', 'WQR_09'}
# print(hour_14 - hour_14)  # set()

# 실습 5. 두 라인의 센서 구성 비교하기
# line_a = {"s01", "s02", "s03", "s05"}
# line_b = {"s03", "s04", "s05"}
# print(line_a | line_b) # {'s03', 's04', 's01', 's02', 's05'}
# print(line_a & line_b) # {'s03', 's05'}
# print(line_a - line_b) # {'s02', 's01'}
# print(line_b - line_a) # {'s04'}

# 실습 6. 두 시점의 이벤트 센서 추적하기
# sensor_30 = {"s01", "s02", "s03"}
# sensor_31 = {"s02", "s03", "s05"}
# print(f"신규 이상 : {sensor_31 - sensor_30}") # 신규 이상 : {'s05'}
# print(f"지속 이상 : {sensor_30 & sensor_31}") # 지속 이상 : {'s02', 's03'}
