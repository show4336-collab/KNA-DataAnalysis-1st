# 리스트로 크루 여러분의 이름을 나열해봅시다.
data_class_list = ["태구", "수진", "영준"]

# 딕셔너리로 정확하게 역할까지 부여해봅시다.

data_class_dict = {"반장": "태구", "부반장": "수진", "당번": "영준"}

# 센서로부터 얻는 예시 데이터로 딕셔너리 만들어봅시다.
sensors = {"motor_temp": 36, "vib": 0.5}
print(sensors)  # {"motor_temp": 36, "vib": 0.5}
print(type(sensors))  # <class 'dict'>

empty = {}
print(empty)  # {}
print(type(empty))  # <class 'dict'>

print(sensors["motor_temp"])
print(sensors["vib"])

