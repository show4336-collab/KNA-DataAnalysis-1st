# 리스트로 크루 여러분의 이름을 나열해봅시다.
# data_class_list = ["태구", "수진", "영준"]

# 딕셔너리로 정확하게 역할까지 부여해봅시다.

# data_class_dict = {"반장": "태구", "부반장": "수진", "당번": "영준"}

# 센서로부터 얻는 예시 데이터로 딕셔너리 만들어봅시다.
# sensors = {"motor_temp": 36, "vib": 0.5}
# print(sensors)  # {"motor_temp": 36, "vib": 0.5}
# print(type(sensors))  # <class 'dict'>

# empty = {}
# print(empty)  # {}
# print(type(empty))  # <class 'dict'>

# print(sensors["motor_temp"])
# print(sensors["vib"])

# sensors["motor_temp"] = 40
# print(sensors)  # {"motor_temp": 40, "vib": 0.5}

# sensors["sensor_name"] = "pump"  # sensor_name이라는 key에 pump라는 value를 추가
# sensors["flow"] = 10  # flow라는 key에 10이라는 value를 추가

# print(sensors)

# print(sensors)
# del sensors["flow"]  # flow라는 key와 value를 삭제

# 딕셔너리.get(키, 기본값)
# 키 있으면 값, 없으면 오류 대신 None 반환
# 두 번째 인자로 기본값을 지정 가능
# 여러 설비의 값을 더할 때 센서를 0 처리
# sensors.get("flow")
# print(sensors.get("flow"))  # None
# print(sensors.get("flow", 0))  # 0

# motor_degree에 숫자가 안담기면 에러 발생
# next_degree = motor_degree + 10
# print(next_degree)

# sensors = {"모터온도": 12, "진동": 0.5}

# is_motor_degree_key = "모터온도" in sensors
# print(is_motor_degree_key)  # True

# is_motor_degree_key가 True일 경우
# if True:랑 같은 의미임
# if is_motor_degree_key:
# print("그런 키 있어요!")
# else:
# print("그런 키 없어요!")

# is_motor_degree_key = "압력" in sensors
# print(is_motor_degree_key)  # False

# is_motor_degree_key가 Fasle일 경우
# if False:랑 같은 의미
# if False:면 else:로 간다.

# if is_motor_degree_key:
#     print("그런 키 있어요!")
# else:
#     print("그런 키 없어요!")

# 하지만 실무에서는 변수로 저장안하고 바로 print로 해버림

# sensors = {"모터온도": 12, "진동": 0.5}

# keys를 가져와봅시다!
# print(sensors.keys())  # dict_keys(['모터온도', '진동'])
# values를 가져와봅시다!
# print(sensors.values())  # dict_values([12, 0.5]) / 잘 쓰지 않음! 값들의 type이 달라서
# len을 통해 몇개의 key-value 조합들이 있는지 살펴봅시다
# print(len(sensors))  # 2

# 딕셔너리.items()

# for name, value in sensors.items():
#     print(name)
#     print(value)

# len으로 항목 개수 세기
# len( 딕셔너리 )
# 키와 값은 항상 짝이니 키 개수가 곧 센서 수

# 재미난 사례를 추가로 만들어봅시다.
# 나라 이름들로 정리해봅시다
# 유럽 : 스페인(ESP), 프랑스(FRA), 독일(GER), 스위스(SUI), 네덜란드(NED)
# 아시아 : 한국(KOR), 일본(JPN), 중국(CHN), 사우디(SAU), 이란(IRN)
# 남미 : 아르헨티나(ARG), 브라질(BRA), 칠레(CHI), 콜롬비아(COL), 우루과이(URU)

# korea = {"국가명": "대한민국", "약칭": "KOR"}
# japan = {"국가명": "일본", "약칭": "JPN"}

# # 아시아 나라들을 하나의 리스트로 모아봅시다
# asia = [korea, japan]
# print(asia) # [{'국가명': '대한민국', '약칭': 'KOR'}, {'국가명': '일본', '약칭': 'JPN'}]

# 조별과제
# 포켓몬 1, 2, 3 진화단계들을 딕셔너리로 만들고
# 그 포켓몬 딕셔너리들이 최소 10개 모인 배열을 만들어봅시다
# 그 배열 데이터를 화면에 print 합니다.
# 가능하면 그 배열의 데이터들을 for-in을 사용해서 하나씩 꺼내 print 합시다(선택사항)

# 파이리 = {"1단계": "파이리", "2단계": "리자드", "3단계": "리자몽"}
# 꼬부기 = {"1단계": "꼬부기", "2단계": "어니부기", "3단계": "거북왕"}
# 구구 = {"1단계": "구구", "2단계": "피죤", "3단계": "피죤투"}
# 이상해씨 = {"1단계": "이상해씨", "2단계": "이상해풀", "3단계": "이상해꽃"}
# 고오스 = {"1단계": "고오스", "2단계": "고오소트", "3단계": "팬텀"}
# 물짱이 = {"1단계": "물짱이", "2단계": "수륙챙이", "3단계": "강챙이"}
# 미뇽 = {"1단계": "미뇽", "2단계": "신뇽", "3단계": "망나뇽"}
# 캐터피 = {"1단계": "캐터피", "2단계": "단데기", "3단계": "버터풀"}
# 삐삐 = {"1단계": "삐삐", "2단계": "픽시", "3단계": "메가픽시"}
# 또가스 = {"1단계": "또가스", "2단계": "또도가스", "3단계": "또또도가스"}

# pocketmon = [파이리, 꼬부기, 구구, 이상해씨, 고오스, 물짱이, 미뇽, 캐터피, 삐삐, 또가스]

# for monster in pocketmon:
#     for name, value in monster.items():
#         print(f"{name} {value}")


# ======================================================================================

# 다음의 두 딕셔너리는 같은 key들을 가지고 있습니다.
# 실제데이터
# values = {"모터온도": 95, "압력": 88}
# 임계치 데이터
# limits = {"모터온도": 90, "압력": 90}

# print로 잘나오는지 먼저 확인 해보자
# for name, value in values.items():
#     print(f"{name} : {value}")

# for name, value in values.items():
# print(f"{name} : {value}")

# limits 딕셔너리에도 name의 key가 있따면, 가져와서 비교하자! 순서는 상관없는거야.
# if value > limits.get(name, 0):
# print(name, "경고")

# 결과값
# 모터온도 : 95
# 모터온도 경고
# 압력 : 88
# limits.get(name, 0)을 쓰는건 limits라는 변수안에 있는 딕셔너리에 값은 키 값 중에
# values에 있는 name과 같은 이름일때 value와 비교하게 됨. 순서 상관 x


# sensors = {"모터온도": 78, "진동": 0.5}
# new_data = {"모터온도": 80, "유량": 42}
# sensors.update(new_data)  # 기존 딕셔너리에 새로운 딕셔너리의 key-value 조합을 추가
# print(sensors)  # {'모터온도': 80, '진동': 0.5, '유량': 42}

# zip으로 key들의 배열과 value들의 배열을 묶어서 새로운 딕셔너리를 만들 수 있습니다.
# names = ["모터온도", "진동", "압력"]
# values = [78, 0.5, 95]
# sensors = dict(
# zip(names, values)
# )  # dict.zip() 기능으로 두 배열을 사용해 묶고 dict 타입 딕셔너리로 만들기

# print(sensors) # 결과 : {'모터온도': 78, '진동': 0.5, '압력': 95}


# 딕셔너리 안에 value로 딕셔너리를 사용하기
# value는 리스트가 될 수도 있고 문자, 숫자가 될 수도 있는거임.
# kbo = [
#     {
#         "구단명": "삼성",
#         "마스코트": "라이온스",
#         "구장": {"1구장": "대구라이온스파크", "2구장": "포항야구장"},
#     },
#     {
#         "구단명": "두산",
#         "마스코트": "베어스",
#         "구장": {"1구장": "잠실야구장", "2구장": "베어스파크"},
#     },
# ]

# 쉽게 배열 안에 딕셔너리 안에 딕셔너리 접근하기

# print(kbo[0]["구장"])  # {'1구장': '대구라이온스파크', '2구장': '포항야구장'}
# print(kbo[0]["구장"]["2구장"])  # 포항야구장

# plant = {
#     "1번모터": {"온도": 78, "상태": "정상"},
#     "2번펌프": {"압력": 95, "상태": "경고"},
# }
# print(plant["2번펌프"]["압력"])


# 튜플, 셋, 딕셔너리 선택 기준
# 튜플 : 안바뀜 / 고정 묶은(센서이름, 값, 위치좌표)
# 셋 : 중복 없음 / 종류,비교(두 목록 비교, 종류 세기)
# 딕셔너리 : 이름 조회 / 이름, 값 짝 - 센서 이름으로 측정값 찾기
# 고정된 묶음은 튜플, 중복 없는 목록과 비교는 셋(셋은 순서가 없음)
# 이름으로 찾는 데이터는 딕셔너리 선택


# 실습 1.

# 1) 센서명을 키(key), 측정값을 값(value)로 딕셔너리 저장

# 2) 키로 값을 꺼내고 새 키로 추가, 기존 키로 수정
# sensors = {"센서명": "펌프", "온도": "78"}
# print(sensors["온도"])  # 값 꺼내기
# print(sensors.get("온도", 0))  # 값 더 안전하게 꺼내기 이걸로 익숙해지기

# sensors["진동"] = 95  # 없던 키를 언급하면 추가
# sensors["센서명"] = "모터"  # 있던 키를 언급하면 수정

# print(sensors)  # {'센서명': '모터', '온도': '78', '진동': 95}

# 3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인

# print(sensors.get("압력", 0))  # 압력 key는 존재하지 않아서 0으로 출력
# print("진동" in sensors) # True
# print("압력" in sensors) # False

# 실습 2. update로 여러 값 한 번에 갱신하기

# sensors = {"센서명": "모터", "온도": 72}
# sensors.update({"압력": 100})
# print(sensors)  # {'센서명': '모터', '온도': 72, '압력': 100}
# del sensors["온도"]
# print(len(sensors))

# print(f"===============================================================")
# print(f"실습 3. 딕셔너리로 통계 내기")
# sensors = {"온도": 72, "압력": 95, "진동": 50}

# value_max = 0
# value_sum = 0
# for name, value in sensors.items():
#     value_sum += value
#     if value > value_max:
#         value_max = value
#         max_name = name
# print(f"평균 : {round(value_sum / len(sensors), 1)}")
# print(f"최댓값 센서 : {max_name} {value_max}")


# print(f"===============================================================")
# print(f"실습 4. zip으로 센서명-값 매핑하기")

# sensor_name = ["온도", "압력", "진동"]
# sensor_value = [10, 20, 30]
# sensor = dict(zip(sensor_name, sensor_value))
# print(sensor)
# for name, value in sensor.items():
#     print(name, value)

# print(f"===============================================================")
# print(f"실습 5. 임계값으로 경고 센서 분류하기")

# sensors = {"온도": 15, "압력": 20, "진동": 30}
# limits = {"온도": 10, "압력": 30, "진동": 40}

# limit_list = []

# for name, value in sensors.items():
#     if value > limits.get(name, 0):
#         limit_list.append(name)
# print(f"경고 센서 : {limit_list}")

# print(f"===============================================================")
# print(f"실습 6. 중첩 딕셔너리로 설비 관리하기")

# sensors = {"1번펌프": {"온도": 75, "압력": 60}, "2번펌프": {"온도": 95, "압력": 60}}
# print(sensors["1번펌프"]["온도"])  # 95
# for name, info in sensors.items():
#     for names, value in info.items():
#         if value > 90:
#             print(f"{name} 점검 필요")

# print(f"===============================================================")
# print(f"실습 7. 표 데이터를 딕셔너리로 변환하기")

# sensors = {}
# sensors_list = ["압력, 10", "온도, 20", "진동, 30"]
# for name in sensors_list:
#     name = name.split(",")
#     sensors[name[0]] = float(name[1])

# print(sensors)

# print(f"===============================================================")
# print(f"실습 8. 센서 데이터 통합 정리")

# sensors = {"온도": 95, "압력": 90, "진동": 100}
# limits = {"온도": 90, "압력": 80, "진동": 120}


# sensors_avg = sum(sensors.values()) / len(sensors)
# print(round(sensors_avg, 1))


# limits_over = set()

# for name, value in sensors.items():
#     if value > limits.get(name, 0):
#         limits_over.add(name)
# print(limits_over)


# 간단하게 딕셔너리 예제를 만들어봅시다
# 보통 리스트 안에 딕셔너리들이 있다면, 그 딕셔너리들은 같은 key들을 갖는게 일반적

location_dict = {
    "시": [
        {"이름": "서울특별시", "기초단체": ["종로구", "중구", "마포구"]},
        {"이름": "대구광역시", "기초단체": ["중구", "수성구", "달서구"]},
    ],
    "도": [
        {"이름": "경기도", "기초단체": ["수원시", "안양시", "안산시"]},
        {"이름": "경상북도", "기초단체": ["포항시", "경주시", "김천시"]},
    ],
}

# 전체 출력
print(location_dict)
print("======================")

# 시와 도 단위 딕셔너리들을 각각 출력하기
print(location_dict["시"])
# print(locateion_dict.get("시", 0))
# 위 두개는 동일한 의미임
print(location_dict.get("도", 0))

# 각 시 도 마다 세부 딕셔너리들을 출력하기
for basic_dict in location_dict["시"]:
    print(basic_dict.get("이름"))
    print(basic_dict.get("기초단체"))
    print("------------------------")


for basic_dict in location_dict.get("도", 0):
    print(basic_dict.get("이름"))
    print(basic_dict.get("기초단체"))
    print("------------------------")

# 오늘 배울 주제
# 위 코드를 보면 두 개의 for문이 사실상 같은 일을 한다.
# 그래서 중복되는 부분을 묶고, 다른점만 외부에서 지적해 시키면 돌아가는
# '함수(functhion)'를 만들면 효율성이 높아진다.
